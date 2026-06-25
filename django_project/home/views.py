from django.shortcuts import render, redirect, get_object_or_404
from .models import dept as department, Doctors, Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def book(request):
    return render(request, 'booking.html')
@login_required
def dept(request):
    dict_dept = {
        'dept': department.objects.all()
    }
    return render(request, 'dept.html', dict_dept)

@login_required
def doctors(request):
    # Fetching the data from the database
    data = Doctors.objects.all()
    dict_docs = {
        'doctors': data  
    }
    return render(request, 'doctors.html', dict_docs)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.user = request.user
            booking_instance.save()
            return redirect('my_bookings')
    else:
        # Pre-fill doctor choice if passed in URL
        initial_data = {}
        doctor_id = request.GET.get('doctor')
        if doctor_id:
            initial_data['doc_name'] = doctor_id
        form = BookingForm(initial=initial_data)
    
    return render(request, 'booking.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booked_on')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking_instance = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking_instance.delete()
    return redirect('my_bookings')