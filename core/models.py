from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Venda(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    status = models.CharField(max_length=20, default='em processo')
    def __str__(self):
        return str(self.code) + "----" + str(self.owner) 

class Item(models.Model):
    nome_items= models.CharField(max_length=30)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nome_items)
    
