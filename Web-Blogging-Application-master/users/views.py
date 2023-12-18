from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # request.POST contains the data enterd by user into the form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # request.cleaned_data is a dictionary made of all entries made by the user
            message = messages.success(request, 'You have successfully created an account.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST': # To display dtaa in the form beforehand
        u_form = UserUpdateForm(request.POST, instance=request.user) # instance still required to let the form know which model to update
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # request.POST=data, request.FILES=files like images 
        if u_form.is_valid() and p_form.is_valid(): # to save the updated data
            u_form.save()
            p_form.save()
            message = messages.success(request, 'Profile updated successfully.')
            return redirect('profile') # redirect necessary. When reloading after submitting, the browser sends another 
                                       # POST request. Redirecting will send a normal GET request and then no weird messages pop up.
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
                'u_form' : u_form,
                'p_form' : p_form
                }
    return render(request, 'users/profile.html', context)



