from django.db import models


class PreRegistration(models.Model):
    SPECIALIZATIONS = [
        ('cyber', 'Cybersécurité'),
        ('cloud', 'Cloud Computing'),
        ('ai', 'Intelligence Artificielle'),
        ('devsecops', 'DevSecOps'),
        ('data', 'Data & Analytics'),
        ('grc', 'Gouvernance IT & Risk'),
        ('forensics', 'Digital Forensics'),
        ('soc', 'SOC & Threat Intelligence'),
        ('archi', 'Architecture Cloud'),
        ('dev', 'Développement logiciel'),
        ('pm', 'Gestion de projets'),
        ('entrep', 'Entrepreneuriat tech'),
        ('other', 'Autre'),
    ]

    LEVELS = [
        ('student', 'Étudiant'),
        ('junior', 'Junior (< 3 ans)'),
        ('mid', 'Confirmé (3-7 ans)'),
        ('senior', 'Senior (7+ ans)'),
        ('expert', 'Expert (15+ ans)'),
    ]

    full_name = models.CharField('Nom complet', max_length=100)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Téléphone', max_length=20, blank=True)
    specialization = models.CharField('Spécialité', max_length=20, choices=SPECIALIZATIONS)
    level = models.CharField('Niveau', max_length=20, choices=LEVELS)
    country_of_origin = models.CharField('Pays d\'origine', max_length=50)
    city = models.CharField('Ville en Allemagne', max_length=50)
    wants_mentor = models.BooleanField('Intéressé par le mentorat', default=False)
    wants_newsletter = models.BooleanField('Newsletter', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pré-inscription'
        verbose_name_plural = 'Pré-inscriptions'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} — {self.get_specialization_display()}"
