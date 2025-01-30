from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reservation
from .forms import ReservationForm

# Create a reservation
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm()
    return render(request, 'bookings/create_reservation.html', {'form': form})

# List all reservations
def list_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'bookings/list_reservations.html', {'reservations': reservations})

# Update a reservation
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'bookings/update_reservation.html', {'form': form})

# Delete a reservation
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('list_reservations')
