from django.db import models

class list_of_words(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word +'/'+self.translation
