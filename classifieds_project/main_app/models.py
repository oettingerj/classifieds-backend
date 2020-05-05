from django.db import models


class User(models.Model):
    username = models.CharField(max_length=240)
    password = models.CharField(max_length=240)

    email = models.EmailField(unique=True)
    roleChoice = models.TextChoices('roleChoice', 'STUDENT FACULTY STAFF ALL')
    role = models.CharField(choices=roleChoice.choices, max_length=7)
    dummy_field = models.CharField(max_length=240, default='dummy')


    def __str__(self):
        return self.name


class Posting(models.Model):
    user = models.ForeignKey(User, related_name='poster', on_delete=models.CASCADE)
    timePosted = models.DateTimeField()
    category = models.CharField(max_length=240)  # change to choices later
    prospective = models.BooleanField()
    fulfilled = models.BooleanField()
    title = models.TextField(default="N/A")
    description = models.TextField()
    audienceChoice = models.TextChoices('audienceChoice', 'STUDENT FACULTY STAFF ALL')
    audience = models.CharField(choices=audienceChoice.choices, max_length=7)
    savedBy = models.ManyToManyField(User, related_name='savedPostings')
#title?

class RidePosting(models.Model):
    posting = models.OneToOneField(Posting, on_delete=models.CASCADE)
    dateTimeOfRide = models.DateTimeField()
    startLocation = models.TextField()
    endLocation = models.TextField()
    numberOfPeople = models.IntegerField()
    willingToPay = models.BooleanField()
    payment = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')


class ItemPosting(models.Model):
    posting = models.OneToOneField(Posting, on_delete=models.CASCADE)
    images = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    forSale = models.BooleanField()
    forLoan = models.BooleanField()



