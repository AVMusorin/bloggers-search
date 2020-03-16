from django.db import models

INCOMES = [
    ("LOW", "Ниже среднего"),
    ("MIDDLE", "Средний"),
    ("HIGH", "Выше среднего")
]

CITIES = [
    ("moscow", "Москва"),
    ('others', "другие")
]


class FollowersAgeIntervals(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500, blank=False, verbose_name="Название интервала")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Subject(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500, blank=False, verbose_name="Название сферы деятельности")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Blogger(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500, blank=False, verbose_name="Имя")
    username = models.CharField(max_length=500, blank=False, verbose_name="Ник")
    url = models.CharField(max_length=500, blank=False, verbose_name="url")
    age = models.IntegerField(null=True, blank=True, verbose_name="Возраст")
    followers_count = models.BigIntegerField(blank=False, verbose_name="Кол-во подписчиков")
    followings_count = models.BigIntegerField(blank=False, verbose_name="Кол-во подписок")
    posts_count = models.BigIntegerField(blank=False, verbose_name="Кол-во публикауий")
    man_percent = models.IntegerField(blank=True, verbose_name="Мужчины %")
    woman_percent = models.IntegerField(blank=True, verbose_name="Женщины %")
    bots_percent = models.IntegerField(blank=True, verbose_name="Боты %")
    commerce_accounts_percent = models.IntegerField(blank=True, verbose_name="Коммерческие аккаунты %")
    income = models.CharField(blank=True, max_length=500, choices=INCOMES, null=True, verbose_name="Уровень дохода")
    city = models.CharField(null=True, max_length=500, blank=True, verbose_name="Города", choices=CITIES)
    followers_age = models.ForeignKey(null=True, to=FollowersAgeIntervals, on_delete=models.DO_NOTHING,
                                      verbose_name="Возраст подписчиков")
    subject = models.ForeignKey(null=True, to=Subject, on_delete=models.DO_NOTHING, verbose_name="Сфера деятельности")

    class Meta:
        ordering = ['created']
