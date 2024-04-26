from django.db import models

# Create your models here.
class Weather(models.Model):
    dx_txt = models.DateTimeField() # 관측 시간
    temp = models.FloatField()      # 당시 온도 (단위 : K)
    feels_like = models.FloatField() # 체감 온도 (단위 : K)
