from django.shortcuts import render, redirect, get_object_or_404
from .models import myText, Comment
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def home_list(request):

    texts = myText.objects.filter()
    print(texts)

    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})

def lecture_list(request):

    texts = myText.objects.filter()

    hot_lecture = myText.objects.filter(category="인기")

    return render(request, 'inflearn_lecture/lecture_list.html', 
                  {'texts': texts, 'hot_lecture': hot_lecture}
                  )

def login(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, username=email, password=password)
    
        if user is None:
            print("회원이 아니무니다.")
            return redirect('/join')
        else:
            auth.login(request, user)
            return redirect('/')

    return render(request, 'inflearn_lecture/login.html')

def join(request):

    print("join 실행")
    if request.method == 'POST':
        print("여기는 포스팅 요청")

        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=email, password=password)

        return redirect('/')

    print("join 마지막 부분")
    return render(request, 'inflearn_lecture/join.html')

def logout(request):

    auth.logout(request)

    return redirect('/')

def lecture_list_info(request, pk):

    board_contents = get_object_or_404(myText, pk=pk)
    comment = Comment.objects.filter(lecture = board_contents)
    
    if request.method == 'POST':
        rate = request.POST['rate']
        writer = request.POST['writer']
        comment = request.POST['comment']

        Comment.objects.create(lecture=board_contents,
                               writer=writer,
                               rate=rate,
                               comment=comment,
                               )
        return redirect('/lecture_list/' + str(pk))

    return render(request, 'inflearn_lecture/lecture_list_info.html', 
                  {
                    'board_contents':board_contents,
                    'comment': comment,
                   }
                  )

def comment_remove(request, pk):

    if request.method == 'POST':

        Comment.objects.get(pk=pk).delete()

    return redirect('/lecture_list')