from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)
    full_description = models.TextField()
    news_type = models.ForeignKey('NewsType', on_delete = models.PROTECT, null = False)

    def __str__(self):
        return self.title

class NewsType(models.Model):
    name = models.CharField(max_length = 20)
    color = models.CharField(max_length = 20)


    def __str__(self):
        return self.name