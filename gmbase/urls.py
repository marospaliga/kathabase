from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from lectures import views as lecture_views


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("tran_search/", lecture_views.tran_search, name="tran_search"),
    path("article_search/", lecture_views.article_search, name="article_search"),
    path("question_search/", lecture_views.question_search, name="question_search"),
    path("universal_search/", lecture_views.universal_search, name="universal_search"),
    path("question_list/", lecture_views.question_list, name="question_list"),
    path("article_list/", lecture_views.article_list, name="article_list"),
    path("lecture_list/", lecture_views.lecture_list, name="lecture_list"),
    path('question/<int:question_id>/', lecture_views.question_detail, name='question_detail'),
    path('article/<int:article_id>/', lecture_views.article_detail, name='article_detail'),    
    path('lecture/<int:lecture_id>/', lecture_views.lecture_detail, name='lecture_detail'),
    path('all_search/', lecture_views.all_search, name='all_search'),
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
