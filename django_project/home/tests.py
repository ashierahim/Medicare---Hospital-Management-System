from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import dept, Doctors, Booking
import datetime

class MedicareTests(TestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.other_user = User.objects.create_user(username='otheruser', password='password123')
        
        # Create department
        self.dept = dept.objects.create(dept_name='Cardiology', dep_desc='Heart health')
        
        # Create doctor
        self.doctor = Doctors.objects.create(doc_name='Dr. Smith', doc_spec='Heart Surgeon', dept_name=self.dept)

    def test_unauthenticated_redirects(self):
        # Unauthenticated users should be redirected to login page for protected views
        for url_name in ['index', 'booking', 'my_bookings', 'dept', 'doctors']:
            response = self.client.get(reverse(url_name))
            self.assertEqual(response.status_code, 302)
            self.assertIn('/login/', response.url)

    def test_authenticated_pages_load(self):
        self.client.login(username='testuser', password='password123')
        for url_name in ['index', 'booking', 'my_bookings', 'dept', 'doctors']:
            response = self.client.get(reverse(url_name))
            self.assertEqual(response.status_code, 200)

    def test_booking_creation_and_ownership(self):
        self.client.login(username='testuser', password='password123')
        booking_data = {
            'p_name': 'John Doe',
            'p_phone': '1234567890',
            'p_email': 'john@example.com',
            'doc_name': self.doctor.id,
            'booked_on': datetime.date.today(),
        }
        response = self.client.post(reverse('booking'), booking_data)
        
        # Redirects to My Bookings dashboard after success
        self.assertRedirects(response, reverse('my_bookings'))
        
        # Verify database record exists and is linked to correct user
        bookings = Booking.objects.filter(p_name='John Doe')
        self.assertEqual(bookings.count(), 1)
        self.assertEqual(bookings.first().user, self.user)

    def test_dashboard_isolation(self):
        # Create a booking for user
        Booking.objects.create(
            user=self.user,
            p_name='John Doe',
            p_phone='1234567890',
            p_email='john@example.com',
            doc_name=self.doctor,
            booked_on=datetime.date.today()
        )
        # Create a booking for other_user
        Booking.objects.create(
            user=self.other_user,
            p_name='Jane Doe',
            p_phone='0987654321',
            p_email='jane@example.com',
            doc_name=self.doctor,
            booked_on=datetime.date.today()
        )
        
        # Log in as user
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('my_bookings'))
        
        # Dashboard should only list user's bookings, not other_user's bookings
        self.assertContains(response, 'John Doe')
        self.assertNotContains(response, 'Jane Doe')

    def test_booking_cancellation(self):
        booking = Booking.objects.create(
            user=self.user,
            p_name='John Doe',
            p_phone='1234567890',
            p_email='john@example.com',
            doc_name=self.doctor,
            booked_on=datetime.date.today()
        )
        self.client.login(username='testuser', password='password123')
        
        # Post request to cancel
        response = self.client.post(reverse('cancel_booking', args=[booking.id]))
        self.assertRedirects(response, reverse('my_bookings'))
        
        # Verify deleted
        self.assertEqual(Booking.objects.filter(id=booking.id).count(), 0)
