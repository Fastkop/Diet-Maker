from django.contrib import admin
from .models import Profile, Meal, Diet, Food

# Register your models here.
admin.site.register(Profile)
admin.site.register(Meal)
admin.site.register(Diet)
admin.site.register(Food)
