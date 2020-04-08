from django.urls import path

from . import views


app_name = 'demodays'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:demoday_id>/', views.detail_demoday, name='detail_demoday'),
]
