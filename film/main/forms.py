from django import forms


class RechercheForm(forms.Form):
    id = forms.CharField(required=False, label='Id :', widget=forms.TextInput(attrs={'placeholder': 'Id'}))
    titre = forms.CharField(required=False, label='Titre :', widget=forms.TextInput(attrs={'placeholder': 'Titre'}))
    real = forms.CharField(required=False, label='Réalisateur :', widget=forms.TextInput(attrs={'placeholder': 'Réalisateur'}))
    lang = forms.CharField(required=False, label='Langue :', widget=forms.TextInput(attrs={'placeholder': 'Langue'}))
    date = forms.CharField(required=False, label='Date :', widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    duree = forms.CharField(required=False, label='Durée :', widget=forms.TextInput(attrs={'placeholder': 'Durée'}))
    color = forms.CharField(required=False, label='Couleur :', widget=forms.TextInput(attrs={'placeholder': 'Couleur'}))
    voix = forms.CharField(required=False, label='Voix :', widget=forms.TextInput(attrs={'placeholder': 'Voix'}))
    disque = forms.CharField(required=False, label="Disque :", widget=forms.TextInput(attrs={'placeholder': "Disque"}))
    type = forms.CharField(required=False, label='Type :', widget=forms.TextInput(attrs={'placeholder': 'Type'}))
    acteurs = forms.CharField(required=False, label='Acteurs :', widget=forms.TextInput(attrs={'placeholder': 'Acteurs'}))


