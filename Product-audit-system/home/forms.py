from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Roll number',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))