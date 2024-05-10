from django import forms
from .models import Products,Doctor,Schedule,Deals
from django.forms import TextInput,DateInput,TimeInput
import datetime
from datetime import datetime, timedelta

class Add_product(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['Name','Company_Name','Image','Price']
        widgets = {
            'Name':TextInput(attrs={
                'class':'form-control',
                'style':'max-width: 300px',
                'placeholder':"Enter Product's Name"
            }),

            'Company_Name':TextInput(attrs={
                'class':'form-control',
                'style':'max-width: 300px',
                'placeholder':"Enter Company's Name"
            }),
               'Price':TextInput(attrs={
                'class':'form-control',
                'style':'max-width: 300px',
                'placeholder':"Enter Product's Price"
        })
        }
class Add_Doctor(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['Name','Specialisation','Contact','Location']
        widgets = {
            'Name':TextInput(attrs={
                'class':'form-control',
                'style':'max-width: 300px',
                'placeholder':"Enter Doctor's Name"
            }),

            'Specialisation':TextInput(attrs={
                'class':'form-control',
                'style':'max-width: 300px',
                'placeholder':"Enter Doctor's Specialisation"
            }),
               'Contact':TextInput(attrs={
                'class':'form-control',
                'style':'max-width: 300px',
                'placeholder':"Enter Doctor's Contact Number"
            }),
               'Location':TextInput(attrs={
                'class':'form-control',
                'style':'max-width: 300px',
                'placeholder':"Enter Doctor's Location"
        })
        }
        
class ScheduleAppointment(forms.ModelForm):
    Name = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=True)
    class Meta:
        model = Schedule
        fields = ['Name', 'Date_Of_Schedule', 'Time_Of_Schedule']
        widgets = {
            'Date_Of_Schedule':DateInput(attrs={
                'type': 'date',
                'class': 'x',
                 'min': datetime.now().strftime("%Y-%m-%d")
            }),
             'Time_Of_Schedule':TimeInput(attrs={
                'type': 'time',
                'class': 'x'
            })
        }

class Add_Deals(forms.ModelForm):
    Doctor_Name = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=True)
    Product_Name = forms.ModelChoiceField(queryset=Products.objects.all(), required=True)
    class Meta:
        model = Deals
        fields= ['Quantity','Doctor_Name','Product_Name']