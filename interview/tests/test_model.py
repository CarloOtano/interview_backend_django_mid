from datetime import datetime
import pytz

from django.test import TestCase
from interview.inventory.models import InventoryLanguage, Inventory, InventoryTag, InventoryType


class TestInventory(TestCase):
    # Ideally we would use dump, modify it and created a custom fixture
    # for testing functionality
    def setUp(self):
        en = InventoryLanguage.objects.create(name='English')
        tag = InventoryTag.objects.create(name='Action')
        type = InventoryType.objects.create(name='Movie')
        data = dict(
            created_at=datetime(
                year=2000, month=1,
                day=1,
                tzinfo=pytz.timezone('US/Eastern')
            ),
            name='The Matrix',
            language=en,
            type=type,
            metadata=dict(
                year=1999,
                actors=['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],
                imdb_rating=8.7,
                rotten_tomatoes_rating=87,
            )
        )
        Inventory.objects.create(**data).tags.add(tag)

    def test_filter_empty(self):
        q = Inventory.get_after_created_date('2100-1-1')
        self.assertIs(len(q), 0)

    def test_filter_none(self):
        q = Inventory.get_after_created_date('2000-1-1')
        self.assertIs(len(q), len(Inventory.objects.all()))

    # TODO: Need to add testing for view perse
