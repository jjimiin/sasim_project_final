from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from decouple import config

# Create your views here.

# MySQL Connection
conn = pymysql.connect(host=config('db_host'), user='sasim', password=config('db_password'), db='sasim', charset='utf8')

# Connection 으로 Cursor 생성
curs = conn.cursor() # curs가 DB fetch 관리


#
def mypage_main(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    response_date['mypage_main_order_list'] = []

    # 주문 조회 내역 데이터 가져오기
    curs.execute('SELECT * FROM order_list where mb_id=%s order by order_id DESC;', (account[0],))
    mypage_main_order_list1 = curs.fetchmany(3)  # 전부

    if userid != 'sasim':

        if mypage_main_order_list1:
            #
            for list in mypage_main_order_list1:
                response_date['mypage_main_order_list1'] = []

                curs.execute('select * from order_list li join order_items it on li.order_id = it.order_id where li.order_id = %s;', (list[0],))
                order_id_info = curs.fetchone()  # 하나

                #
                curs.execute('select count(*) from order_list li join order_items it on li.order_id = it.order_id where li.order_id = %s;', (list[0],))
                order_id_info_count = curs.fetchone()  # 하나
                ##
                if order_id_info[0] is not None:
                    curs.execute('select * from plant_table where pl_id = %s;', (order_id_info[13],))
                    order_id_info_plant = curs.fetchone()  # 하나

                    response_date['mypage_main_order_list1'].append(list[0])  # 주문 id
                    response_date['mypage_main_order_list1'].append(order_id_info[13])  # 대표 주문 아이템 하나
                    response_date['mypage_main_order_list1'].append(order_id_info_plant[2])  # 대표 주문 아이템 이름 하나
                    response_date['mypage_main_order_list1'].append(order_id_info_plant[10])  # 대표 주문 아이템 사진 하나
                    response_date['mypage_main_order_list1'].append(order_id_info_count[0] - 1)  # 한 주문당 상품 종류 개수 - 1
                    response_date['mypage_main_order_list1'].append(order_id_info[2])  # 총 주문 금액
                    response_date['mypage_main_order_list1'].append(order_id_info[11])  # 주문 방식
                    response_date['mypage_main_order_list1'].append(order_id_info[10])  # 주문 상태
                    response_date['mypage_main_order_list1'].append(order_id_info[9])  # 주문 날짜

                    response_date['mypage_main_order_list'].append(response_date['mypage_main_order_list1'])

                else:
                    response_date['mypage_main_order_list'] = []
            #
        #
        else:
            response_date['mypage_main_order_list'] = []

            response_date['order_null'] = '최근 주문 내역이 없습니다.'
        #
    #

    return render(request, 'mypage_main.html', response_date)


# 주문 완료
def order_success(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    return render(request, 'order_success.html', response_date)


# 주문 완료
def admin_order_check(request, sort):
    response_date = {}

    response_date['sort'] = sort

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    #
    if sort == 1:
        curs.execute('SELECT * FROM order_list where payment = "무통장입금" and order_state = "입금 확인 전" order by order_id DESC;')
        order_list_admin = curs.fetchall()  # 전부

        response_date['order_list_admin'] = order_list_admin
    #

    elif sort == 2:
        curs.execute('SELECT * FROM order_list order by order_id DESC;')
        order_list_admin = curs.fetchall()  # 전부

        response_date['order_list_admin'] = order_list_admin
    #

    #
    #
    if request.method == "POST":
        # 해당하는 주문 id 받아옴
        admin_order_id = request.POST.getlist("admin_order_id")

        # 입금 확인 버튼
        if request.POST["checkBtn"] == '입금 확인':

            for list in admin_order_id:
                # 입금 확인으로 변경
                curs.execute('UPDATE order_list SET order_state = %s where order_id = %s', ('입금 확인', list, ))
                conn.commit()

            return redirect('admin_order_check', sort=sort)
        #

        # 주문 취소 버튼
        elif request.POST["checkBtn"] == '주문 취소':

            for list in admin_order_id:
                # 주문 취소로 변경
                curs.execute('UPDATE order_list SET order_state = %s where order_id = %s', ('주문 취소', list, ))
                conn.commit()

            return redirect('admin_order_check', sort=sort)
        #

        # 환불 완료 버튼
        elif request.POST["checkBtn"] == '환불 완료':

            for list in admin_order_id:
                # 환불 완료로 변경
                curs.execute('UPDATE order_list SET order_state = %s where order_id = %s', ('환불 완료', list, ))
                conn.commit()

            return redirect('admin_order_check', sort=sort)
        #

        # 검색 버튼
        elif request.POST["checkBtn"] == '검색':

            admin_search_mb_id = request.POST["admin_search_mb_id"]

            if sort == 1:
                curs.execute('SELECT * FROM order_list where payment = "무통장입금" and order_state = "입금 확인 전" and mb_id = %s order by order_id DESC;', (admin_search_mb_id, ))
                admin_search_result_mb_id = curs.fetchall()  # 전부

            elif sort == 2:
                curs.execute('SELECT * FROM order_list where mb_id = %s order by order_id DESC;', (admin_search_mb_id, ))
                admin_search_result_mb_id = curs.fetchall()  # 전부


            if admin_search_result_mb_id:
                response_date['order_list_admin'] = admin_search_result_mb_id
            else:
                response_date['result_null'] = '검색 결과가 없습니다.'

            return render(request, 'admin_order_check.html', response_date)
        #

    #
    return render(request, 'admin_order_check.html', response_date)
