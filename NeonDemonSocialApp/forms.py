from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content', 'name']
        labels = {
            'rating': 'Rating (1-5)',
            'content': 'Review Content',
            'name': 'Your Name',
        }
    
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating should be between 1 and 5")
        return rating

    def clean_content(self):
        content = self.cleaned_data['content']
        # Add additional validation rules for content if needed
        return content