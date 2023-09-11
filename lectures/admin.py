from django.contrib import admin
from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Lecture




class TranscriptAdmin(ModelAdmin):
    model = Lecture
    menu_label = "Transcripts"
    list_display = ("truncated_transcript",)
    search_fields = ("transcript",)

    def truncated_transcript(self, obj):
        MAX_LENGTH = 100  # Maximum length of the truncated transcript
        if len(obj.transcript) > MAX_LENGTH:
            return f"{obj.transcript[:MAX_LENGTH]}..."
        else:
            return obj.transcript

    truncated_transcript.short_description = "Transcript"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.exclude(transcript__exact='')

modeladmin_register(TranscriptAdmin)
