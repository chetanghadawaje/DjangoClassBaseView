from django.core.exceptions import ValidationError


def phone_number_validators(value):
    if len(value) != 10:
        raise ValidationError(
            f"{value} is not an valid phone number"
        )