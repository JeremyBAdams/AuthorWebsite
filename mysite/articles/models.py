import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Pseudonym(models.Model):
    """class for pseudo-authors/writers of articles"""

    #all articles must be written by a pseudo author (via foreignkey constraint)
    pseudonym_id = models.AutoField(
        primary_key = True
    )
    pseudonym = models.CharField(
        unique = True,
        max_length=250,
    )

    def __str__(self):
        """docstring"""
        return "Pseudonym instance - " + self.pseudonym \
               + ", id: " + str(self.pseudonym_id)

class Series(models.Model):
    """class for the serialization group that an article falls under"""

    #all articles fall into a series (eg. Astran History, or Character Bios)
    #articles will be forced into a series via foreignkey constraint)
    series_id = models.AutoField(
        primary_key = True
    )
    series_name = models.CharField(
        unique=True,
        max_length=250
    )

    def __str__(self):
        """docstring"""
        return "Series instance - " + self.series_name \
               + ", id: " + str(self.series_id)

class Palette(models.Model):
    """class for webpage color palette based on the novel's concept of soul archetypes"""

    #all articles will be colored according to one of the six soul archetypes
    #the best soul archetype that covers the article's content will be used

    #color palette archetype name
    palette_id = models.AutoField(
        primary_key = True
    )
    archetype_name = models.CharField(
        unique=True,
        max_length=20
    )

    def __str__(self):
        """docstring"""
        return "Palette instance - " + self.archetype_name \
               + ", id: " + str(self.palette_id)

class Article(models.Model):
    """class for story-based articles"""

    "attributes"
    article_id = models.AutoField(
        primary_key = True
    )
    #title: article title
    title = models.CharField(
        max_length=500,
        unique=True
    )

    url_string = models.CharField(
        max_length=500,
        unique=True
    )

    #reference_number: a 6-digit reference id number
    #ie '123456', to be used for file pathing
    #html pages and images will be named based on reference id number
    reference_number = models.CharField(
        validators=[MinLengthValidator(6)],
        max_length=6,
        unique=True
    )
    #pub_date: the local time that the article was published
    pub_date = models.DateTimeField(
        'date published'
    )
    #pseudonym: the fictional author who wrote the article, from Pseudonym class
    pseudonym = models.ForeignKey(
        Pseudonym,
        on_delete=models.CASCADE
    )
    #series: the serialization that the article falls under
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE
    )
    #palette: the soul archetype palette for the article
    palette = models.ForeignKey(
        Palette,
        on_delete=models.CASCADE
    )

    #CLASS METHODS
    def __str__(self):
        """display Article object instance attributes"""
        return  "Article:: title:" + self.title \
                + " reference_number:" +self.reference_number
