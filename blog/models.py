from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"





class tag(models.Model):
    captions = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.captions}"


class post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    images = models.ImageField(upload_to="blog/static/images")
    slug = models.SlugField(default="",null=False,db_index=True,blank=True)
    content = models.TextField()
    author_post = models.ForeignKey(Author,null=True,on_delete=models.CASCADE)
    tag = models.ManyToManyField(tag)
   
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'post-descriptions'

    def save(self, *args ,**kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("full-post",args=[self.slug])
