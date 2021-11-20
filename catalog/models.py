import uuid  # Required for unique instances

from django.db import models
from django.urls.base import reverse

class Pilot(models.Model):
    """Model representing a Pilot."""
    name = models.CharField(max_length=50, help_text='Enter the name of the pilot')
    firstrace = models.DateField(help_text='Enter the date of the first race')
    description = models.TextField(help_text='Enter a description')

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the Pilot model."""
        return reverse('pilot-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class CarImage(models.Model):
    """Model representing a car image."""
    path = models.CharField(max_length=50, help_text='Enter image path')
    description = models.TextField(help_text='Enter a description')
    car = models.ForeignKey('Car', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.path
    
class Car(models.Model):
    """Model representing a car."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this car')
    pilot = models.ForeignKey('Pilot', on_delete=models.RESTRICT, null=True)
    order = models.IntegerField(null=False)
    name = models.CharField(max_length=50, help_text='Enter the name of the car')
    caryear = models.DateField(help_text='Enter the car date')
    maxspeed = models.IntegerField(null=True, help_text='Max Speed')
    hp = models.IntegerField(null=True, help_text='Horse Power')
    cylinders = models.IntegerField(null=True, help_text='Number of cylinders')
    description = models.TextField(null=True, help_text='Enter a description')

    COLOR = (
        ('yl', 'Yellow'),
        ('bk', 'Black'),
        ('bl', 'Blue'),
        ('rd', 'Red'),
    )

    color = models.CharField(
        max_length=2,
        choices=COLOR,
        blank=True,
        default='rd',
        help_text='Car color',
    )

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the Car model."""
        return reverse('car-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.name})'