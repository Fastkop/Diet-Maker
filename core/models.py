from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    diet = models.ForeignKey('Diet', on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='Profile-Photos', default=None)

    def __str__(self):
        return self.user.username


class Diet(models.Model):
    name = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='Diet-photos')
    description = models.CharField(max_length=40, blank=True)


    @property
    def meals(self):
        return self.meal_set

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=20, blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default=None)
    TYPE = (
        ('b', 'Breakfast'),
        ('l', 'Lunch'),
        ('d', 'Dinner'),
        ('s', 'Snack'),
    )
    type = models.CharField(max_length=8, choices=TYPE)
    foods = models.ManyToManyField('Food')
    photo = models.ImageField(upload_to='Meal-photos', default=None)

    def __str__(self):
        return self.name

    @property
    def total_calories(self):
        total = 0
        for food in self.foods.all():
            total += food.calories
        return total

    @property
    def total_carbs(self):
        total = 0
        for food in self.foods.all():
            total += food.carbs
        return total

    @property
    def total_protein(self):
        total = 0
        for food in self.foods.all():
            total += food.protein
        return total


class FoodType(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20, blank=True)
    diet = models.ManyToManyField('Diet')
    calories = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    note = models.CharField(max_length=40, blank=True)
    photo = models.ImageField(upload_to='Food-photos')
    type = models.ManyToManyField('FoodType')

    def __str__(self):
        return self.name
