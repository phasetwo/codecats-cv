import logging

from codecats_cv.model import dbExperiences


class Experience:
    def __init__(
            self, category, what, when, title, url, location, flag,
            description, referenceName=None, referenceMail=None, img=None):
        self.category = category
        self.what = what
        self.when = when
        self.title = title
        self.url = url
        self.location = location
        self.flag = flag
        self.description = description
        self.referenceName = referenceName
        self.referenceMail = referenceMail
        self.img = img

    @property
    def asDict(self):
        return self.__dict__


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dbExperiences.purge()
    dbExperiences.insert_multiple([e.asDict for e in experiences])
    logging.info(dbExperiences.all())
