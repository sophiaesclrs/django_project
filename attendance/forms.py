from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):

  class Meta:
    model = Participant #name you made in the models.py
    fields = '__all__'
    labels = {
      'student_num':'ID Number',
      # 'fullname': 'Fullname',
      'year':'Year Level',
      # 'college':'College',
      # 'course':'Course',
      # 'major':'Major'
    }

  def __init__(self, *args, **kwargs):
    super(ParticipantForm,self).__init__(*args, **kwargs)
    self.fields['college'].empty_label = ""