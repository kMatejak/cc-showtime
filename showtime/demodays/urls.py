from django.contrib import admin
from django.urls import path


app_name = 'demodays'
urlpatterns = [
    path('', admin.site.urls, name='admin'),
]

admin.site.site_header = "CC Showtime"
admin.site.site_title = "CC Showtime"
admin.site.index_title = "CC Showtime Administration"
admin.empty_value_display = '**Empty**'
