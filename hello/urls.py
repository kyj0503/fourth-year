from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDetailView, StudentDeleteView
from . import views
urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
    path('api/', views.ApiStudent_list),
    path('api/<int:Hacsam_id>/', views.ApiStudent_detail),
]