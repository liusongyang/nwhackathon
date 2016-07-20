from datetime import datetime
from pytz import timezone
from slugify import slugify

class Workshop:
    __slots__ = ['title', 'when', 'location', 'series', 'facebook_event']

    def __init__(self, title, when, location, facebook_event, series=None):
        self.title = title
        self.when = when
        self.location = location
        self.facebook_event = facebook_event
        self.series = series

    @property
    def title_slug(self):
        return slugify(self.title)

    @property
    def series_slug(self):
        return slugify(self.series)

    def __str__(self):
        base = '"{}" at {} in {}'.format(self.title, self.when, self.location)
        if self.series is not None:
            self.series + ': ' + base
        else:
            self.series

    def __repr__(self):
        return '<Workshop title="{}", when={}, location="{}", series="{}", facebook_event={}>' \
            .format(self.title, self.when, self.location, self.series, self.facebook_event)

eastern = timezone('US/Eastern')

workshops = [
    Workshop('Cloud Hosting with Microsoft Azure',
             datetime.fromtimestamp(1448926200, eastern),
             'CIT 316', 'https://www.facebook.com/events/139565859737837/'),
    Workshop('Data with Python',
             datetime.fromtimestamp(1448321400, eastern),
             'Smitty-B 106', 'https://www.facebook.com/events/759393817538731/', 'Python'),
    Workshop('Hangman with Python: An Introduction to Programming',
             datetime.fromtimestamp(1447284600, eastern),
             'MacMillan 117', 'https://www.facebook.com/events/1488634168107009/', 'Python'),
    Workshop('Python with Paxson: An Introduction to Programming',
             datetime.fromtimestamp(1446507000, eastern),
             'MacMillan 117', 'https://www.facebook.com/events/832881926810717/', 'Python'),
    Workshop('JavaScript Workshop', datetime.fromtimestamp(1446071400, eastern),
             '85 Waterman St.', 'https://www.facebook.com/events/161691197513226/'),
    Workshop('Internet Workshop', datetime.fromtimestamp(1444343400, eastern),
             'Wilson 102', 'https://www.facebook.com/events/652888234814711/'),
    Workshop('HTML/CSS Workshop', datetime.fromtimestamp(1442269800, eastern),
             'Metcalf Auditorium', 'https://www.facebook.com/events/1626068997681433/')
]


def past_workshops():
    return [w for w in workshops if w.when < datetime.now(eastern)]


def upcoming_workshops():
    return [w for w in workshops if w.when >= datetime.now(eastern)]


def by_title(title):
    for workshop in workshops:
        if slugify(workshop.title) == title:
            return workshop
    raise KeyError('Workshop with title "{}" not found'.format(title))


def by_series(name):
    return [w for w in workshops if slugify(w.series) == name]
