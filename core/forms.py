from django import forms
from .models import ContactMessage
from accounts.models import PreRegistration


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'votre@email.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet de votre message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message...', 'rows': 6}),
        }
        labels = {
            'name': 'Nom complet',
            'email': 'Adresse email',
            'subject': 'Sujet',
            'message': 'Message',
        }


class PreRegistrationForm(forms.ModelForm):
    class Meta:
        model = PreRegistration
        exclude = ['created_at']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex. : Jean Dupont'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'jean@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+49 176 12345678'}),
            'specialization': forms.Select(attrs={'class': 'form-select'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex. : Cameroun'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex. : Berlin'}),
            'wants_mentor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'wants_newsletter': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'full_name': 'Nom complet',
            'email': 'Adresse email',
            'phone': 'Téléphone (optionnel)',
            'specialization': 'Domaine de spécialité',
            'level': 'Niveau d\'expérience',
            'country_of_origin': 'Pays d\'origine',
            'city': 'Ville en Allemagne',
            'wants_mentor': 'Je suis intéressé(e) par le mentorat',
            'wants_newsletter': 'Je souhaite recevoir la newsletter',
        }
