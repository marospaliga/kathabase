import os
import json

from django.core.management.base import BaseCommand, CommandError

from lectures.models import LectureIndex, Question


class Command(BaseCommand):
    help = "Imports questions from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("topic", nargs="+", type=str)

    def handle(self, *args, **options):
        count = 0
        topic = options["topic"][0]

        # Make sure the filename exists
        if not os.path.isfile(topic):
            raise CommandError("File does not exist at the specified path.")

        self.stdout.write(self.style.SUCCESS(topic))

        with open(topic, encoding="utf-8") as data_file:
            data = json.load(data_file)

        lecture_index = LectureIndex.objects.first()
        if not lecture_index:
            raise CommandError("There is no LectureIndex. You need to create one first.")

        for item in data:
            # {'topic': 'Topic 1', 'answer': 'Answer 1'}
           
            question = Question(title=item['topic'], answer=item['answer'])
            lecture_index.add_child(instance=question)

            count += 1

        self.stdout.write(self.style.SUCCESS("Successfully imported %d questions" % count))
