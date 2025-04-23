from django.contrib import admin
from .models import Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "description")
    filter_horizontal = ("genres", "actors")


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rows", "seats_in_row")
    search_fields = ("name",)
    list_filter = ("rows",)


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("id", "play", "theatre_hall", "show_time")
    list_filter = ("theatre_hall", "show_time")
    search_fields = ("play__title",)
    autocomplete_fields = ("play", "theatre_hall")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username",)
    date_hierarchy = "created_at"


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "performance", "reservation", "row", "seat")
    list_filter = ("performance", "row")
    search_fields = ("reservation__user__username",)
    autocomplete_fields = ("performance", "reservation")
