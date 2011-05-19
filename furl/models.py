from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Furl(models.Model):
    owner = models.ForeignKey(User)
    url  = models.URLField(max_length=200)
    description  = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    html = models.TextField(blank=True)
    date_added   = models.DateField(auto_now_add=True)
    
    def get_tag_names(self):
        return " ".join([x.name for x in self.tag_set.all()])
    
    def __unicode__(self):
        return self.title
    

class Tag(models.Model):
    owner = models.ForeignKey(User, default=1)
    name  = models.CharField(max_length=100)
    furls  = models.ManyToManyField(Furl)    
    def furl_count(self):
        return self.furls.count()
