import django_filters
from theatre_service.models import Performance, Play, Reservation


class PerformanceFilter(django_filters.FilterSet):
    show_time = django_filters.DateFromToRangeFilter()
    play = django_filters.ModelChoiceFilter(queryset=Play.objects.all())
    theatre_hall = django_filters.CharFilter(field_name="theatre_hall__name", lookup_expr="icontains")

    class Meta:
        model = Performance
        fields = ["show_time", "play", "theatre_hall"]


class PlayFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name="genres__name", lookup_expr="icontains")

    class Meta:
        model = Play
        fields = ["genre"]


class ReservationFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(field_name="user__id")
    created_at__gte = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_at__lte = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")
    has_tickets = django_filters.BooleanFilter(method="filter_has_tickets")

    class Meta:
        model = Reservation
        fields = ["user", "created_at__gte", "created_at__lte"]

    def filter_has_tickets(self, queryset, value):
        return queryset.exclude(tickets=None) if value else queryset.filter(tickets=None)
