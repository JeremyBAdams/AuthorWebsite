from datetime import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Feature(models.Model):
    feature_id = models.AutoField(
        primary_key=True
    )

    is_article = models.BooleanField()
    is_blog = models.BooleanField()
    is_news = models.BooleanField()

    foreign_reference_number = models.CharField(
        validators=[MinLengthValidator(6)],
        max_length=6,
    )

    pub_date = models.DateTimeField(
        'date published',
        default=datetime.now
    )

    internal_description = models.CharField(
        max_length=100,
        default="no description"
    )

    def __str__(self):
        return "Feature instance: " + str(self.feature_id) + " - " + str(self.internal_description)
