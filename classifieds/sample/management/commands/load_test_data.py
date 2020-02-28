from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from sample.models import User, Posting, RidePosting, ItemPosting, Comment
from pytz import UTC

DATETIME_FORMAT = '%m/%d/%Y %H:%M'

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.exists() or Posting.objects.exists() or RidePosting.objects.exists() \
        or ItemPosting.objects.exists() or Comment.objects.exists():
            print('Data already loaded...exiting.')
            return
        print("Proceeding to add data")

        print("Adding user data")
        for row in DictReader(open('./test_user_data_01.csv')):
            user = User()
            user.name = row['Name']
            user.email = row['Email']
            user.role = row['role']
            user.save()