from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='Img/', verbose_name= "Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripcion", null=True)


    def __str__(self):
        fila = "Titulo: " + self.titulo + " Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete()
        super().delete(using=using, keep_parents=keep_parents)
        


