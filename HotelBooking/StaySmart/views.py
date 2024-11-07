from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm, UserProfileForm
from django.shortcuts import render
from .models import Hotel  # Assuming Hotel model exists for listing


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'StaySmart/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'StaySmart/profile.html', {'profile_form': profile_form})


def search(request):
    hotels = Hotel.objects.all()
    location = request.GET.get('location')
    if location:
        hotels = hotels.filter(location__icontains=location)
    return render(request, 'StaySmart/search.html', {'hotels': hotels})
