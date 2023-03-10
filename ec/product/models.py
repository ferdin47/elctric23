from django.db import models

class Product(models.Model):
    sProductNr = models.CharField(max_length=20)
    sProductNm = models.CharField(max_length=100)
    sProductPrice = models.DecimalField(max_digits=5, decimal_places=2)
    sProductDescription = models.CharField(max_length=255)
    sImagePath = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.sProductNm

    class Meta:
      db_table = 'product'