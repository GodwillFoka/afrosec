from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField('Nom', max_length=100)
    slug = models.SlugField('Slug', unique=True, blank=True)

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('Titre', max_length=200)
    slug = models.SlugField('Slug', unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Catégorie')
    excerpt = models.TextField('Résumé', max_length=300, help_text='Court résumé affiché dans les listes')
    content = RichTextField('Contenu')
    author_name = models.CharField('Auteur', max_length=100, default='AfroSec')
    image = models.ImageField('Image à la une', upload_to='blog/', blank=True, null=True)
    published = models.BooleanField('Publié', default=False)
    created_at = models.DateTimeField('Date de création', auto_now_add=True)
    updated_at = models.DateTimeField('Mis à jour', auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
