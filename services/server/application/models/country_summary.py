"""Country Summary model."""

from datetime import datetime

from mongoengine import Document, StringField, IntField, DateTimeField


class CountrySummary(Document):
    """Country Summary representation."""

    created_at = DateTimeField()
    country = StringField(required=True, null=False)
    country_code = StringField(required=True, null=False)
    new_confirmed = IntField(min_value=0, required=True, null=False)
    total_confirmed = IntField(min_value=0, required=True, null=False)
    new_deaths = IntField(min_value=0, required=True, null=False)
    total_deaths = IntField(min_value=0, required=True, null=False)
    new_recovered = IntField(min_value=0, required=True, null=False)
    total_recovered = IntField(min_value=0, required=True, null=False)
    last_update = DateTimeField()

    def clean(self):
        """Set last_update information before saving it to Mongo."""
        self.last_update = datetime.now()
