from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['decision',
                   'passwhy',
                   'beliefelicit',
                   'reward',
                   'instructions',
                   'goals'
                   ]


# class City(Page):
#     form_model = 'player'
#     form_fields = ['city',
#                    'yearsinmsc', 'mscyourcity', 'achieve', 'deput']


class Yourself(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'height',
                    'city',
                   'othercit',
                   'title',
                   'riskat',
                   'satis',
                   'trust',
                   'freedom'
                   ]

# class polit(Page):
#     form_model = 'player'
#     form_fields = ['freedom',
#                        'politics',
#                        'leftright',
#                        'owner',
#                        'responsibility',
#                        'democracy',
#                         'democracy_today',
#                         'renovation',
#                         'attitudes']

    def before_next_page(self):
        self.player.set_payoff()


page_sequence = [
    MyPage,
    Yourself #, polit, City,
]
