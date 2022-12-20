from django.shortcuts import render, get_object_or_404
from .models import Category, Note
import datetime

def home(request):
    return render(request, 'index.html', {
        'categories': Category.objects.all()
    })



def category_detail_sort(request, category_id, filt, arg):
    filtname = ''
    filtvalue = ''
    print(filt)
    if len(filt.split('+')) > 1:
        filtname, filtvalue= filt.split('+')
    category = get_object_or_404(Category, id=category_id,)
    q = category.notes.all().order_by(arg)
    if filtname and filtvalue:
        if filtname == 'title':
            q = q.filter(title__contains=filtvalue)
        elif filtname == 'created':
            filtvalue = filtvalue.replace('%20',' ')
            date = datetime.datetime.strptime(filtvalue, "%d.%m.%Y %H:%M:%S")
            print(date)
            q = q.filter(created=date)
        elif filtname == 'favorite':
            q = q.filter(favorite=filtvalue)
        elif filtname == 'completed':
            q = q.filter(completed=filtvalue)
            
    
    setattr(category, 'note', q)
    category.save()
    for note in category.note.all():
        print(note.id)
    return render(request, 'detail_sort.html', {
        'category': category,
        'arg': arg,
        'filtname': filtname,
        'filtvalue': filtvalue
    })

def note(request, note_id):
    note = get_object_or_404(Note, id=note_id,)
    return render(request, 'detail_note.html', {
        'note': note,
    })