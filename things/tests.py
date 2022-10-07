from django.test import TestCase
from things.models import Thing
from django.core.exceptions import ValidationError

class ThingModelTestCase(TestCase):
    def setUp(self):
        self.thing1 = Thing.objects.create(
            name="thing1",
            description="description1",
            quantity=1
        )
        self.thing2 = Thing.objects.create(
            name="thing2",
            description="description2",
            quantity=2
        )
    
    def _assert_thing_is_valid(self):
        try:
            self.thing1.full_clean()
        except (ValidationError):
            self.fail("Test thing should be valid.")
    
    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing1.full_clean()
    
    def test_valid_thing(self):
        self._assert_thing_is_valid()
    
    # Name test cases.
    def test_name_must_be_unique(self):
        self.thing1.name = self.thing2.name
        self._assert_thing_is_invalid()

    def test_name_must_not_be_blank(self):
        self.thing1.name = ''
        self._assert_thing_is_invalid()

    def test_name_may_be_30_characters(self):
        self.thing1.name = 'x' * 30
        self._assert_thing_is_valid()

    def test_name_must_not_be_over_30_characters(self):
        self.thing1.name = 'x' *31
        self._assert_thing_is_invalid()
    
    # Description test cases.
    def test_description_may_already_exist(self):
        self.thing1.description = self.thing2.description
        self._assert_thing_is_valid()

    def test_name_may_be_blank(self):
        self.thing1.description = ''
        self._assert_thing_is_valid()

    def test_name_may_be_120_characters(self):
        self.thing1.description = 'x' * 120
        self._assert_thing_is_valid()

    def test_name_must_not_be_over_120_characters(self):
        self.thing1.description = 'x' * 121
        self._assert_thing_is_invalid()
    
    # Quantity test cases.
    def test_quantity_may_already_exist(self):
        self.thing1.quantity = self.thing2.quantity
        self._assert_thing_is_valid()
    
    def test_quantity_may_be_0(self):
        self.thing1.quantity = 0
        self._assert_thing_is_valid()
    
    def test_quantity_may_be_100(self):
        self.thing1.quantity = 100
        self._assert_thing_is_valid()
    
    def test_quantity_must_not_be_under_0(self):
        self.thing1.quantity = -1
        self._assert_thing_is_invalid()
    
    def test_quantity_must_not_be_over_100(self):
        self.thing1.quantity = 101
        self._assert_thing_is_invalid()
