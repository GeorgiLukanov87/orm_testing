from django.db import models


class Car(models.Model):
    model = models.CharField(
        max_length=40,
    )

    year = models.PositiveIntegerField()

    color = models.CharField(
        max_length=40,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    price_with_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )


class Task(models.Model):
    title = models.CharField(
        max_length=25,
    )

    description = models.TextField()

    due_date = models.DateField()

    is_finished = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"Task - {self.title} needs to be done until {self.due_date}!"


class HotelRoom(models.Model):
    ROOM_TYPES = [
        ("st", "Standard"),
        ("dlx", "Deluxe"),
        ("suite", "Suite"),
    ]
    room_number = models.PositiveIntegerField()

    room_type = models.CharField(
        choices=ROOM_TYPES,
    )

    capacity = models.PositiveIntegerField()

    amenities = models.TextField()

    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    is_reserved = models.BooleanField(
        default=False
    )
