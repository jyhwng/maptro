from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse

from .models import *
from .forms import NickForm
from django.db.models import F
from django.contrib.auth.decorators import login_required

from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# To count foreignkey and sort nick by it
# https://docs.djangoproject.com/en/1.10/topics/db/aggregation/


def home(request):
    lines = Line.objects.all()
    stations = Station.objects.all()
    form = NickForm()

    # if request.method == 'POST':
    #     if request.is_ajax():
    #         nick = Nick(request.session)
    #         name = request.POST.get('name')
    #         print(name)
    #         return JsonResponse({
    #             'message':'update {} for {}'.format(nick, nick.station)
    #             })
    #     return render(request, 'map/index.html', context)

    context = {
        'lines' : lines,
        'stations' : stations,
        'form' : form,
    }

    return render(request, 'map/index.html', context)


@login_required
def station_detail(request, station_pk):
    station = Station.objects.get(pk=station_pk)
    form = NickForm()

    top_nicks = Nick.objects.filter(station_id=station_pk)\
                .annotate(num_likes=Count('like'))\
                .order_by('-num_likes')
    # user_likes = Like.objects.filter(user_id=request.user.id)

    # paginator = Paginator(top_nicks, 10)
    # page_request_var = 'page'
    # page = request.GET.get(page_request_var)
    #
    # try:
    #     nicks = paginator.page(page)
    # except PageNotAnInteger:
    #     nicks = paginator.page(1)
    # except EmptyPage:
    #     nicks = paginator.page(paginator.num_pages)

    context = {
        'station' : station,
        'form' : form,
        'top_nicks' : top_nicks,
        # 'page_request_var' : page_request_var,
        # 'user_likes' : user_likes,
    }

    if request.method == "POST":
        form = NickForm(request.POST)
        if form.is_valid():
            nick = form.save(commit=False)
            nick.station = station
            nick.author = request.user
            # nick 쓴 사람이 request.user 라는거 지정 안하면 not null constraint 생김
            # ForeignKey - station 으로 엮여 있기 때문에 어떤 station의 nick 인지 이렇게 지정 안해주면 intergrity error - not null constraint 나옴
            nick.save()

            # return render(request, 'map/station_detail.html', context)
            return JsonResponse({
                        'name' : nick.name,
                        'id' : nick.id,
                        })


@login_required
def nick_like(request, station_pk, nick_pk):
    station = get_object_or_404(Station, pk=station_pk)
    nick = get_object_or_404(Nick, pk=nick_pk)
    # nick.like = F('like') + 1
    # incrementing at database level. not using memory
    # nick.save()
    user = request.user
    like = Like.objects.filter(nick_id=nick.id, user_id=user.id)

    if like.count() == 0:
        Like.objects.create(nick_id = nick_pk, user_id=user.id)
    else:
        like.delete()

    return redirect(station)


@login_required
def nick_delete(request, station_pk, nick_pk):
    station = get_object_or_404(Station, pk=station_pk)
    nick = get_object_or_404(Nick, pk=nick_pk)
    if request.user == nick.author:
        nick.delete()
    return JsonResponse({})


def logout(request):
    # return redirect(home)
    return render(request, 'map/logout.html')


def mypage(request):
    user = request.user
    my_nicks = Nick.objects.filter(author_id=user.id)\
        .order_by('created_at')

    paginator = Paginator(my_nicks, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        nicks = paginator.page(page)
    except PageNotAnInteger:
        nicks = paginator.page(1)
    except EmptyPage:
        nicks = paginator.page(paginator.num_pages)

    context = {
        'user' : user,
        'page_request_var' : page_request_var,
        'nicks' : nicks,
        'my_nicks' : my_nicks,
    }
    return render(request, 'map/mypage.html', context)
# logout redirect home 어떻게 하지? url 에 걸린게 auth_views 인데...
