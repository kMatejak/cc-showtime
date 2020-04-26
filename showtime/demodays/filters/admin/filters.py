from datetime import date

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class UpcomingOrPastDemodaysFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('date status')

    # Parameter fot the filter that will be used in the URL query.
    parameter_name = 'planned_date'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is
        the coded value for the option that will appear in the URL query.
        The second element is the human-readable name for the option that
        will appear in the right sidebar.
        """
        return (
            ('up', _('Upcoming')),
            ('ps', _('Past')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value provided in the
        query string and retrivable via `self.value()`.
        """
        if self.value() == 'up':
            return queryset.filter(planned_date__gte=date.today())
        if self.value() == 'ps':
            return queryset.filter(planned_date__lt=date.today())


class HowManyDemosDidTakeFilter(admin.SimpleListFilter):
    title = _('demos did take')
    parameter_name = 'took'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is
        the coded value for the option that will appear in the URL query.
        The second element is the human-readable name for the option that
        will appear in the right sidebar.
        """
        return (
            ('0', _('None')),
            ('1', _('1 (just one)')),
            ('2', _('2 (equally two)')),
            ('3', _('3 or more')),
        )

    def queryset(self, request, queryset):
        students = queryset
        for student in students:
            # take every team related to student
            teams = student.projectteam_set.all()

            # collect all demos related to student's teams
            query_demos = [team.demo_set.all() for team in teams]
            demos = list()
            for d in query_demos:
                for demo in d:
                    demos.append(demo)

            # count only demos which did take place
            counter = 0
            for demo in demos:
                counter += demo.demoday_set.all().filter(
                    did_take_place=True).count()

            # override integer field in student object
            student.took_demos = counter
            student.save()

        if self.value() == '0':
            return queryset.filter(took_demos__exact=0)
        if self.value() == '1':
            return queryset.filter(took_demos__exact=1)
        if self.value() == '2':
            return queryset.filter(took_demos__exact=2)
        if self.value() == '3':
            return queryset.filter(took_demos__gte=3)
