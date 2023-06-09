from django.db import models

# Create your models here.

class Product_category(models.Model):
    PCID=models.IntegerField()
    PCname=models.CharField(max_length=100)

    def __str__(self):
        return self.PCname

class Product(models.Model):
    PCname=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    PID=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdate=models.DateField()

    def __str__(self):
        return self.Pname


