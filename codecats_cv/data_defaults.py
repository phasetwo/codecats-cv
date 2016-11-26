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
        ('Fachinformatiker Anwendungsentwicklung', '#'), # wud? URL?
        ('Automation Engineer', 'https://www.avira.com')
    )
    DESCRIPTION = (
        'This is my personal online CV, designed with '
        'Python HTML, CSS and JavaScript.')
    PHONE = '+12 345 6789 1011'
    ADDRESS = [
        'Pfitznerstr. 1',
        '80807 Munich',
        'Germany',
    ]
    SKILLS = [
        'C#',
        'AutoIt',
        'PHP',
        'hopefully Python soon'
    ]
    LANGUAGES = [
        Language('German', 'germany', 101),
        Language('English', 'us', 80),
        Language('Italian', 'it', 20),
        Language('Spanish', 'es', 15)
    ]
