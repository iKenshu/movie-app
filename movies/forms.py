from django import forms

from .models import Movie, Review

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'synopsis', 'poster', 'director']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'synopsis': forms.Textarea(attrs={'class':'form-control'}),
            'director': forms.TextInput(attrs={'class':'form-control'}), 
        }

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['comment', 'rating']