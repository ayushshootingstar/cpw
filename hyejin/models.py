from django.db import models

# Create your models here.

    
class Upload(models.Model):

    caption=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to='image/', default="")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f"{self.caption}" 



    

   
