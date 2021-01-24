from django.db import models


class ScraperModel(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    fun_fact = models.TextField(blank=True)

    class Meta:
        verbose_name = "Radzi Scraper"
