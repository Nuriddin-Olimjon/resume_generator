from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r"^((\+998)|(998))\d{9}$",
    message="The phone number should look like this: \n998901234567",
)
