from django.contrib import admin
from django.urls import path
from meals.views import meal_list
from taxi.views import taxi_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', meal_list),
    path('taxi/', taxi_list)
]