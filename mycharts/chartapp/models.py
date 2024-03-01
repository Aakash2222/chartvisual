from django.db import models

# Create your models here.
class Product(models.Model):
    category        = models.CharField(default="",max_length=100, null=False,unique=True, blank=False)
    num_of_products = models.IntegerField(null=True,blank=True)
    end_year        = models.CharField(max_length=100, null=True, blank=True)
    intensity       = models.IntegerField(null=True, blank=True)
    sector          = models.CharField(max_length=100, null=True, blank=True)
    topic           = models.CharField(max_length=100, null=True, blank=True)
    insight         = models.IntegerField(blank=True, null=True)
    url             = models.URLField(max_length=100, null=True, blank=True)
    region          = models.CharField(max_length=100, null=True, blank=True)
    start_year      = models.CharField(max_length=100, null=True, blank=True)
    impact          = models.IntegerField(null=True, blank=True)
    added           = models.DateTimeField(null=True, blank=True)
    published       = models.DateTimeField(null=True, blank=True)
    country         = models.CharField(max_length=100, null=True, blank=True)
    relevance       = models.IntegerField(null=True, blank=True)
    pestle          = models.CharField(max_length=100, null=True, blank=True)
    source          = models.CharField(max_length=100, null=True, blank=True)
    title           = models.CharField(max_length=100, null=True, blank=True)
    likelihood      = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.product_name
    
    def __str__(self):
        return f'{self.category} - {self.num_of_products}'
    
    