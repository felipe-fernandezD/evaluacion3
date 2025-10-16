from django.db import models

# Create your models here.

class Tareas(models.Model):
    titulo = models.CharField(max_length=200)
    hecho = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.hecho})"
    