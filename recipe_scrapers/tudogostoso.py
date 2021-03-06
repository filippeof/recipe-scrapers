from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string
import json


class TudoGostoso(AbstractScraper):

    @classmethod
    def host(self):
        return 'tudogostoso.com.br'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('time', {'class': 'dt-duration'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('span', {'class': "p-ingredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('div', {'class': "instructions e-instructions"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

        ])
