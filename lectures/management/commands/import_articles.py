import os
import json

from django.core.management.base import BaseCommand, CommandError

from lectures.models import LectureIndex, Article


class Command(BaseCommand):
    help = "Imports articles from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("filepath", type=str)

    def handle(self, *args, **options):
        count = 0
        filepath = options["filepath"]

        # Make sure the file exists
        if not os.path.isfile(filepath):
            raise CommandError("File does not exist at the specified path.")

        with open(filepath, encoding="utf-8") as data_file:
            data = json.load(data_file)

        lecture_index = LectureIndex.objects.first()
        if not lecture_index:
            raise CommandError("There is no LectureIndex. You need to create one first.")

        for item in data:
            # Create an Article instance and add it as a child to the lecture index
            article = Article(title=item["Article"], content=item['content'])
            lecture_index.add_child(instance=article)

            count += 1

        self.stdout.write(self.style.SUCCESS("Successfully imported %d articles" % count))
