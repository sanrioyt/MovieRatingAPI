from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    """ Model that handles Movie object"""
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        """ returns the number of ratings for a movie"""
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_ratings(self):
        """ Returns average rating for a movie """
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

    def __str__(self):
        """ Returns a string representation of Movie Object"""
        return self.title


class Rating(models.Model):
    """ Model that handles Rating object """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])

    def __str__(self):
        """Returns a string representation of the rating object"""
        return f"{self.movie} {self.user} {self.stars}"

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
