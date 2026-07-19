from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from resources.models import Article


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.filter(published=True)[:3]
        context['domains'] = [
            {'emoji': '🛡️', 'name': 'Cybersécurité'},
            {'emoji': '☁️', 'name': 'Cloud Computing'},
            {'emoji': '🤖', 'name': 'Intelligence Artificielle'},
            {'emoji': '🔧', 'name': 'DevSecOps'},
            {'emoji': '📊', 'name': 'Data & Analytics'},
            {'emoji': '🏛️', 'name': 'Gouvernance IT'},
            {'emoji': '⚠️', 'name': 'Risk & Compliance'},
            {'emoji': '🔍', 'name': 'SOC & Threat Intelligence'},
            {'emoji': '🕵️', 'name': 'Digital Forensics'},
            {'emoji': '🏗️', 'name': 'Architecture Cloud'},
            {'emoji': '💻', 'name': 'Développement logiciel'},
            {'emoji': '📋', 'name': 'Gestion de projets'},
            {'emoji': '🚀', 'name': 'Entrepreneuriat tech'},
        ]
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['values'] = [
            {'emoji': '🎯', 'name': 'Excellence'},
            {'emoji': '💡', 'name': 'Innovation'},
            {'emoji': '🤝', 'name': 'Collaboration'},
            {'emoji': '🌍', 'name': 'Diversité'},
            {'emoji': '❤️', 'name': 'Inclusion'},
            {'emoji': '📤', 'name': 'Partage'},
            {'emoji': '🔒', 'name': 'Intégrité'},
            {'emoji': '⚡', 'name': 'Impact'},
        ]
        context['roadmap'] = [
            {'year': '2026', 'title': 'Structurer la communauté', 'desc': 'Développer le réseau et lancer le site institutionnel.'},
            {'year': '2027', 'title': 'Plateforme numérique', 'desc': 'Lancer la plateforme interactive AfroSec.'},
            {'year': '2028', 'title': 'AfroSec Academy', 'desc': 'Déployer les premiers programmes de formation certifiants.'},
            {'year': '2029', 'title': 'AfroSec Labs', 'desc': 'Soutenir les projets collaboratifs et l\'innovation.'},
            {'year': '2030', 'title': 'Hub de référence', 'desc': 'Devenir le Hub technologique de référence de la communauté africaine en Allemagne.'},
        ]
        return context


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Merci ! Votre message a été envoyé.")
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'core/contact_success.html'
