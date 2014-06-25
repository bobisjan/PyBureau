from __future__ import unicode_literals

from django.core.exceptions import ValidationError

from .interior import validate
from .exceptions import InvalidCardError


def id_validator(value):
  try:
    validate(value, TYPE_ID)
  except InvalidCardError, e:
    raise ValidationError(str(e))
