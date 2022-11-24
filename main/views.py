from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from django.utils import timezone
from board.models import Post
from decouple import config


# MySQL Connection
conn = pymysql.connect(host=config('db_host'), user='sasim', password=config('db_password'), db='sasim', charset='utf8')

# Connection 으로 Cursor 생성
curs = conn.cursor() # curs가 DB fetch 관리


# Create your views here.
def index(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    # 공지사항 게시글 전부 가져옴
    # curs.execute('select id, title, text, date_format(created_date, "%Y-%m-%d") from board_post order by id DESC;')
    # n_posts = curs.fetchone()
    n_posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    response_date['n_posts'] = n_posts
    #

    # 식물 신상품 3개 가져옴
    curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table order by pl_id DESC;')
    new_plant = curs.fetchmany(3)

    response_date['new_plant'] = new_plant

    #
    if account:

        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account
        response_date['userid'] = userid
        response_date['username'] = username

        return render(request, 'base.html', response_date)

    return render(request, 'base.html', response_date)
