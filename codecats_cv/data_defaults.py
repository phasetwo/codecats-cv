SECRET_INIT = ('dmendek', '<w}I*N.aR[.YjojIsc$N73XSZ58&)zCa', 'SBsBj,>n/5g]b634BBK+&.R!Jg%81s{(')
"""tuple containing username, password and secret session key"""


class Language:
    def __init__(self, name, flag, level):
        self.name = name
        self.flag = flag
        self.level = level


# TODO move into a db table
class MY:
    NAME = 'David Mendek'
    EMAIL = 'contact@david.mendek.com'
    TITLES = (
        ('', ''),
    )
    DESCRIPTION = (
        'Hello.')
    PHONE = ''
    ADDRESS = [
        '',
    ]
    SKILLS = [
        'C#',
        'PHP',
        'AutoIt',
        'Python'
    ]
    LANGUAGES = [
        Language('German', 'germany', 101),
        Language('English', 'us', 80),
        Language('Italian', 'it', 20),
        Language('Spanish', 'es', 15)
    ]
