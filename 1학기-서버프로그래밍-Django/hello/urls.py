from django.urls import path, include
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDetailView, StudentDeleteView
from . import views
from .views import HacsamViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hacsams', HacsamViewSet)
urlpatterns = [
    #템플릿 CRUD 뷰
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),

    # API 뷰 및 토큰 인증
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),
]