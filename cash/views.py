from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

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

# def detail(request, question_id):
#     """
#     질문 내용
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'cash/question_detail.html', context)

def answer_create(request, question_id):
    """
    답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('cash:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'cash/question_detail.html', context)  

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('cash:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'cash/question_form.html', context)