# PyBureau [![Build Status](https://secure.travis-ci.org/bobisjan/PyBureau.png?branch=next)](http://travis-ci.org/bobisjan/PyBureau)

Set of utilities based on the applications provided by the administration authorities in the Czech Republic.

## Ministry of the Interior

Module `interior` is for an invalid card (IDs, passports, etc.) detection against the central repository provided by the ministry.

### Basic Usage

```python
from pybureau.interior import CardValidator

try:
  CardValidator.validate('1234') # validates ID card
except InvalidCardError, e:
  print 'Ouch, this ID card is invalid!'
```

### Django Validators

```python
from pybureau.interior.validators import id_validator
from django import forms

class UserForm(forms.Form):
  id_card = forms.CharField(blank=False, null=False, max_length=30, required=True, validators=[id_validator])
```

## Contact

Jan Bobisud

- http://github.com/bobisjan
- me@bobisjan.com

## License

PyBureau is available under the MIT license. See the LICENSE file for more info.
