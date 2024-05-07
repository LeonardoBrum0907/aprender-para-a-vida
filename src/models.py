from django.db import models

class User(models.Model):
      nome = models.CharField(max_length=255, null=False)
      email = models.CharField(max_length=255, null=False)
      telefone = models.CharField(max_length=255, null=False)

      def __str__(self):
            return self.nome


# Create your models here.
