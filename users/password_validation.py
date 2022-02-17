import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class AlphabeticPasswordValidator:
    """
    Validate whether the password is alphabetic.
    """
    def validate(self, password, user=None):

        if not re.search(r'[0-9]', password):   # Если в пароле нет цифр, то вызываем ошибку валидации.
            raise ValidationError(
                _("This password does not contain numbers."),
                code='password_without_numbers',
            )

    def get_help_text(self):
        return _('Your password can’t be without numbers.')