from django.contrib import admin
from django.urls import path

from . import views


app_name = 'demodays'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:demoday_id>/', views.detail_demoday, name='detail_demoday'),
]

admin.site.site_header = "CC Showtime"
admin.site.site_title = "CC Showtime"
admin.site.index_title = "CC Showtime Administration"
admin.empty_value_display = '**Empty**'
