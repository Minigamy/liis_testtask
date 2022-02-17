# import re
#
#
#
#
# class AlphabeticPasswordValidator:
#     """
#     Validate whether the password is alphabetic.
#     """
#     def validate(self, password, user=None):
#
#         if not re.search(r'[0-9]', password):
#             raise ValidationError(
#                 _("This password does not contain numbers."),
#                 code='password_without_numbers',
#             )
#
#     def get_help_text(self):
#         return _('Your password can’t be without numbers.')