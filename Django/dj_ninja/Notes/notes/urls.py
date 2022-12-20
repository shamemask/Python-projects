from django.urls import path
from . import views
app_name = 'notes'
urlpatterns = [
	path('', views.home, name='home'),
    path('note/<note_id>', views.note, name='note'),
    path('category/<category_id>/<filt>/<arg>', views.category_detail_sort, name='detail'),
]