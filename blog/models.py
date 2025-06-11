from django.db import models

class Autors(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField()
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nom} ({self.cognom})"


    
class Tag(models.Model):
    caption = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.caption

class Post(models.Model):
    titol = models.CharField(max_length=100)
    descripcio = models.TextField()
    contingut = models.TextField()
    imatge = models.ImageField()
    data = models.DateField(null=True)
    autor = models.ForeignKey(Autors, on_delete=models.CASCADE, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.titol
