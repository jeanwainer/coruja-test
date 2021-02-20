from django.db import models


class Customer(models.Model):
    """
    Customer list based on customers.csv. Max_length of each column was rounded up after the max length of each entry.
    """

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other / Rather not say'),
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    company = models.CharField(max_length=15)
    city = models.CharField(max_length=25)
    title = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} - {self.title} at {self.company}"
