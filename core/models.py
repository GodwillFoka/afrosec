from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# ===== CONTACT =====
class ContactMessage(models.Model):
    name = models.CharField('Nom', max_length=100)
    email = models.EmailField('Email')
    subject = models.CharField('Sujet', max_length=200)
    message = models.TextField('Message')
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField('Lu', default=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"
