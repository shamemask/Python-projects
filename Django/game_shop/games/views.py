from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from games.models import Game


class GameListView(ListView):
    model = Game
    template_name = 'games/home.html'
    context_object_name = 'game_list'


class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    context_object_name = 'game'


# ДЗ из 10 урока
def game_list(request):
    games = Game.objects.all()

    return render(request, 'games/home.html', {"game_list": games})


# ДЗ из 11 урока
def game_detail(request, slug):
    game = Game.objects.get(slug=slug)

    return render(request, 'games/game_detail.html', {"game": game})
