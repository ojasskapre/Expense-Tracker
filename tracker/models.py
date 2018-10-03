from django.db import models
class Expenses(models.Model):
    name = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    date = models.DateField()
    amount = models.FloatField()
    spent_on = models.TextField()

    def __str__(self):
        return self.name
