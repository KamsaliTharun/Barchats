from django.db import models

# Create your models here.


# class DashboardData(models.Model):
#     intensity = models.IntegerField()
#     likelihood = models.IntegerField()
#     relevance = models.IntegerField()
#     year = models.IntegerField()
#     country = models.CharField(max_length=100)
#     topics = models.CharField(max_length=100)
#     region = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
    
#     def __str__(self):
#         return f"{self.year} - {self.country} - {self.topics}"


class Visual_dash(models.Model):
    topic = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    intensity = models.CharField(max_length = 100)
    sector = models.CharField(max_length = 100)
    url = models.URLField()
    insight = models.CharField(max_length = 100)
    # end_Year = models.CharField(max_length = 100, default = "")
    region = models.CharField(max_length = 100)
    # start_Year = models.CharField(max_length = 100, default = "")
    impact = models.CharField(max_length = 100, default = "")
    added = models.CharField(max_length = 100, default = "")
    published = models.CharField(max_length = 100, default = "")
    country = models.CharField(max_length = 100)
    relevance = models.CharField(max_length = 100)
    pestle = models.CharField(max_length = 100)
    source = models.CharField(max_length = 100)
    likelihood = models.CharField(max_length = 100, null = True)

    def __str__(self) -> str:
        return str(self.title)