from django.urls import path
from . import views



urlpatterns = [
    path('trans_search/', views.page_list, name='page_list'),
]