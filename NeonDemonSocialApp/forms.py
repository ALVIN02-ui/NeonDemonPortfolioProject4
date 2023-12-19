from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # adds classnames to the fields
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'responsive-textarea'
    
    class Meta:
        model = Review
        fields = ['rating', 'content', 'name']
        content = forms.CharField(widget=forms.Textarea(attrs={'class': 'responsive-textarea'})),
        labels = {
            'content': '',
            'rating': '',
            'name': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 45, 'placeholder': 'Write your review here...'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'rating': forms.TextInput(attrs={'placeholder':'Leave your rating (1-5)'}),
        }
    
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating should be between 1 and 5")
        return rating

    def clean_content(self):
        content = self.cleaned_data['content']
        return content