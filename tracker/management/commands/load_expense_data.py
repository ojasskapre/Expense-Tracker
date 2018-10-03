from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from tracker.models import Expenses


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Expenses.objects.exists():
            print('Data already loaded')
            return
        print('Loading expenses data')
        for row in DictReader(open('./expense_data.csv')):
            expense = Expenses()
            expense.name = row['name']
            expense.spent_on = row['spent_on']
            expense.date = row['date']
            expense.amount = row['amount']
            expense.payment_method = row['payment_method']
            expense.save()
