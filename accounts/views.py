from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from core.forms import PreRegistrationForm


class PreRegisterView(FormView):
    template_name = 'accounts/preregister.html'
    form_class = PreRegistrationForm
    success_url = reverse_lazy('preregister_success')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Inscription réussie ! Bienvenue dans la communauté AfroSec.")
        return super().form_valid(form)


class PreRegisterSuccessView(TemplateView):
    template_name = 'accounts/preregister_success.html'
