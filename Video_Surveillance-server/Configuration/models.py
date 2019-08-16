from django.db import models


# Create your models here.
class idconfig(models.Model):
    terminal_id = models.CharField(max_length=64)
    res_id = models.CharField(max_length=64)
    config = models.CharField(max_length=1000)
    capturedserver = models.CharField(max_length=200)
    interval = models.CharField(max_length=200)


class rtsp(models.Model):
    terminal_id = models.CharField(max_length=64)
    res_id = models.CharField(max_length=64)
    res_name = models.CharField(max_length=200)
    camid = models.CharField(max_length=200)
    rtsp = models.CharField(max_length=1000)
    cam_name = models.CharField(max_length=200)


class user(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)


class Cache(models.Model):
    index = models.CharField(max_length=200,default='D:\\')
    volume = models.CharField(max_length=50,default='50')


class Restaurant(models.Model):
    res_id = models.CharField(max_length=64)

    def __str__(self):
        return self.name