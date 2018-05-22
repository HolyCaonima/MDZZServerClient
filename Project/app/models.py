# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    type = models.CharField(max_length=10)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Boss(models.Model):

    account = models.OneToOneField(Account, on_delete=models.CASCADE)


class KeFu(models.Model):

    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)

    account = models.OneToOneField(Account, on_delete=models.CASCADE)


class Worker(models.Model):

    account = models.OneToOneField(Account, on_delete=models.CASCADE)


class Order(models.Model):

    kefu = models.ForeignKey(KeFu, on_delete=models.CASCADE)

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    invitation = models.CharField(max_length=50)


class BW(models.Model):

    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
