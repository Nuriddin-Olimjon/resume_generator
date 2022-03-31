from django.contrib.auth.tokens import PasswordResetTokenGenerator  
from django.core.validators import RegexValidator
import six


class TokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            six.text_type(user.pk) + six.text_type(timestamp) +  
            six.text_type(user.is_active)  
        )  


phone_regex = RegexValidator(
    regex=r"^((\+998)|(998))\d{9}$",
    message="The phone number should look like this: \n998901234567",
)
