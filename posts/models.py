from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class TagDict(models.Model):
    tag = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.tag
 

class Post(models.Model):
    CATEGORY_CHOICES = ( 
        ("1", "Programming/Technology"), 
        ("2", "Health/Fitness"), 
        ("3", "Personal"), 
        ("4", "Fashion"), 
        ("5", "Food"), 
        ("6", "Travel"), 
        ("7", "Business"), 
        ("8", "Art"),
        ("9", "Other"), 
    ) 
    
    category = models.CharField( 
        max_length = 20, 
        choices = CATEGORY_CHOICES, 
        default = '1'
        ) 
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, editable=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    read_count = models.IntegerField(default=0, editable=False)
    read_time = models.IntegerField(default=0, editable=False)
    # likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    featured_image = models.ImageField(null=True, blank=True, upload_to='posts/featured-images/')
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

        for tag in self.tags.all():
            tag_dict,_ = TagDict.objects.get_or_create(tag=str(tag))
            tag_dict.count += 1
            tag_dict.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug":self.slug})

    def get_like_url(self):
        return reverse('like-toggle', kwargs={"slug":self.slug})
    
    def get_api_like_url(self):
        return reverse('like-api-toggle', kwargs={"slug":self.slug})
