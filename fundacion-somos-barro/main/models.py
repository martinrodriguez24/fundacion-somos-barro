from django.db import models

class User(models.Model):
    username = models.CharField(
    max_length=100,
    verbose_name='name')

    email = models.EmailField(
    unique=True,
    max_length=100,
    verbose_name='email')
    
    password = models.CharField(
        verbose_name='password',
        max_length=100)

    def __str__(self):
        return self.username

    class Meta():
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class News(models.Model):
    class Categories(models.TextChoices):
        EVENTO = 'EVENTO', 'eventos'
        TALLER = 'TALLER', 'talleres'
        VISITA = 'VISITA', 'visitas'

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='news', null=True)
    category = models.CharField(null=False, default=1, max_length=100, choices=Categories.choices)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        super().delete()
    class Meta():
        ordering = ['title']
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, default=1)
    email = models.EmailField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta():
        ordering = ['-created_on']



