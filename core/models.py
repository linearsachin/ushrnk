from django.db import models
import os
import string, random
# debug = __import__(os.environ.get('DJANGO_SETTINGS_MODULE'))
class ShrnkUrl(models.Model):
    og_url = models.URLField()
    shrnk_url_slug = models.CharField(max_length=10,unique=True)
    xcode =models.CharField(max_length=5,unique=True,blank=True, null=True)
    total_clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.shrnk_url_slug
    def get_shrnk_url(self):
        # if debug.development.DEBUG:
        #     return f"http://127.0.0.1:8000/u/{self.shrnk_url_slug}"
        # else:
        return f"https://ushrnk.herokuapp.com/u/{self.shrnk_url_slug}"
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ShrnkUrls'
        verbose_name_plural = 'ShrnkUrls'

class Click(models.Model):
    shrnk_url = models.ForeignKey(ShrnkUrl,on_delete=models.CASCADE)
    date = models.DateField()
    clicks = models.IntegerField()
    def __str__(self):
        return self.shrnk_url.shrnk_url_slug 
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Click'
        verbose_name_plural = 'Clicks'