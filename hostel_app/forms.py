from django import forms
from hostel_app.models import Booking
from profile_user.models import Profile

class RoomSearchForm(forms.Form):
    search = forms.CharField(max_length=128)
    
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('is_checkout','services','status', 'user')
        
        
    
        
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture','location', 'birth_date']


