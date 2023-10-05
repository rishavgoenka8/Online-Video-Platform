import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SpecialCharValidator(object):

    ''' The password must contain at least 1 special character @#$%!^&* '''

    def __init__(self, *args, **kwargs):
        pass

    def validate(self, password, user=None):
        if not re.findall('[@#$%!^&*]', password):
            raise ValidationError(
                _("The password must contain at least 1 special character: " +
                  "@#$%!^&*"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character: " +
            "@#$%!^&*"
        )