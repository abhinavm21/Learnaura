from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # This will create form based on variables in Room model
        # The updated and created will not show as they are not editable
        # for sepearate variables we can do ['name','body'] like this
        exclude = ['host','participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email'] 
