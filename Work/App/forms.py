from django import forms

class InputCaption(forms.Form):
    caption = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form__block__chapter__input', 'name': 'chapter'}))

class InputPrice(forms.Form):
    price = forms.IntegerField(required=True, label="", widget=forms.TextInput(attrs={'class':'form__block__chapter__input', 'name': 'price'}))

class InputpathImg(forms.Form):
    path_img = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__chapter__input', 'name': 'path_img'}))

class InputSelect(forms.Form):
    ch = forms.ChoiceField(choices=((1, 'Процессоры'), (2, 'Видеокарты'), (3, 'Оперативная память')), label='', widget=forms.Select(attrs={'class': 'form__block__chapter__input__radial'}))