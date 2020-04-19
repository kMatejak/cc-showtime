from django.contrib import admin

from .models import demos, users, companies, techs


admin.site.register(demos.Demo)
admin.site.register(demos.Demoday)
admin.site.register(users.ProjectTeam)
admin.site.register(users.Student)
admin.site.register(companies.Company)
admin.site.register(companies.Representative)
admin.site.register(techs.Tech)
