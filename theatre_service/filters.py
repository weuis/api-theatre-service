import django_filters
from theatre_service.models import Performance, Play


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
