from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Reservation
from .forms import ReservationForm
from .forms import UserCreationForm

# Create a reservation
@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Add the logged-in user to the reservation
            reservation = form.save(commit=False)
            reservation.user = request.user  # Associate the logged-in user
            reservation.save()  # Save the reservation to the database
            return redirect('list_reservations')
    else:
        form = ReservationForm()
    messages.info(request, "Successfully created reservation!")
    return render(request, 'bookings/create_reservation.html', {'form': form})

# List all reservations
def list_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'bookings/list_reservations.html', 
                  {'reservations': reservations})

# Update a reservation
@login_required
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    # Allow only the owner or an admin
    if request.user != reservation.user and not request.user.is_superuser:
        messages.error(request, 
                       "You do not have permission to edit this reservation.")
        return redirect("list_reservations")  
        # Redirect to the reservations list

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm(instance=reservation)
    messages.info(request, "Successfully updated reservation!")
    return render(request, 'bookings/update_reservation.html', {'form': form})

# Delete a reservation
@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    # Allow only the owner or an admin
    if request.user != reservation.user and not request.user.is_superuser:
        messages.error(request, 
                       "You do not have permission to edit this reservation.")
        return redirect("list_reservations")  
        # Redirect to the reservations list

    reservation.delete()
    messages.info(request, "Successfully deleted reservation!")
    return redirect('list_reservations')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            # Log the user in automatically
            login(request, user)
            return redirect('list_reservations')  
            # Redirect to the list reservations page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})