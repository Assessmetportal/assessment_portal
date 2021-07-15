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

# Roles
INTERVIEW_PARTICIPANT = 'INTERVIEW_PARTICIPANT'
VIEWER = 'VIEWER'
TECHNICAL_EXPERT = 'TECHNICAL_EXPERT'
TECHNICAL_LEAD = 'TECHNICAL_LEAD'

ROLES_DICT = {
    INTERVIEW_PARTICIPANT: _('Interview participant'),
    VIEWER: _('Viewer'),
    TECHNICAL_EXPERT: _('Technical expert'),
    TECHNICAL_LEAD: _('Technical lead'),
}


GRADES_TYPES = ((k, v) for k, v in GRADES_DICT.items())
ROLES_TYPES = ((k, v) for k, v in ROLES_DICT.items())