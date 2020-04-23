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
        # Compare the requested value (either 'up' or 'ps')
        # to decide how to filter the queryset.
        if self.value() == 'up':
            return queryset.filter(planned_date__gte=date.today())
        if self.value() == 'ps':
            return queryset.filter(planned_date__lt=date.today())


# TODO
class HowManyDemosDidTakeFilter(admin.SimpleListFilter):
    title = _('demos did take')
    parameter_name = 'took'

    def lookups(self, request, model_admin):
        pass

    def queryset(self, request, queryset):
        pass
