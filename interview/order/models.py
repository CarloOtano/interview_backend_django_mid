import pytz
from datetime import datetime

from django.db import models
from django.utils.timezone import make_aware

from interview.core.behaviors import IsActiveModel, TimestampedModel, UniqueNameModel
from interview.inventory.models import Inventory


class OrderTag(UniqueNameModel, TimestampedModel, IsActiveModel, models.Model):
        
    def __str__(self) -> str:
        return self.name
    

class Order(TimestampedModel, IsActiveModel, models.Model):
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    start_date = models.DateField()
    embargo_date = models.DateField()
    tags = models.ManyToManyField(OrderTag, related_name='orders')

    def __str__(self) -> str:
        return f'{self.inventory.name} - {self.start_date}'

    @classmethod
    def get_in_between_dates(cls, startDateStr: str, embargoDateStr: str):
        # Additional date formats can be handled
        startDate = make_aware(
            datetime.strptime(startDateStr, '%Y-%m-%d'),
            timezone=pytz.timezone('US/Eastern'))

        embargoDate = make_aware(
            datetime.strptime(embargoDateStr, '%Y-%m-%d'),
            timezone=pytz.timezone('US/Eastern'))

        return cls.objects.filter(start_date__gte=startDate, embargo_date__lte=embargoDate)
