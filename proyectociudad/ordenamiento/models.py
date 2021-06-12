from django.db import models

# Create your models here.
class Parroquia (models.Model):
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Las Parroquias'

    opciones_parroquia = (
        ('Urbana', 'Urbana'),
        ('Rural', 'Rural'),
    )

    nombre = models.CharField('Nombre de la parroquia', max_length=150)
    tipo = models.CharField(choices = opciones_parroquia, max_length=8)

    def __str__(self):
        return "%s" % (self.nombre)

class Barrio (models.Model):

    class Meta:
        ordering = ['nombre']
        verbose_name_plural  = 'Los Barrios'
    opciones_parque= (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )
    nombre = models.CharField('Nombre del Barrio', max_length=150)
    num_viviendas = models.IntegerField("Número de Viviendas")
    num_parques = models.IntegerField('Número de Parques', choices=opciones_parque)
    num_edificios = models.IntegerField("Número de Edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias',
            on_delete = models.CASCADE)

    def __str__(self):
        return '%s | %s | %s | %s | %s' %(self.nombre, self.num_viviendas,
                self.num_parques, self.num_edificios, self.parroquia.nombre)
