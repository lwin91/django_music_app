from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Playlist, View
from django.template import loader

# Create your views here.

def index(request):
    songs = Song.objects.all()
    q = View.objects.all()
    t = list(set([i.view_date for i in q]))
    total_view_counts = []
    for i in t:
    	time_ = '{}/{}/{}'.format(i.year, i.month, i.day)
    	a = View.objects.filter(view_date=i)
    	profit = round(len(a) * 0.001, 3)
    	total_view_counts.append({'time': time_, 'length': len(a), 'profit': profit})
    s = list(set([i.song for i in q]))
    all_songs = []
    for i in s:
    	song_name = i.title
    	a = View.objects.filter(song=i)
    	profit = round(len(a) * 0.001, 3)
    	all_songs.append({'song_name': song_name, 'length': len(a), 'profit': profit})
    c = [i['length'] for i in total_view_counts]
    forecast_for_month = int(sum(c) / len(c) * 30)
    profit_for_month = round(forecast_for_month * 0.001, 3)
    context = {
        'songs': songs,
        'total_view_counts': total_view_counts,
        'all_songs': all_songs,
        'forecast_for_month': forecast_for_month,
        'profit_for_month': profit_for_month
    }
    return render(request, 'music/index.html', context)
    

def detail(request, song_id):
	try:
		s = Song.objects.get(id=song_id)
		q = View.objects.filter(song=s)
		total_view_counts = []
		all_q = View.objects.all()
		t = list(set([i.view_date for i in all_q]))
		for i in t:
			time_ = '{}/{}/{}'.format(i.year, i.month, i.day)
			a = View.objects.filter(view_date=i, song=s)
			total_view_counts.append({'time': time_, 'length': len(a)})
		context = {
	        'total_views': len(q),
	        'total_view_counts': total_view_counts,
	    }
		return render(request, 'music/detail.html', context)
	except:
		data = 'No view for this song'
		return HttpResponse(data)

def results(request, song_id):
    response = "You're looking at the results of song %s."
    return HttpResponse(response % song_id)

def view(request, song_id):
	song_ = Song.objects.get(id=song_id)
	song = View(song=song_)
	song.save()
	return HttpResponse("You're viewing on song %s." % song.song)