from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import Participant

# Create your views here.
def participant_list(request):
  context = {'participant_list': Participant.objects.all()}
  return render(request, "attendance/participant_list.html", context)

def participant_form(request, num=0):
  if request.method == "GET":
    if num == 0:
      form = ParticipantForm()
    else:
      participant = Participant.objects.get(pk=num)
      form = ParticipantForm(instance=participant)
    return render(request, "attendance/participant_form.html", {'form':form})
  else:
    if num == 0:
      form = ParticipantForm(request.POST)
    else:
      participant = Participant.objects.get(pk=num)
      form = ParticipantForm(request.POST, instance=participant)
    if form.is_valid():
      form.save()
    return redirect('/participant/')

def participant_delete(request, num):
  participant = Participant.objects.get(pk=num)
  participant.delete()
  return redirect('/participant/')