from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email",required=True, widget=forms.EmailInput(
        attrs= {'class':'form-control', 'placeholder':'ejemplo@utp.edu.co'}), max_length=100, min_length=3) #campo opcional
    
    contraseña = forms.CharField(label="Contraseña", required=True, widget= forms.PasswordInput(attrs= {'class':'form-control', 'placeholder':'Contraseña'})) 
