from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.db.models import Count

class Line(models.Model):
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.number


class Station(models.Model):
    name = models.CharField(max_length=100)
    # name_eng = models.CharField(max_length=100)
    line = models.ManyToManyField(Line)
    # number = models.IntegerField(default=0)
    code = models.CharField(max_length=10, blank=True)
    matrix = models.CharField(max_length=30)
    text_anchor = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('station:station_detail', args=[self.pk])

    def get_best_nick(self):
        best_nick = Nick.objects.filter(station_id=self.id)\
            .annotate(num_likes=Count('like'))\
            .order_by('-num_likes')
        return best_nick
        # by importing django.db.models.Count, you can count foreignkey(likes) by which nicks can be sorted

        # template 에서 station.get_best_nick처럼 함수 불러올 수 있음
        # self 이외의 인자가 필요한 함수라면 {% url "xx" %} 처럼 double-quote 안에 넣을 수 있음!


class Nick(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.TextField(max_length=10, verbose_name="This station is...")
    # num_of_likes = models.IntegerField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_likes(self):
    #     num_of_likes = Like.objects.filter(nick_id=self.id).count()
    #     return num_of_likes


class Like(models.Model):
    # count = models.IntegerField(default=0)
    nick = models.ForeignKey(Nick, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nick.name
