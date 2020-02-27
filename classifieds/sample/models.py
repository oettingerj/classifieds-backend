from django.db import models

class User(models.Model):
    name = models.CharField('Name', max_length=240)
    email = models.EmailField()
    roleChoice = models.TextChoices('roleChoice', 'STUDENT FACULTY STAFF')
    role = models.CharField(choices=roleChoice.choices, max_length=7)

    def __str__(self):
        return self.name

class Posting(models.Model):
    user = models.ForeignKey(User)
    timePosted = models.DateTimeField()
    category = models.CharField() #change to choices later
    prospective = models.BooleanField()
    fulfilled = models.BooleanField()
    description = models.TextField()
    audienceChoice = models.TextChoices('audienceChoice', 'STUDENT FACULTY STAFF')
    audience = models.CharField(choices=audienceChoice.choices, max_length=7)

class RidePosting(models.Model):
    posting = models.OneToOneField(Posting)
    dateTimeOfRide = models.DateTimeField()
    startLocation = models.TextField()
    endLocation = models.TextField()
    numberOfPeople = models.IntegerField()

class ItemPosting(models.Model):
    posting = models.OneToOneField(Posting)
    images = models.ImageField()
    price = models.DecimalField()
    forSale = models.BooleanField()
    forLoan = models.BooleanField()

class Comment(models.Model):
    posting = models.ForeignKey(Posting)
    user = models.ForeignKey(User)
    timePosted = models.DateTimeField()
    content = models.TextField()