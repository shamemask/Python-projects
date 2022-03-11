from django.urls import path
from django.views.generic import TemplateView

from games.views import GameListView, GameDetailView


urlpatterns = [
    path('', GameListView.as_view(), name='home'),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail'),
]
