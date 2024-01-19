from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('create/', create, name='create'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('work/<slug:work_slug>/', work, name='work'),
    path('work_create/', work_create, name='work_create'),
    path('profile/', profile_view, name='profile'),
]