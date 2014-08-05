from django.db import models
from django.contrib import admin

# Create your models here.

LENGUAJES = (
	('python','Python'),
	('perl','Perl'),
	('java','Java'),
	('ruby','Ruby'),
	('bash','Bash Script')
)

class Code(models.Model):
  nombre = models.CharField(max_length=50)
  pub_date = models.DateTimeField('fecha de publicacion')
  lenguaje = models.CharField(max_length=1, choices=LENGUAJES)
  autor = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=50)
  codigo = models.TextField(max_length=1000)
  
  def __unicode__(self):
	return self.nombre

