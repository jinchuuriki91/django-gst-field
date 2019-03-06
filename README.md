# django-gst-field

A Django library which provides model and form fields for `Goods and Services Tax` and `Permanent Account Number`

Includes:

 - `GSTField`, form and model field
 - `PANField`, form and model field

## Installation
```
pip install django-gst-field
```

### Basic usage

Add `gst_field` to the list of the installed apps in Django `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'gst_field',
    ...
]
```

### Model usage

```python
from django.conf import settings
from django.db.models import ForeignKey, CASCADE, Model
from gst_field.modelfields import GSTField, PANField

class Tax(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    gstin = GSTField()
    pan = PANField()
```