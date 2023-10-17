from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
class RegisterView(CreateView):
    form_class = UserRegisterForm
    #success_url = reverse_lazy('login')
    template_name = 'registration/register.html' #<----في هذا السطر
    """def get_succes_url(self):
        login(self.request, self.object)
        return reverse_lazy('Project_list')"""
    def get_success_url(self):
       login(self.request, self.object)
       return reverse_lazy('Project_List')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = ProfileForm(instance=request.user)
    return render(request, 'profile.html',{
        'form': form
    })
