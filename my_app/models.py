from django.db import models

# Create your models here.
class Wishlist(models.Model):
    added_date = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=2000)
    item_name = models.CharField(max_length=250)
    expected_price = models.FloatField()

    def __str__ (self):
        return '{}'.format(self.item_name)       

    class Meta:
        verbose_name_plural = 'Wishlists'