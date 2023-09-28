import json
import csv
import os.path
from django.core.management.base import BaseCommand, CommandError
from recipes.models import Ingredient, Tag


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        file_path = "data/ingredients.json"
        try:
            if os.path.exists(file_path) is True:
                with open('data/ingredients.json', encoding='utf-8',
                          ) as data_file_ingredients:
                    ingredient_data = json.loads(data_file_ingredients.read())
                    for ingredients in ingredient_data:
                        Ingredient.objects.get_or_create(**ingredients)

            else:
                MODELS_FILES = {Ingredient: 'ingredients.csv', }
                for model, file in MODELS_FILES.items():
                    with open(f'/data/{file}', encoding='utf-8',
                              ) as data_file_ingredients_2:
                        reader = csv.DictReader(data_file_ingredients_2)
                        model.objects.bulk_create(
                            model(**data) for data in reader
                        )

            with open('data/tags.json', encoding='utf-8',
                      ) as data_file_tags:
                tags_data = json.loads(data_file_tags.read())
                for tags in tags_data:
                    Tag.objects.get_or_create(**tags)

            self.stdout.write(self.style.SUCCESS('Данные загружены'))

        except FileNotFoundError:
            raise CommandError('Файл отсутствует в директории data')
