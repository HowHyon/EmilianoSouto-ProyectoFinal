from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import User
from django.shortcuts import render, redirect

from users.forms import RegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages



class UserRegistration(FormView):
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        form.save()
        return super(UserRegistration, self).form_valid(form)
    
@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El perfil se actualizó con éxito!')
            return redirect('users:ver_perfil')  # Cambia 'ver_perfil' por la URL de visualización del perfil
    else:
        form = UserProfileForm(instance=usuario)

    return render(request, 'editar_perfil.html', {'form': form})



def ver_perfil(request):
    usuario = request.user
    return render(request, 'ver_perfil.html', {'usuario': usuario})
    
