from django.forms import ModelForm
from .models import thebricks

class thebricksForm(ModelForm):
	
	class Meta:
		model = thebricks
		fields = ('brick_type', 'brick_width', 'brick_length', 'brick_height', 'my_color')