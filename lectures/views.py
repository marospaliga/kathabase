from django.shortcuts import render, get_object_or_404
from wagtail.core.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from wagtail.search.models import Query
from lectures.models import Lecture, Article, Question
from django.db.models import Q
from django.shortcuts import redirect



def page_list(request):
    pages = Page.objects.all()
    return render(request, 'lectures/page_list.html', {'pages': pages})


def tran_search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Lecture.objects.live().filter(
            Q(transcript__isnull=False, transcript__icontains=search_query) |
            Q(title__icontains=search_query)
        )
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Lecture.objects.none()

    # Pagination
    paginator = Paginator(search_results, 20)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/tran_search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )


def article_search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Article.objects.live().filter(
            Q(content__icontains=search_query) |
            Q(title__icontains=search_query)
        )

        # Pagination
        paginator = Paginator(search_results, 20)
        try:
            search_results = paginator.page(page)
        except PageNotAnInteger:
            search_results = paginator.page(1)
        except EmptyPage:
            search_results = paginator.page(paginator.num_pages)
    else:
        search_results = Article.objects.none()

    return TemplateResponse(
        request,
        "search/article_search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )


def question_search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Question.objects.live().filter(
            Q(answer__icontains=search_query) |
            Q(title__icontains=search_query)
        )

        # Pagination
        paginator = Paginator(search_results, 20)
        try:
            search_results = paginator.page(page)
        except PageNotAnInteger:
            search_results = paginator.page(1)
        except EmptyPage:
            search_results = paginator.page(paginator.num_pages)
    else:
        search_results = Question.objects.none()

    return TemplateResponse(
        request,
        "search/question_search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )



def all_search(request):
    query = request.GET.get('query', '')
    page = request.GET.get('page', 1)

    # Search in all Lecture, Question, and Article objects
    search_results = Page.objects.live().search(query)

    # Pagination
    paginator = Paginator(search_results, 20)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        'search/all_search.html',
        {
            'search_query': query,
            'search_results': search_results,
        }
    )



def universal_search(request):
    query = request.GET.get('query', '')
    search_type = request.GET.get('search_type', '')

    # Determine the appropriate search URL based on the selected search type
    
    if search_type == 'transcriptions':
        search_url = '/tran_search/?query={}'.format(query)
    elif search_type == 'articles':
        search_url = '/article_search/?query={}'.format(query)
    elif search_type == 'answers':
        search_url = '/question_search/?query={}'.format(query)
    elif search_type == 'all':
        search_url = '/all_search/?query={}'.format(query)

    return redirect(search_url)


from django.db.models import Q

def lecture_list(request):
    search_title = request.GET.get('search_title')

    if search_title:
        lectures = Lecture.objects.filter(title__icontains=search_title)
    else:
        lectures = Lecture.objects.all()

    paginator = Paginator(lectures, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'lectures/lecture_list.html', {
        'lectures': lectures,
        'page_obj': page_obj,
        'search_title': search_title
    })


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 50)  # 10 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lectures/article_list.html', {'page_obj': page_obj})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'lectures/question_list.html', {'questions': questions})



def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'lectures/question.html', {'question': question})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'lectures/article.html', {'article': article})

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'lectures/lecture.html', {'lecture': lecture})

