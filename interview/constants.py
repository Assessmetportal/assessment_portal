from django.utils.translation import gettext_lazy as _

# Grades
UNDEFINED = 'UNDEFINED'
JUNIOR = 'JUNIOR'
MIDDLE = 'MIDDLE'
SENIOR = 'SENIOR'

GRADES_DICT = {
    UNDEFINED: _('Undefined'),
    JUNIOR: _('Junior'),
    MIDDLE: _('Middle'),
    SENIOR: _('Senior'),
}

GRADES_TYPES = ((k, v) for k, v in GRADES_DICT.items())
