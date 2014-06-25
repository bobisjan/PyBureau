from __future__ import unicode_literals

from django.core.exceptions import ValidationError

from . import CardValidator
from .exceptions import InvalidCardError


def id_validator(value):
    try:
        CardValidator.validate(value, CardValidator.TYPE_ID)
    except InvalidCardError, e:
        raise ValidationError(str(e))
