from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from decouple import config

# Create your views here.

# MySQL Connection
conn = pymysql.connect(host=config('db_host'), user='sasim', password=config('db_password'), db='sasim', charset='utf8')

# Connection 으로 Cursor 생성
curs = conn.cursor() # curs가 DB fetch 관리


def index(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    return render(request, 'introduction.html', response_date)

