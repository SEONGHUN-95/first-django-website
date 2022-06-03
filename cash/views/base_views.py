from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Count
from ..models import Question
from ..models import QuestionCount

def index(request):
    """
    질문 목록
    """
    #입력 파라미터
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')    
    so = request.GET.get('so','recent')
    #정렬
    if so == "recommend":
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    elif so == 'recent':
        question_list = Question.objects.order_by('-create_date')
    else:
        question_list = Question.objects.order_by('-view_count')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    #페이징처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page' :page, 'kw':kw, 'so':so}

    return render(request, 'cash/question_list.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def detail(request, question_id):

    """
    질문 내용
    """
    question = get_object_or_404(Question, pk=question_id)
    
    #입력 파라미터
    page = request.GET.get('page','1')
    
    #조회하기
    question_list = Question.objects.order_by('-create_date')   

    #페이징처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    # # 조회수
    # ip = get_client_ip(request)
    # cnt = QuestionCount.objects.filter(ip=ip, question=question).count()
    
    # if cnt == 0:
    #     qc = QuestionCount(ip=ip, question=question)
    #     qc.save()
    #     if question.view_count:
    #         question.view_count += 1
    #     else:
    #         question.view_count = 1
    #     question.save()
    question.view_count += 1
    question.save()
    context = {'question': question, 'question_list' : page_obj}
    return render(request, 'cash/question_detail.html', context)
