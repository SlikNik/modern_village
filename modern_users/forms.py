from django import forms
from modern_users.models import ModernUsers

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ModernUsers
        fields = ('first_name', 'last_name', 'email', 'address', 'city', 'zipcode', 'age', 'birthday', 'facebook', 'instagram', 'twitter', 'username', 'password', 'user_pic',)

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ModernUsers
        fields = ('first_name', 'last_name', 'address', 'city', 'zipcode', 'age', 'birthday', 'facebook', 'instagram', 'twitter', 'user_pic',)
