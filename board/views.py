from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Contact_Contact
from .forms import ContactForm, replyForm
from django.core.paginator import Paginator
import pymysql
from decouple import config

# Create your views here.

# MySQL Connection
conn = pymysql.connect(host=config('db_host'), user='sasim', password=config('db_password'), db='sasim', charset='utf8')

# Connection 으로 Cursor 생성
curs = conn.cursor() # curs가 DB fetch 관리


def notice_list(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 페이지
    page = request.GET.get('page', '1')

    # 공지사항 게시글 전부 가져옴
    n_posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    response_date['n_posts'] = n_posts

    # 페이지당 10개씩
    paginator = Paginator(n_posts, 10)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'notice.html', response_date)


def notice_detail(request, pk):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    n_post_detail = get_object_or_404(Post, pk=pk)
    response_date['n_post_detail'] = n_post_detail

    return render(request, 'notice_detail.html', response_date)


def contact_list(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

        response_date['notUser'] = 1

    ####

    # 페이지
    page = request.GET.get('page', '1')

    # 공지사항 게시글 전부 가져옴
    n_contact_posts = Contact_Contact.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    response_date['n_contact_posts'] = n_contact_posts

    # 페이지당 10개씩
    paginator = Paginator(n_contact_posts, 7)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'contact.html', response_date)


def contact_detail(request, pk):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    n_contact_posts_detail = get_object_or_404(Contact_Contact, pk=pk)
    response_date['n_contact_posts_detail'] = n_contact_posts_detail

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account
        response_date['userid'] = userid

        # 작성자 데이터 가져오기
        # curs.execute('select mb_id from board_contact_contact WHERE mb_id = %s', (n_contact_posts_detail.mb_id, ))
        # contact_writer = curs.fetchone()
        #
        # response_date['contact_writer'] = contact_writer[0]


    return render(request, 'contact_detail.html', response_date)
    # return redirect('contact_list')


# 나의 1:1문의 조회
def mypage_contact_list(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    if userid != 'sasim':
        # 해당 이용자가 작성한 게시글만 전부 가져옴
        mypage_contact_list_userid = Contact_Contact.objects.filter(created_date__lte=timezone.now(), mb_id=userid).order_by('-created_date')

        response_date['mypage_contact_list_userid'] = mypage_contact_list_userid

    elif userid == 'sasim':
        # 미답변 게시글만 전부 가져옴
        mypage_contact_list_userid = Contact_Contact.objects.filter(created_date__lte=timezone.now(), reply='').exclude(mb_id='sasim').order_by('-created_date')

        response_date['mypage_contact_list_userid'] = mypage_contact_list_userid


    # 페이지
    page = request.GET.get('page', '1')

    # 공지사항 게시글 전부 가져옴
    # n_contact_posts = Contact_Contact.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    response_date['n_contact_posts'] = mypage_contact_list_userid

    # 페이지당 10개씩
    paginator = Paginator(mypage_contact_list_userid, 7)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    #
    return render(request, 'mypage_contact_list.html', response_date)


#
def post_new(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_post = form.save(commit=False)
            contact_post.mb_id = userid
            contact_post.created_date = timezone.now()
            contact_post.reply = ''
            contact_post.save()

            # return render(request, 'contact_detail.html', response_date)
            return redirect('contact_list')

    else:
        form = ContactForm()
        response_date['form'] = form

    return render(request, 'contact_edit.html', response_date)


def replyContact(request, pk):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ###

    post = get_object_or_404(Contact_Contact, pk=pk)

    if request.method == "POST":
        form = replyForm(request.POST, instance=post)

        if form.is_valid():
            reply_post = form.save(commit=False)
            reply_post.save()

            return redirect('contact_detail', pk=post.pk)

    else:
        form = replyForm(instance=post)
        response_date['form'] = form

    return render(request, 'contact_reply.html', response_date)

