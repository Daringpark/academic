from django.db import models

# Create your models here.
class GameSession(models.Model):

    target_number = models.IntegerField()
    # 처음 비어있는 상태를 받기 위해서
    user_guess_number = models.IntegerField(null = True, blank = True)
    counting_trial = models.IntegerField(default = 0)