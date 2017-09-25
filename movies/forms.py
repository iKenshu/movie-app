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
    CHOICES = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )

    rating = forms.ChoiceField(
        choices=CHOICES, 
        required=True,
        label='Rate this movie',
        help_text='Choose a rate 1 = Worst and 5 = Best'
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']