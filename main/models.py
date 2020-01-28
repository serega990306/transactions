from django.db import models

# Create your models here.


class Currency(models.Model):
    title = models.CharField(max_length=5)

    def __str__(self):
        return self.title


class Account(models.Model):
    balance = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Transactions(models.Model):
    user_post = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_post')
    user_get = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_get')
    operation_dttm = models.DateTimeField(auto_now_add=True)
