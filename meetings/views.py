from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from meetings.models import Meeting
from django.forms import modelform_factory

# Create your views here.
def meetings(request):
    return render(request, 'meetings/meetingsHome.html', 
        { "num_meetings": Meeting.objects.count(),
        "meetings": get_list_or_404(Meeting)
    })

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', { 'meeting': meeting })

MeetingForm = modelform_factory(Meeting, exclude=[])

def add(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('meetingsHome')
    else:
        form = MeetingForm()
    return render(request, 'meetings/add.html', { 'form': form })