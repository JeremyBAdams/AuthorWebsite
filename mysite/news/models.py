from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class NewsArticle(models.Model):
    """class for Articles/Stories for news and current events"""
    news_article_id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=500,
        unique=True
    )
    description = models.CharField(
        max_length=500,
        default="no description"
    )
    url_string = models.CharField(
        max_length=500,
        unique=True
    )
    reference_number = models.CharField(
        validators=[MinLengthValidator(6)],
        max_length=6,
        unique=True
    )
    pub_date = models.DateTimeField(
        'date_published'
    )


class Event(models.Model):
    """class for an upcoming event with a specific data/time that can be
    viewed on the calendar
    """
    event_id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=500,
        unique=True
    )
    description = models.CharField(
        max_length=500,
        default="no description"
    )
    location = models.CharField(
        max_length=500
    )
    event_date = models.DateTimeField(
        'date_and_time_of_event'
    )
