from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'profession',
            'phone_number',
            'region',
            'address',
            'profile',
            'email',
            'place_of_birth',
            'skills',
            'hobbies',
            'languages',
            'achievements',
            'image',
        )
        help_texts = {
            'username': None,
        }
