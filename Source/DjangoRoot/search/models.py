from django.db import models

class Search(models.Model):
    search = models.CharField(max_length=255, blank=False, null=False)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Search'
        verbose_name_plural = 'Searches'
