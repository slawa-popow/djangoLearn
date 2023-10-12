from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>', views.categories),
    path('slug/', views.cats_by_slug),
    path("arhive/<year4:year>/", views.arhive),
]