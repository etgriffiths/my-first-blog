from django.conf import settings
from django.db import models
from django.utils import timezone

#this line defines our model (it is an object).
#Post is the name of our model. We can give it a different name
#(but we must avoid special characters and whitespace).
#Always start a class name with an uppercase letter.
class Post(models.Model):
    #To create a recursive relationship – an object that has a many-to-one relationship with itself
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
         return self.title
