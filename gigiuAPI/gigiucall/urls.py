from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gigiucall import views

app_name = 'gigiucall'

urlpatterns = [
  path('', views.CallRegisterList.as_view()),
  # path('index/', views.CallRegisterList.as_view()),
  # path('<int:pk>/', views.CallRegisterDetail.as_view()),
  # path('edit/<int:pk>/', views.CallRegisterDetail.as_view()),
  # path('delete/<int:pk>/', views.CallRegisterDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
