# -*-  coding: utf-8 -*-

import os
import json

from django.core.management.base import BaseCommand, CommandError

from lectures.models import LectureIndex, Lecture



class Command(BaseCommand):
    help = "Imports lectures from json file."

    def add_arguments(self, parser):
        parser.add_argument("filename", nargs="+", type=str)

    def handle(self, *args, **options):
        count = 0
        filename = options["filename"][0]

        # make sure filename exists
        if not os.path.isfile(filename):
            raise CommandError("File does not exist at the specified path.")

        self.stdout.write(self.style.SUCCESS(filename))

        with open(filename, encoding="utf-8") as data_file:
            data = json.load(data_file)

        lecture_index = LectureIndex.objects.first()
        if not lecture_index:
            raise CommandError(
                "There is no LectureIndex. You need to create one first.")

        for item in data:
            # {'Link': '031226VT.mp3',
            #  'Name': 'Bhaktivinoda Parivara: Harinama & Diksa Initiation',
            #  'Transcript': None,
            #  'Tag': 'BVT Ki Jay!'}

            lecture = Lecture(filename=item['Link'], title=item['Name'], transcript=item['Transcript'])
            lecture_index.add_child(instance=lecture)

            count += 1

        self.stdout.write(self.style.SUCCESS(
            "Successfully imported %d lecture" % count))

