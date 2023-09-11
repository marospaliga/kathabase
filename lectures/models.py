from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.documents.models import AbstractDocument, Document
from wagtail.search import index





class LectureIndex(Page):
    parent_page_types = [
        'home.Homepage',
    ]
    subpage_types = [
        'lectures.Lecture',
        'lectures.Question',
        'lectures.Article'
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(LectureIndex, self).get_context(request)

        lectures = self.get_children().live().specific()
        context['lectures'] = lectures

        return context


class Lecture(Page):
    parent_page_types = [
        'lectures.LectureIndex',
    ]
    filename = models.CharField(
        max_length=100, blank=True, help_text="Audio filename of the lecture")
    
    transcript = models.TextField(
        blank=True,
        help_text="Transcript of the lecture"
    )
    
    search_fields = Page.search_fields + [ # Inherit search_fields from Page
        index.SearchField('transcript'),]
    

    content_panels = Page.content_panels + [
        FieldPanel("filename"),
        FieldPanel('transcript'),
    ]
    
class Question(Page):
    parent_page_types = [
        'lectures.LectureIndex',
    ]
  
    
    answer = models.TextField(
        blank=True, 
        help_text="Various Q&A"
    )

    content_panels = Page.content_panels + [
        FieldPanel('answer'),
    ]

class Article(Page):
    parent_page_types = [
        'lectures.LectureIndex',
    ]
  
    
    content = models.TextField(
        blank=True, 
        help_text="Articles from harmonist.us"
    )
    

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

