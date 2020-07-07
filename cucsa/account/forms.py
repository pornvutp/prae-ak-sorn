from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        fields = ("email",)
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "อีเมล"
        self.fields["password1"].label = "รหัสผ่าน"
        # self.fields["password1"].help_text = "รหัสผ่าน"
        self.fields["password2"].label = "ยืนยันรหัสผ่าน"
