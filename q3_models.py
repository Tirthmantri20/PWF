from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title