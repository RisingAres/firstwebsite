from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('There are no users with this login')
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise forms.ValidationError('Invalid password, try it once')


class RegistrationForm(forms.ModelForm):

    password_check = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)

    class Meta:
        model = User  # get_user_model()
        fields = [
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = 'Required field'
        self.fields['password'].label = 'Password'
        self.fields['password_check'].help_text = 'Confirm the password'
        self.fields['first_name'].label = 'First name'
        self.fields['last_name'].label = 'Last name'
        self.fields['email'].label = 'Email'

    # for checking errors
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The user with the same name already exists !!!')
        if password != password_check:
            raise forms.ValidationError('Your passwords do not match')
