from django.db import models


class Blogger(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500, blank=False, verbose_name="Имя")
    username = models.CharField(max_length=500, blank=False, verbose_name="Ник")
    url = models.CharField(max_length=500, blank=False, verbose_name="url")
    followers_count = models.BigIntegerField(blank=False, verbose_name="Кол-во подписчиков")
    followings_count = models.BigIntegerField(blank=False, verbose_name="Кол-во подписок")
    posts_count = models.BigIntegerField(blank=False, verbose_name="Кол-во публикауий")
    man_percent = models.IntegerField(blank=False, verbose_name="Мужчины %")
    woman_percent = models.IntegerField(blank=False, verbose_name="Женщины %")
    bots_percent = models.IntegerField(blank=False, verbose_name="Боты %")
    commerce_accounts_percent = models.IntegerField(blank=False, verbose_name="Коммерческие аккаунты %")

    class Meta:
        ordering = ['created']
