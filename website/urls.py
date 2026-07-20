from django.urls import path
from website.views import *

urlpatterns = [
    path('', index_view),
    path('about', about_view),
    path('contacts', contact_view)
]