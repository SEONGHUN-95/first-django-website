from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from ..models import Question

def index(request):
    """
    질문 목록
    """
    #입력 파라미터
    page = request.GET.get('page','1')
    
    #조회하기
    question_list = Question.objects.order_by('-create_date')
    
    #페이징처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'cash/question_list.html', context)
 
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

    context = {'question': question, 'question_list' : page_obj}
    return render(request, 'cash/question_detail.html', context)
