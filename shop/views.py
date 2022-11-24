from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from decouple import config

# Create your views here.

# MySQL Connection
conn = pymysql.connect(host=config('db_host'), user='sasim', password=config('db_password'), db='sasim', charset='utf8')

# Connection 으로 Cursor 생성
curs = conn.cursor() # curs가 DB fetch 관리


# 상품 목록
def plant_list(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 카테고리 위치 확인용
    response_date['category_chk1'] = ['#9AB37D', 'white']

    # 식물 테이블에서 데이터 접근
    curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table order by pl_id DESC;')
    plant_list_all = curs.fetchall() # 전부 가져옴

    # 식물 목록
    response_date['plant_list'] = plant_list_all
    #

    #
    # 식물 목록 pg > 검색
    if request.POST.get("searchBtn") == '검색':
        # 검색 내용 가져옴
        search_content = request.POST["search_content"]
        response_date['search_content'] = search_content

        # 공백으로 문자 자름
        splitted_str = search_content.split()
        # 공백 부분에 '|' 넣기
        joined_str = "|".join(splitted_str)

        # 식물 테이블에서 데이터 접근 / 입력 받은 문자열을 포함하는 식물명 찾기
        curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_name REGEXP %s;', (joined_str,))
        plant_list_all = curs.fetchall() # 전부 가져옴

        # 식물 목록 새로 저장
        response_date['plant_list'] = plant_list_all
    else:
        pass
    #

    #
    # 페이지
    page = request.GET.get('page', '1')

    response_date['n_contact_posts'] = plant_list_all

    # 페이지당 10개씩
    paginator = Paginator(plant_list_all, 9)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'plant_list.html', response_date)


# 관엽
def plant_list_1(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 카테고리 위치 확인용
    response_date['category_chk2'] = ['#9AB37D', 'white']

    # 식물 테이블에서 데이터 접근
    curs.execute('select pl_id, pl_name, FORMAT(pl_price, 0), pl_img from plant_table where pl_category = "관엽" order by pl_id DESC;')
    plant_list_1 = curs.fetchall() # 전부 가져옴

    #
    response_date['plant_list'] = plant_list_1

    #
    # 페이지
    page = request.GET.get('page', '1')

    response_date['n_contact_posts'] = plant_list_1

    # 페이지당 10개씩
    paginator = Paginator(plant_list_1, 9)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'plant_list.html', response_date)


# 다육
def plant_list_2(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 카테고리 위치 확인용
    response_date['category_chk3'] = ['#9AB37D', 'white']

    # 식물 테이블에서 데이터 접근
    curs.execute('select pl_id, pl_name, FORMAT(pl_price, 0), pl_img from plant_table where pl_category = "다육" order by pl_id DESC;')
    plant_list_2 = curs.fetchall() # 전부 가져옴

    #
    response_date['plant_list'] = plant_list_2

    #
    # 페이지
    page = request.GET.get('page', '1')

    response_date['n_contact_posts'] = plant_list_2

    # 페이지당 10개씩
    paginator = Paginator(plant_list_2, 9)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'plant_list.html', response_date)


# 구근
def plant_list_3(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 카테고리 위치 확인용
    response_date['category_chk4'] = ['#9AB37D', 'white']

    # 식물 테이블에서 데이터 접근
    curs.execute('select pl_id, pl_name, FORMAT(pl_price, 0), pl_img from plant_table where pl_category = "구근" order by pl_id DESC;')
    plant_list_3 = curs.fetchall() # 전부 가져옴

    #
    response_date['plant_list'] = plant_list_3

    #
    # 페이지
    page = request.GET.get('page', '1')

    response_date['n_contact_posts'] = plant_list_3

    # 페이지당 10개씩
    paginator = Paginator(plant_list_3, 9)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'plant_list.html', response_date)


# 허브
def plant_list_4(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 카테고리 위치 확인용
    response_date['category_chk5'] = ['#9AB37D', 'white']

    # 식물 테이블에서 데이터 접근
    curs.execute('select pl_id, pl_name, FORMAT(pl_price, 0), pl_img from plant_table where pl_category = "허브" order by pl_id DESC;')
    plant_list_4 = curs.fetchall() # 전부 가져옴

    #
    response_date['plant_list'] = plant_list_4

    #
    # 페이지
    page = request.GET.get('page', '1')

    response_date['n_contact_posts'] = plant_list_4

    # 페이지당 10개씩
    paginator = Paginator(plant_list_4, 9)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'plant_list.html', response_date)


# 선인장
def plant_list_5(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 카테고리 위치 확인용
    response_date['category_chk6'] = ['#9AB37D', 'white']

    # 식물 테이블에서 데이터 접근
    curs.execute('select pl_id, pl_name, FORMAT(pl_price, 0), pl_img from plant_table where pl_category = "선인장" order by pl_id DESC;')
    plant_list_5 = curs.fetchall() # 전부 가져옴

    #
    response_date['plant_list'] = plant_list_5

    #
    # 페이지
    page = request.GET.get('page', '1')

    response_date['n_contact_posts'] = plant_list_5

    # 페이지당 10개씩
    paginator = Paginator(plant_list_5, 9)
    page_obj = paginator.get_page(page)

    response_date['page_obj'] = page_obj

    return render(request, 'plant_list.html', response_date)


# 상품 상세
def plant_detail(request, id):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 식물 테이블에서 데이터 접근
    curs.execute('SELECT pl_id, pl_category, pl_name, pl_animal, pl_effect, pl_place, pl_size, pl_time, FORMAT(pl_price, 0), pl_stock, pl_img, pl_detail FROM plant_table where pl_id = %s;', id)
    plant_info = curs.fetchone() # 하나 가져옴

    #
    response_date['plant_info'] = plant_info

    pl_d_stock = int(plant_info[9])
    response_date['pl_d_stock'] = pl_d_stock

   # 반려동물
    if plant_info[3] == '5':
        response_date['plant_animal'] = '반려동물안심'
    elif plant_info[3] == '4' or plant_info[3] == '3':
        response_date['plant_animal'] = '반려동물주의'
    else:
        response_date['plant_animal'] = '반려동물위험'

    # 효과
    if plant_info[4][0] == '3':
        response_date['plant_effect1'] = '공기정화'
        if plant_info[4][1] == '3':
            response_date['plant_effect2'] = '실내가습'
        elif plant_info[4][2] == '3':
            response_date['plant_effect2'] = '벌레퇴치'
            
    elif plant_info[4][1] == '3':
        response_date['plant_effect1'] = '실내가습'
        if plant_info[4][2] == '3':
            response_date['plant_effect2'] = '벌레퇴치'
            
    elif plant_info[4][2] == '3':
        response_date['plant_effect1'] = '벌레퇴치'

    else:
        response_date['plant_effect1'] = ''

    # 크기
    if plant_info[6] == '5':
        response_date['plant_size'] = '매우큼'
    elif plant_info[6] == '4':
        response_date['plant_size'] = '큼'
    elif plant_info[6] == '3':
        response_date['plant_size'] = '보통'
    elif plant_info[6] == '2':
        response_date['plant_size'] = '작음'
    elif plant_info[6] == '1':
        response_date['plant_size'] = '매우작음'

    # 시간
    if plant_info[7] == '1':
        response_date['plant_time'] = '매우잘견딤'
    elif plant_info[7] == '2':
        response_date['plant_time'] = '잘견딤'
    elif plant_info[7] == '3':
        response_date['plant_time'] = '관심조금'
    elif plant_info[7] == '4':
        response_date['plant_time'] = '관심필요'
    else:
        response_date['plant_time'] = '매우관심필요'

    return render(request, 'plant_detail.html', response_date)


# 결제
def plant_buy(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 식물 상세 form
    if request.method == "POST":

        # 상품 상세 pg > 구매
        if request.POST["sort"] == '구매':

            # 구매 구분용
            buy_sort = request.POST["sort"]
            response_date['buy_sort'] = buy_sort
            ###

            # 상품 정보 가져옴 / 식물 id
            plant_buy_info_id = request.POST.getlist("plant_buy_info_id")
            # 해당 id의 식물 데이터 가져오기
            curs.execute('select * from plant_table where pl_id = %s;', (plant_buy_info_id,))
            plant_buy_info = curs.fetchone()  # 하나

            response_date['plant_buy_info_id'] = plant_buy_info_id
            response_date['plant_buy_info'] = plant_buy_info

            # 수량 가져옴
            buy_amount = int(request.POST["buy_amount"])
            response_date['buy_amount'] = buy_amount

            #
            # 장바구니 버튼 클릭 시:
            if request.POST["buyButton"] == '장바구니':

                # 이미 장바구니에 있는 상품인지 확인
                curs.execute('select * from cart where mb_id = %s and pl_id = %s;', (userid, plant_buy_info[0],))
                cart_already = curs.fetchone() # 하나

                # 이미 있는 상품일 경우 / 기존 수량에 추가로 더함
                if cart_already:
                    total_amount = int(cart_already[2]) + buy_amount # 수량 총합
                    # db 갱신
                    curs.execute('UPDATE cart SET amount = %s, addCart_date = %s where mb_id = %s and pl_id = %s;', (total_amount, timezone.now(), userid, plant_buy_info[0],))
                    conn.commit()

                # 없는 상품일 경우 / 장바구니에 새로 추가
                else:
                    # 장바구니에 데이터 추가
                    curs.execute('INSERT INTO cart VALUES (%s, %s, %s, %s, %s);', (userid, plant_buy_info[0], buy_amount, plant_buy_info[8], datetime.now(),))
                    conn.commit()

                return redirect('plant_detail', id=plant_buy_info_id[0])
            # btn = '장바구니' if문 종료
        # sort = '구매' if문 종료

        #
        # 장바구니 pg > 구매
        elif request.POST["sort"] == '장바구니':

            # 구매 구분용
            buy_sort = request.POST["sort"]
            response_date['buy_sort'] = buy_sort
            ###

            # 장바구니의 체크된 상품 id 가져옴
            # cart_chk = request.POST.getlist("cart_chk")
            cart_chk_x = request.POST.getlist("cart_chk")

            cart_chk = []
            x = 0
            for x in cart_chk_x:
                split_x = x.split(',')
                cart_chk.append(split_x[0][2:-1])


            # 선택 삭제 버튼 클릭 시:
            if request.POST["buyButton"] == '선택 삭제':
                for n in cart_chk:
                    # 해당 상품 삭제
                    curs.execute('delete from cart where mb_id = %s and pl_id = %s;', (userid, n))
                    conn.commit()

                return redirect('plant_cart')
            #

            # 장바구니 비우기 버튼 클릭 시:
            elif request.POST["buyButton"] == '장바구니 비우기':
                # 모든 상품 삭제
                curs.execute('delete from cart where mb_id = %s;', (userid,))
                conn.commit()

                return redirect('plant_cart')
            #

            # 선택 상품 주문 버튼 클릭 시:
            elif request.POST["buyButton"] == '선택 상품 주문':

                response_date['plant_buy_info_id'] = cart_chk

                #
                phone1_list = ['010', '02', '031', '033', '041', '042', '043', '044', '051', '053', '054', '055', '062', '063', '064', '070']

                phone1_chk = []
                for n in range(len(phone1_list)):
                    phone1_chk.append("")
                    n += 1

                phone1_chk_nm = phone1_list.index(account[8])
                phone1_chk[phone1_chk_nm] = 'selected'

                response_date['phone1_chk'] = phone1_chk
                #

                # 선택한 상품이 없을 경우: 현재 화면 유지
                if not cart_chk:
                    return redirect('plant_cart')

                # return render(request, 'plant_buy.html', response_date)
            #

            # 전체 주문 주문 버튼 클릭 시:
            elif request.POST["buyButton"] == '전체 상품 주문':
                curs.execute('select * from cart where mb_id = %s;', (userid,))
                plant_buy_info_id = curs.fetchall()  # 전부

                response_date['plant_buy_info_id'] = []

                # 장바구니에 상품이 없을 때: 현재 화면 유지
                if not plant_buy_info_id:
                    return redirect('plant_cart')

                # 장바구니에 상품이 있을 때: 결제 화면으로 이동
                else:
                    # 주문할 식물 id 전부 리스트에 넣어서 넘김
                    i = 0
                    for n in plant_buy_info_id:
                        response_date['plant_buy_info_id'].append(plant_buy_info_id[i][1])
                        i += 1

                #
                phone1_list = ['010', '02', '031', '033', '041', '042', '043', '044', '051', '053', '054', '055', '062',
                               '063', '064', '070']

                phone1_chk = []
                for n in range(len(phone1_list)):
                    phone1_chk.append("")
                    n += 1

                phone1_chk_nm = phone1_list.index(account[8])
                phone1_chk[phone1_chk_nm] = 'selected'

                response_date['phone1_chk'] = phone1_chk
                #
            #

            ####
            # 구매하는 상품 묶음
            response_date['plant_buy_list'] = []
            # 총 상품 금액
            total_price = 0

            #
            # 체크된 상품 id 정보 가져오기
            for id_list in response_date['plant_buy_info_id']:
                # 필요한 정보값 들어간 구매 상품 정보 생성
                response_date['plant_buy_info'] = []

                # 식물 테이블 해당 id의 식물 데이터 가져오기
                curs.execute('select * from plant_table where pl_id = %s;', (id_list,))
                plant_buy_info = curs.fetchone()  # 하나

                # 장바구니 테이블에서 수량 데이터 가져오기
                curs.execute('select * from cart where pl_id = %s and mb_id = %s;', (id_list, userid,))
                plant_buy_info_cart = curs.fetchone()  # 하나

                response_date['plant_buy_info'].append(plant_buy_info[0])  # 식물id
                response_date['plant_buy_info'].append(plant_buy_info[10])  # 이미지
                response_date['plant_buy_info'].append(plant_buy_info[2])  # 식물명
                response_date['plant_buy_info'].append(format(int(plant_buy_info[8]), ',d'))  # 단가
                response_date['plant_buy_info'].append(plant_buy_info_cart[2])  # 수량
                # 단가*수량
                plant_total_cost = int(plant_buy_info[8]) * int(plant_buy_info_cart[2])
                response_date['plant_buy_info'].append(format(int(plant_total_cost), ',d'))

                response_date['plant_buy_info'].append(int(plant_buy_info[8]))  # 단가 (천단위 , X)
                response_date['plant_buy_info'].append(int(plant_total_cost)) # 단가*수량 (천단위 , X)


                # 구매하는 상품 묶음에 추가
                response_date['plant_buy_list'].append(response_date['plant_buy_info'])

                total_price += plant_total_cost

            #

            # 주문 상품들 총 금액 (배송비 포함x)
            response_date['plant_buy_info_total_price'] = format(int(total_price), ',d')

            # 배송비 포함 여부 계산
            if total_price < 20000:
                response_date['plant_buy_info_ship'] = '2,000'
                response_date['plant_buy_info_ship_total_price'] = format((int(total_price) + 2000), ',d')
                response_date['plant_buy_info_ship_total_price_x'] = int(total_price) + 2000
            else:
                response_date['plant_buy_info_ship'] = 0
                response_date['plant_buy_info_ship_total_price'] = format(int(total_price), ',d')
                response_date['plant_buy_info_ship_total_price_x'] = int(total_price)

            ####
            return render(request, 'plant_buy.html', response_date)
        # sort = '장바구니' if문 종료
    # Post if문 종료

    #
    # 결제 페이지 작업 / 상세>결제
    if buy_sort == '구매':

        # 필요한 정보값 들어간 구매 상품 정보 생성
        response_date['plant_buy_info'] = []
        response_date['plant_buy_info'].append(plant_buy_info[0]) # 식물id
        response_date['plant_buy_info'].append(plant_buy_info[10]) # 이미지
        response_date['plant_buy_info'].append(plant_buy_info[2]) # 식물명
        response_date['plant_buy_info'].append(format(int(plant_buy_info[8]), ',d')) # 단가
        response_date['plant_buy_info'].append(buy_amount) # 수량
        # 단가*수량
        plant_buy_info_price_x_amount = int(plant_buy_info[8]) * buy_amount
        response_date['plant_buy_info'].append(format(int(plant_buy_info_price_x_amount), ',d')) # 단가*수량

        response_date['plant_buy_info'].append(int(plant_buy_info[8]))  # 단가 (천단위 , X)
        response_date['plant_buy_info'].append(int(plant_buy_info_price_x_amount)) # 단가*수량 (천단위 , X)

        # 구매하는 상품 묶음
        response_date['plant_buy_list'] = []
        response_date['plant_buy_list'].append(response_date['plant_buy_info'])

        #
        # 상세>구매 1개이르모 총 상품 금액 = plant_buy_info_price_x_amount
        # 단가*수량 금액
        response_date['plant_buy_info_total_price'] = format(int(plant_buy_info_price_x_amount), ',d')

        # 배송비 포함 여부 계산
        if plant_buy_info_price_x_amount < 20000:
            response_date['plant_buy_info_ship'] = '2,000'
            response_date['plant_buy_info_ship_total_price'] = format((int(plant_buy_info_price_x_amount) + 2000), ',d')
            response_date['plant_buy_info_ship_total_price_x'] = int(plant_buy_info_price_x_amount) + 2000
        else:
            response_date['plant_buy_info_ship'] = 0
            response_date['plant_buy_info_ship_total_price'] = format(int(plant_buy_info_price_x_amount), ',d')
            response_date['plant_buy_info_ship_total_price_x'] = int(plant_buy_info_price_x_amount)

        #
        phone1_list = ['010', '02', '031', '033', '041', '042', '043', '044', '051', '053', '054', '055', '062', '063', '064', '070']

        phone1_chk = []
        for n in range(len(phone1_list)):
            phone1_chk.append("")
            n += 1

        phone1_chk_nm = phone1_list.index(account[8])
        phone1_chk[phone1_chk_nm] = 'selected'

        response_date['phone1_chk'] = phone1_chk
        #

    # sort='구매' if문 끝


    #
    # 결제 페이지 작업 / 장바구니>결제
    # elif buy_sort == '장바구니':
    else:

        # 구매하는 상품 묶음
        response_date['plant_buy_list'] = []
        # 총 상품 금액
        total_price = 0

        #
        # 체크된 상품 id 정보 가져오기
        for id_list in plant_buy_info_id:
            # 필요한 정보값 들어간 구매 상품 정보 생성
            response_date['plant_buy_info'] = []

            # 식물 테이블 해당 id의 식물 데이터 가져오기
            curs.execute('select * from plant_table where pl_id = %s;', (id_list,))
            plant_buy_info = curs.fetchone()  # 하나

            # 장바구니 테이블에서 수량 데이터 가져오기
            curs.execute('select * from cart where pl_id = %s and mb_id = %s;', (id_list, userid,))
            plant_buy_info_cart = curs.fetchone()  # 하나

            response_date['plant_buy_info'].append(plant_buy_info[0]) # 식물id
            response_date['plant_buy_info'].append(plant_buy_info[10]) # 이미지
            response_date['plant_buy_info'].append(plant_buy_info[2]) # 식물명
            response_date['plant_buy_info'].append(plant_buy_info[8]) # 단가
            response_date['plant_buy_info'].append(plant_buy_info_cart[2]) # 수량
            response_date['plant_buy_info'].append(plant_buy_info_cart[3]) # 단가*수량

            # 구매하는 상품 묶음에 추가
            response_date['plant_buy_list'].append(response_date['plant_buy_info'])

            total_price += int(plant_buy_info_cart[3])
        #

        # 주문 상품들 총 금액 (배송비 포함x)
        response_date['plant_buy_info_total_price'] = format(int(total_price), ',d')

        # 배송비 포함 여부 계산
        if total_price < 20000:
            response_date['plant_buy_info_ship'] = '2,000'
            response_date['plant_buy_info_ship_total_price'] = format((int(total_price) + 2000), ',d')
            response_date['plant_buy_info_ship_total_price_x'] = int(total_price) + 2000
        else:
            response_date['plant_buy_info_ship'] = 0
            response_date['plant_buy_info_ship_total_price'] = format(int(total_price), ',d')
            response_date['plant_buy_info_ship_total_price_x'] = int(total_price)

    # sort='장바구니' if문 끝

    return render(request, 'plant_buy.html', response_date)


# 장바구니
def plant_cart(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 해당 회원의 장바구니 데이터 가져오기
    curs.execute('select mb_id, pl.pl_id, pl_name, amount, price, pl_img, pl_stock, addCart_date, amount*price from plant_table pl join cart c on pl.pl_id = c.pl_id where mb_id = %s;', (userid,))
    cart_list = curs.fetchall()  # 전체
    #

    #

    #
    # 장바구니에 넣은지 7일이 지난 상품 삭제하기
    for n in cart_list:
        # 장바구니 넣은지 얼마나 지났는지 계산
        time_c = n[7] - timezone.now().date()

        # 오늘 넣은 건 패스
        if (str(time_c)) == '0:00:00':
            pass

        # 넣은지 하루가 지난 것들
        else:
            # 숫자 있는 부분만 잘라서 time_c_day에 저장
            time_c_day = int(((str(time_c)).split(maxsplit=1))[0])

            # 넣은지 일주일이 지났을 경우
            if time_c_day < -7:
                # 장바구니에서 해당 데이터 삭제
                curs.execute('delete from cart where mb_id = %s and pl_id = %s;', (userid, n[1], ))
                conn.commit()
    # for문 끝.

    #
    # 품절된 상품 삭제하기
    for n in cart_list:
        curs.execute('select pl_id, pl_name, pl_stock from plant_table where pl_id = %s;', (n[1],))
        check_stock_cart = curs.fetchone()  # 1

        # 재고가 0인 상품일 때
        if int(check_stock_cart[2]) == 0:
            # 장바구니에서 해당 데이터 삭제
            curs.execute('delete from cart where mb_id = %s and pl_id = %s;', (userid, n[1], ))
            conn.commit()
    # for문 끝.

    # 해당 회원의 장바구니 데이터 *다시 가져오기
    curs.execute('select mb_id, pl.pl_id, pl_name, amount, FORMAT(price, 0), pl_img, pl_stock, addCart_date, FORMAT(amount*price, 0), amount*price from plant_table pl join cart c on pl.pl_id = c.pl_id where mb_id = %s;', (userid,))
    cart_list = curs.fetchall()  # 전체

    #
    cart_list_final = []

    cart_list = list(cart_list)
    for a in cart_list:
        a = list(a)
        a.append([a[1], a[9]])
        cart_list_final.append(a)
    #

    #
    response_date['cart_list'] = cart_list
    response_date['cart_list_final'] = cart_list_final
    response_date['cart_total_price'] = 0

    # 전체 금액 계산
    curs.execute('select mb_id, sum(total_price) from (select mb_id, amount*price as total_price from plant_table pl join cart c on pl.pl_id = c.pl_id) t where t.mb_id = %s group by t.mb_id;', (userid,))
    cart_total_price = curs.fetchone()  # 하나

    # 장바구니에 상품이 없을 때
    if not cart_total_price:
        response_date['cart_total_price'] = 0
        response_date['shipping_cost'] = 0
        response_date['cart_total_price_shipping'] = 0

    # 장바구니에 상품이 있을 때
    else:
        response_date['cart_total_price'] = format(int(cart_total_price[1]), ',d')

        if cart_total_price[1] >= 20000:
            response_date['shipping_cost'] = 0
            response_date['cart_total_price_shipping'] = format(int(cart_total_price[1]), ',d')
        else:
            response_date['shipping_cost'] = '2,000'
            response_date['cart_total_price_shipping'] = format((int(cart_total_price[1]) + 2000), ',d')

    #

    return render(request, 'plant_cart.html', response_date)


# 주문
def plant_order(request):
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

        order_plant_list = request.POST.getlist("order_plant_list")
        order_plant_amount = request.POST.getlist("order_plant_amount")
        order_plant_price = request.POST.getlist("order_plant_price")

        name = request.POST["name"]
        tel1 = request.POST["tel1"]
        tel2 = request.POST["tel2"]
        tel3 = request.POST["tel3"]
        postcode = request.POST["postcode"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        orderMsg = request.POST["orderMsg"]
        buy_sort = request.POST["buy_sort"]

        tel = tel1 + '-' + tel2 + '-' + tel3

        order_total_price = request.POST["order_total_price"]

        payment = request.POST["Payment"]

        response_date['order_plant_list'] = order_plant_list
        response_date['payment'] = payment

        #
        if payment == '무통장입금':
            # 주문 테이블에 데이터 추가
            curs.execute('INSERT INTO order_list VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', ('', userid, order_total_price, name, tel, postcode, address1, address2, orderMsg, datetime.now(), '입금 확인 전', payment))
            conn.commit()
        #

        # 주문 테이블에서 주문 id 가져옴
        curs.execute('SELECT order_id FROM order_list where mb_id = %s order by order_id DESC;', (userid,))
        order_id = curs.fetchone()  # 하나
        response_date['order_id'] = order_id

        #
        i = 0
        for list in order_plant_list:

            # 주문 아이템 테이블에 주문한 식물 정보 저장
            curs.execute('INSERT INTO order_items VALUES (%s, %s, %s, %s);', (order_id, list, order_plant_price[i], order_plant_amount[i], ))
            conn.commit()

            # 식물 테이블에서 주문한 식물들의 수량 수정 작업
            # 기존 수량 데이터를 가져옴
            curs.execute('SELECT pl_stock FROM plant_table where pl_id = %s', (list,))
            order_amount_modify = curs.fetchone()  # 하나
            # 수량 수정 / (기존 수량 - 주문 수량)
            curs.execute('UPDATE plant_table SET pl_stock = %s where pl_id = %s', ((int(order_amount_modify[0]) - int(order_plant_amount[i])), list, ))
            conn.commit()

            i += 1
        #

        #
        if buy_sort == '장바구니':
            # 장바구니에서 주문한 상품 삭제
            for list in order_plant_list:
                curs.execute('delete from cart where mb_id = %s and pl_id = %s;', (userid, list, ))
                conn.commit()
            #
        #

        return redirect('order_success')

    # POST if문 끝

    return render(request, 'plant_order.html', response_date)


# 주문 조회
def confirm_order(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    response_date['order_list'] = []

    # 주문 테이블에서 해당 회원의 주문 기록 가져옴
    curs.execute('SELECT * FROM order_list where mb_id = %s order by order_id DESC;', (userid,))
    order_id = curs.fetchall()  # 전부

    if order_id:
        #
        for list in order_id:
            response_date['order_id_list'] = []

            curs.execute('select * from order_list li join order_items it on li.order_id = it.order_id where li.order_id = %s;', (list[0],))
            order_id_info = curs.fetchone()  # 하나
            #
            curs.execute('select count(*) from order_list li join order_items it on li.order_id = it.order_id where li.order_id = %s;', (list[0],))
            order_id_info_count = curs.fetchone()  # 하나
            ##
            curs.execute('select * from plant_table where pl_id = %s;', (order_id_info[13],))
            order_id_info_plant = curs.fetchone()  # 하나

            response_date['order_id_list'].append(list[0]) # 주문 id
            response_date['order_id_list'].append(order_id_info[13]) # 대표 주문 아이템 하나
            response_date['order_id_list'].append(order_id_info_plant[2]) # 대표 주문 아이템 이름 하나
            response_date['order_id_list'].append(order_id_info_plant[10]) # 대표 주문 아이템 사진 하나
            response_date['order_id_list'].append(order_id_info_count[0] - 1) # 한 주문당 상품 종류 개수 - 1
            response_date['order_id_list'].append(format(int(order_id_info[2]), ',d')) # 총 주문 금액
            response_date['order_id_list'].append(order_id_info[11]) # 주문 방식
            response_date['order_id_list'].append(order_id_info[10]) # 주문 상태
            response_date['order_id_list'].append(order_id_info[9]) # 주문 날짜

            response_date['order_list'].append(response_date['order_id_list'])
        #
    #
    else:
        response_date['order_id_list'] = []

        response_date['order_null'] = '주문 내역이 없습니다.'

    #
    return render(request, 'confirm_order.html', response_date)


# 주문 상세
def order_detail(request, id):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    #
    curs.execute('select a.order_id, mb_id, a.pl_id, pl_name, pl_img, FORMAT(a.pl_price, 0), pl_amount, FORMAT((a.pl_price*pl_amount), 0), total_price, order_name, order_phone, order_postcode, order_address, order_address_detail, order_msg, order_date, order_state, payment from (select li.order_id, mb_id, pl_id, pl_price, pl_amount, total_price, order_name, order_phone, order_postcode, order_address, order_address_detail, order_msg, order_date, order_state, payment from order_list li join order_items it on li.order_id = it.order_id where li.order_id = %s) a join plant_table pl on a.pl_id = pl.pl_id;', (id,))
    order_list_detail = curs.fetchall()  # 전부

    #
    curs.execute('select FORMAT((sum(a.pl_price*pl_amount)), 0), FORMAT((total_price-sum(a.pl_price*pl_amount)), 0), FORMAT(total_price, 0) from (select li.order_id, mb_id, pl_id, pl_price, pl_amount, total_price, order_name, order_phone, order_postcode, order_address, order_address_detail, order_msg, order_date, order_state, payment from order_list li join order_items it on li.order_id = it.order_id where li.order_id = %s) a join plant_table pl on a.pl_id = pl.pl_id group by a.order_id;', (id,))
    order_list_detail_cost = curs.fetchone()  # 전부

    response_date['order_list_detail'] = order_list_detail
    response_date['order_list_detail_cost'] = order_list_detail_cost

    #
    return render(request, 'order_detail.html', response_date)


# 주문 취소
def cancel_order(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 구매 구분용
    order_id_check = request.POST["order_id_check"]
    response_date['order_id_check'] = order_id_check

    curs.execute('select * from order_list where order_id = %s;', (order_id_check,))
    order_check = curs.fetchone()  # 하나

    if order_check[10] != '주문 취소':
        # db 갱신 / 주문 취소로 변경
        curs.execute('UPDATE order_list SET order_state = "주문 취소" where order_id = %s;', (order_id_check, ))
        conn.commit()

        # db 갱신 / 취소 수량 다시 추가하기
        curs.execute('select * from order_items where order_id = %s;', (order_id_check, ))
        addStock = curs.fetchall()  # 하나

        for stock in addStock:
            curs.execute('select pl_stock from plant_table where pl_id = %s;', (stock[1], ))
            plant_addStock = curs.fetchone()  # 하나

            reStock = int(plant_addStock[0]) + int(stock[3])

            curs.execute('UPDATE plant_table SET pl_stock = %s where pl_id = %s;', (reStock, stock[1], ))
            conn.commit()


        return redirect('order_detail', id=order_id_check)

    #
    return render(request, 'order_cancel.html')


# 주문 조회
def statsCheck(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    datetimeStr = str(datetime.now().date())
    response_date['datetimeStr'] = datetimeStr[0:7]
    response_date['datetimeYear'] = datetimeStr[0:4]
    response_date['datetimeMonth'] = datetimeStr[5:7]

    datetimeA = datetime.now().date()
    datetimeB = datetimeA - timedelta(days=30)
    datetimeC = datetimeA - timedelta(days=60)

    dateformat = "%Y-%m-%d"
    tmpA = datetimeA.strftime(dateformat)
    tmpB = datetimeB.strftime(dateformat)
    response_date['tmpA'] = tmpA
    response_date['tmpB'] = tmpB

    dateformat = "%Y-%m"
    nowMonth = datetimeA.strftime(dateformat)
    prevMonth = datetimeB.strftime(dateformat)
    prevMonth2 = datetimeC.strftime(dateformat)
    response_date['nowMonth'] = nowMonth
    response_date['prevMonth'] = prevMonth
    response_date['prevMonth2'] = prevMonth2

    ### 누적 판매량 ###
    # 상품 판매 통계
    # 상품당 판매 개수 총합 가져옴
    curs.execute('select pl_id, sum(pl_amount) from (select oi.order_id, pl_id, pl_amount, order_state from order_items oi join order_list ol on oi.order_id = ol.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전") g group by g.pl_id order by sum(pl_amount) DESC;')
    total_sell_rank_mysql = curs.fetchall()  # 전부

    #
    total_sell_rank_list = []
    total_sell_rank_list_l = []
    j = -1
    rank = 1
    #
    for n in total_sell_rank_mysql:
        #
        curs.execute('select pl_id, pl_name, FORMAT(pl_price, 0), pl_img from plant_table where pl_id = %s;', (n[0], ))
        total_sell_rank_append = curs.fetchone()  # 하나

        #
        for i in range(len(total_sell_rank_append)):
            total_sell_rank_list_l.append(total_sell_rank_append[i])
            i += 1

        total_sell_rank_list_l.append(n[1])  # 판매량

        # 순위 계산
        if j != -1:
            if total_sell_rank_mysql[j][1] == n[1]:
                rank -= 1
                total_sell_rank_list_l.append(rank)  # 순위
                rank += 2

            else:
                total_sell_rank_list_l.append(rank)  # 순위
                rank += 1

        else:
            total_sell_rank_list_l.append(rank)  # 순위
            rank += 1
            j += 1

        total_sell_rank_list.append(total_sell_rank_list_l)
        total_sell_rank_list_l = []

    total_sell_rank_list = total_sell_rank_list[0:3]
    response_date['total_sell_rank_list'] = total_sell_rank_list
    response_date['total_sell_rank_list_l'] = total_sell_rank_list_l
    ######


    ### 최근 일주일 판매량 ###
    # mysql
    curs.execute('select a.pl_id, sum_a, pl_name, pl_img from (select pl_id, sum(pl_amount) as sum_a from (select oi.order_id, pl_id, pl_amount, order_state from order_items oi join order_list ol on oi.order_id = ol.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and order_date BETWEEN DATE_ADD(%s,INTERVAL -1 WEEK ) AND %s) g group by g.pl_id order by sum(pl_amount) DESC) a join plant_table b on a.pl_id = b.pl_id;', (datetime.now(), datetime.now(),))
    week_sell_rank_mysql = curs.fetchall()  # 전부

    week_sell_rank_list = []
    week_sell_rank_list_l = []
    j = -1
    rank = 1
    for list in week_sell_rank_mysql:
        for l in list:
            week_sell_rank_list_l.append(l)

        # 순위 계산
        if j != -1:
            if week_sell_rank_mysql[j][1] == list[1]:
                rank -= 1
                week_sell_rank_list_l.append(rank)  # 순위
                rank += 2

            else:
                week_sell_rank_list_l.append(rank)  # 순위
                rank += 1

        else:
            week_sell_rank_list_l.append(rank)  # 순위
            rank += 1
            j += 1

        week_sell_rank_list.append(week_sell_rank_list_l)
        week_sell_rank_list_l = []

    response_date['week_sell_rank_list'] = week_sell_rank_list[:3]
    ######


    ### 이번달 회원별 구매 총액 ###
    # mysql

    curs.execute('SELECT mb_id, FORMAT(sum(total_price), 0) FROM (SELECT ol.order_id, mb_id, total_price, order_date FROM order_list ol join order_items oi on ol.order_id = oi.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) group by ol.order_id) a WHERE mb_id != "sasim" group by a.mb_id order by sum(total_price) DESC;', (datetimeStr[0:7], ))
    user_buy_amount_rank_mysql = curs.fetchall()  # 전부

    user_buy_amount_rank_list = []
    user_buy_amount_rank_l = []
    j = -1
    rank = 1
    for list in user_buy_amount_rank_mysql:
        for l in list:
            user_buy_amount_rank_l.append(l)

        # 순위 계산
        if j != -1:
            if user_buy_amount_rank_mysql[j][1] == list[1]:
                rank -= 1
                user_buy_amount_rank_l.append(rank)  # 순위
                rank += 2

            else:
                user_buy_amount_rank_l.append(rank)  # 순위
                rank += 1

        else:
            user_buy_amount_rank_l.append(rank)  # 순위
            rank += 1
            j += 1

        user_buy_amount_rank_list.append(user_buy_amount_rank_l)
        user_buy_amount_rank_l = []

    response_date['user_buy_amount_rank_list'] = user_buy_amount_rank_list[:3]
    ######


    ### 최근 한달 매출액 ###
    # mysql
    curs.execute('SELECT FORMAT(sum(g.total_price), 0), DATE_FORMAT(g.order_date, "%%Y.%%m.%%d") FROM (SELECT total_price, order_date FROM order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and order_date BETWEEN DATE_ADD(%s,INTERVAL -1 MONTH ) AND %s) g group by g.order_date order by g.order_date DESC;', (datetime.now(), datetime.now(),))
    month_total_amount_mysql = curs.fetchall()  # 전부

    response_date['month_total_amount_mysql'] = month_total_amount_mysql[:3]
    ######


    ### 월별 매출액 ###
    # mysql
    curs.execute('select %s, FORMAT(sum(total_price), 0) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (nowMonth[0:4]+'.'+nowMonth[5:7], nowMonth, ))
    month_sales_mysql_1 = curs.fetchone()  # 전부
    curs.execute('select %s, FORMAT(sum(total_price), 0) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (prevMonth[0:4]+'.'+prevMonth[5:7], prevMonth, ))
    month_sales_mysql_2 = curs.fetchone()  # 전부
    curs.execute('select %s, FORMAT(sum(total_price), 0) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (prevMonth2[0:4]+'.'+prevMonth2[5:7], prevMonth2, ))
    month_sales_mysql_3 = curs.fetchone()  # 전부

    mysql_l = [month_sales_mysql_1, month_sales_mysql_2, month_sales_mysql_3]

    month_sales_list = []
    month_sales_list_l = []

    for list in mysql_l:
        for x in list:
            month_sales_list_l.append(x)

        month_sales_list.append(month_sales_list_l)
        month_sales_list_l = []

    response_date['month_sales_list'] = month_sales_list
    ######


    ### 회원 재구매율 ###
    # mysql
    curs.execute('select g.order_count, count(mb_id) from (select mb_id, count(order_id) as order_count from order_list where mb_id != "sasim" and order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" group by mb_id order by order_id desc) g group by g.order_count;')
    user_rebuy_mysql = curs.fetchall()  # 전부

    ##
    # 그래프 그리기
    # x축, y축 값 생성
    idx = ['1건(재구매x)', '2건 이상', '10건 이상']
    v = [0, ]
    sum1 = [0, ]
    sum2 = [0, ]

    for i in user_rebuy_mysql:
        if i[0] == 1:
            v[0] = i[1]
        elif i[0] >= 2 and i[0] < 10:
            sum1.append(i[1])
        elif i[0] >= 10:
            sum2.append(i[1])

    v.append(sum(sum1))
    v.append(sum(sum2))

    user_amount = sum(v)

    user_rebuy_list = []
    user_rebuy_list_l =[]

    for a in range(0, 3):
        user_rebuy_list_l.append(idx[a])
        user_rebuy_list_l.append(round((v[a]/user_amount), 3)*100)

        user_rebuy_list.append(user_rebuy_list_l)
        user_rebuy_list_l =[]

    response_date['user_rebuy_list'] = user_rebuy_list
    ######

    return render(request, 'statsCheck.html', response_date)


# 주문 조회
def statsCheck_detail(request, id):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####
    response_date['id'] = id

    plt.switch_backend('agg')
    plt.rcParams["font.family"] = 'Malgun Gothic'

    if id == 1:
        ### 누적 판매량 ###
        # 상품 판매 통계
        # 상품당 판매 개수 총합 가져옴
        curs.execute('select pl_id, sum(pl_amount) from (select oi.order_id, pl_id, pl_amount, order_state from order_items oi join order_list ol on oi.order_id = ol.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전") g group by g.pl_id order by sum(pl_amount) DESC;')
        total_sell_rank_mysql = curs.fetchall()  # 전부

        ##
        # 그래프 그리기
        # csv 파일 변환
        query = 'select pl.pl_name, sum(pl_amount) from (select oi.order_id, pl_id, pl_amount, order_state from order_items oi join order_list ol on oi.order_id = ol.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전") g join plant_table pl on g.pl_id = pl.pl_id group by g.pl_id order by sum(pl_amount) DESC'

        df = pd.read_sql_query(query, conn)
        df.to_csv(r'shop/csv/totalSellPlant.csv', index=False)

        #
        plt.style.use('ggplot')
        df = pd.read_csv('shop/csv/totalSellPlant.csv', encoding='utf-8').head(30)

        plt.ticklabel_format(axis="y", style="plain")

        for bar in plt.bar(df['pl_name'], df['sum(pl_amount)'], color='mediumaquamarine', width=0.5).patches:
            if bar.get_height() > 10:
                bar.set_facecolor('mediumseagreen')

        plt.bar(df['pl_name'][:3], df['sum(pl_amount)'][:3], width=0.5, color='limegreen')

        plt.title('누적 판매량')
        plt.xlabel('< 식물명 >', fontsize=12)
        plt.ylabel('< 누적 판매량 >', fontsize=12)
        plt.rc('xtick', labelsize=7)
        plt.rc('ytick', labelsize=12)
        plt.xticks(rotation='vertical')

        plt.savefig('static/img/graph/totalSellPlant.png', bbox_inches="tight")
        plt.close('all')

        response_date['img_graph'] = 'img/graph/totalSellPlant.png'
        ##

        #
        total_sell_rank_list = []
        total_sell_rank_list_l = []
        #
        for n in total_sell_rank_mysql:
            #
            curs.execute('select pl_id, pl_name, FORMAT(pl_price, 0), pl_img from plant_table where pl_id = %s;', (n[0], ))
            total_sell_rank_append = curs.fetchone()  # 하나

            #
            for i in range(len(total_sell_rank_append)):
                total_sell_rank_list_l.append(total_sell_rank_append[i])
                i += 1

            total_sell_rank_list_l.append(n[1])  # 판매량

            total_sell_rank_list.append(total_sell_rank_list_l)
            total_sell_rank_list_l = []

        total_sell_rank_list = total_sell_rank_list
        response_date['total_sell_rank_list'] = total_sell_rank_list
        ######

    #
    elif id == 2:

        ### 최근 일주일 판매량 ###
        # mysql
        curs.execute('select a.pl_id, sum_a, pl_name, pl_img, pl_price from (select pl_id, sum(pl_amount) as sum_a from (select oi.order_id, pl_id, pl_amount, order_state from order_items oi join order_list ol on oi.order_id = ol.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and order_date BETWEEN DATE_ADD(NOW(),INTERVAL "-7 9" day_hour) AND DATE_ADD(NOW(),INTERVAL 9 hour)) g group by g.pl_id order by sum(pl_amount) DESC) a join plant_table b on a.pl_id = b.pl_id;')
        week_sell_rank_mysql = curs.fetchall()  # 전부

        ##
        # 그래프 그리기
        # csv 파일 변환
        query = 'select pl_name, sum_a from (select pl_id, sum(pl_amount) as sum_a from (select oi.order_id, pl_id, pl_amount, order_state from order_items oi join order_list ol on oi.order_id = ol.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and order_date BETWEEN DATE_ADD(NOW(),INTERVAL "-7 9" day_hour) AND DATE_ADD(NOW(),INTERVAL 9 hour)) g group by g.pl_id order by sum(pl_amount) DESC) a join plant_table b on a.pl_id = b.pl_id'

        df = pd.read_sql_query(query, conn)
        df.to_csv(r'shop/csv/weekSellPlant.csv', index=False)

        #
        plt.style.use('ggplot')
        df = pd.read_csv('shop/csv/weekSellPlant.csv', encoding='utf-8').head(30)

        plt.ticklabel_format(axis="y", style="plain")

        for bar in plt.bar(df['pl_name'], df['sum_a'], color='plum', width=0.5).patches:
            if bar.get_height() > 10:
                bar.set_facecolor('orchid')

        plt.bar(df['pl_name'][:3], df['sum_a'][:3], width=0.5, color='mediumvioletred')

        plt.title('최근 일주일 판매량')
        plt.xlabel('< 식물명 >', fontsize=12)
        plt.ylabel('< 일주일 판매량 >', fontsize=12)
        plt.rc('xtick', labelsize=12)
        plt.rc('ytick', labelsize=12)
        plt.xticks(rotation='vertical')

        plt.savefig('static/img/graph/weekSellPlant.png', bbox_inches="tight")
        plt.close('all')

        response_date['img_graph'] = 'img/graph/weekSellPlant.png'
        ##

        week_sell_rank_list = []
        week_sell_rank_list_l = []
        for list in week_sell_rank_mysql:
            for l in list:
                week_sell_rank_list_l.append(l)

            week_sell_rank_list.append(week_sell_rank_list_l)
            week_sell_rank_list_l = []

        response_date['week_sell_rank_list'] = week_sell_rank_list
        ######

    #
    elif id == 3:
        datetimeStr = str(datetime.now().date())
        response_date['datetimeStr'] = datetimeStr[0:7]
        response_date['datetimeYear'] = datetimeStr[0:4]
        response_date['datetimeMonth'] = datetimeStr[5:7]

        ### 최근 한달 회원별 구매 총액 ###
        # mysql
        curs.execute('SELECT mb_id, FORMAT(sum(total_price), 0) FROM (SELECT ol.order_id, mb_id, total_price, order_date FROM order_list ol join order_items oi on ol.order_id = oi.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) group by ol.order_id) a WHERE mb_id != "sasim" group by a.mb_id order by sum(total_price) DESC;', (datetimeStr[0:7], ))
        user_buy_amount_rank_mysql = curs.fetchall()  # 전부

        ##
        # 그래프 그리기
        # csv 파일 변환
        query = 'SELECT mb_id, sum(total_price) FROM (SELECT ol.order_id, mb_id, total_price, order_date FROM order_list ol join order_items oi on ol.order_id = oi.order_id where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate("'+ datetimeStr[0:7] +'", order_date) group by ol.order_id) a WHERE mb_id != "sasim" group by a.mb_id order by sum(total_price) DESC'

        df = pd.read_sql_query(query, conn)
        df.to_csv(r'shop/csv/monthBuyUser.csv', index=False)

        #
        plt.style.use('ggplot')
        df = pd.read_csv('shop/csv/monthBuyUser.csv', encoding='utf-8').head(30)

        plt.ticklabel_format(axis="y", style="plain")

        plt.bar(df['mb_id'], df['sum(total_price)'], width=0.5, color='tan')
        plt.bar(df['mb_id'][:3], df['sum(total_price)'][:3], width=0.5, color='goldenrod')

        plt.title('이번달 회원별 구매액')
        plt.xlabel('< 회원ID >', fontsize=12)
        plt.ylabel('< 구매 총액 >', fontsize=12)
        plt.rc('xtick', labelsize=12)
        plt.rc('ytick', labelsize=12)
        plt.xticks(rotation='vertical')

        plt.savefig('static/img/graph/monthBuyUser.png', bbox_inches="tight")
        plt.close('all')

        response_date['img_graph'] = 'img/graph/monthBuyUser.png'
        ##

        user_buy_amount_rank_list = []
        user_buy_amount_rank_l = []
        for list in user_buy_amount_rank_mysql:
            for l in list:
                user_buy_amount_rank_l.append(l)

            user_buy_amount_rank_list.append(user_buy_amount_rank_l)
            user_buy_amount_rank_l = []

        response_date['user_buy_amount_rank_list'] = user_buy_amount_rank_list
        ######

    #
    elif id == 4:

        datetimeA = datetime.now().date()
        datetimeB = datetimeA - timedelta(days=30)

        dateformat = "%Y-%m-%d"
        tmpA = datetimeA.strftime(dateformat)
        tmpB = datetimeB.strftime(dateformat)
        response_date['tmpA'] = tmpA
        response_date['tmpB'] = tmpB

        dateformat = "%Y-%m"
        prevMonth = datetimeB.strftime(dateformat)
        response_date['prevMonthY'] = prevMonth[0:4]
        response_date['prevMonthM'] = prevMonth[5:]

        ### 최근 한달 매출액 ###
        # mysql
        curs.execute('SELECT FORMAT(sum(g.total_price), 0), g.order_date FROM (SELECT total_price, order_date FROM order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and order_date BETWEEN DATE_ADD(%s,INTERVAL -1 MONTH ) AND %s) g group by g.order_date order by g.order_date DESC;', (datetime.now(), datetime.now(),))
        month_total_amount_mysql = curs.fetchall()  # 전부

        ##
        # 그래프 그리기
        # x축, y축 값 생성
        x = []
        for i in range(0, 31):
            x.append(date.today() + timedelta(days=-i))

        y = []
        for a in x:
            curs.execute('SELECT sum(g.total_price), g.order_date FROM (SELECT total_price, order_date FROM order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and order_date BETWEEN DATE_ADD(%s,INTERVAL -1 MONTH ) AND %s) g group by g.order_date order by g.order_date DESC;', (datetime.now(), datetime.now(),))
            month_date = curs.fetchall()  # 전부

            y.append(0)
            for b in month_date:
                if a == b[1]:
                    y[-1] = b[0]

        x.reverse()
        y.reverse()
        #

        plt.style.use('ggplot')

        plt.ticklabel_format(axis="y", style="plain")
        plt.plot(x, y, color='rebeccapurple')
        plt.title('최근 한달 매출액')
        plt.xlabel('< 날짜 >', fontsize=12)
        plt.ylabel('< 매출액 >', fontsize=12)
        plt.xticks(ticks=x, labels=x, rotation='vertical', fontsize=10)
        plt.locator_params(axis='x', nbins=len(x)/2)

        plt.savefig('static/img/graph/monthTotalAmount.png', bbox_inches="tight")
        plt.close('all')

        response_date['img_graph'] = 'img/graph/monthTotalAmount.png'
        ##

        response_date['month_total_amount_mysql'] = month_total_amount_mysql
        ######

    #
    elif id == 5:

        datetimeA = datetime.now().date()
        datetimeB = datetimeA - timedelta(days=31)
        datetimeC = datetimeA - timedelta(days=61)
        datetimeD = datetimeA - timedelta(days=91)
        datetimeE = datetimeA - timedelta(days=121)
        datetimeF = datetimeA - timedelta(days=151)

        dateformat = "%Y-%m-%d"
        tmpA = datetimeA.strftime(dateformat)
        tmpB = datetimeB.strftime(dateformat)
        response_date['tmpA'] = tmpA
        response_date['tmpB'] = tmpB

        dateformat = "%Y-%m"
        nowMonth = datetimeA.strftime(dateformat)
        prevMonth = datetimeB.strftime(dateformat)
        prevMonth2 = datetimeC.strftime(dateformat)
        prevMonth3 = datetimeD.strftime(dateformat)
        prevMonth4 = datetimeE.strftime(dateformat)
        prevMonth5 = datetimeF.strftime(dateformat)
        response_date['nowMonth'] = nowMonth
        response_date['prevMonth'] = prevMonth
        response_date['prevMonth2'] = prevMonth2
        response_date['prevMonth3'] = prevMonth3
        response_date['prevMonth4'] = prevMonth4
        response_date['prevMonth5'] = prevMonth5

        ### 최근 한달 매출액 ###
        # mysql
        curs.execute('select %s, sum(total_price) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (nowMonth[0:4]+'.'+nowMonth[5:7], nowMonth, ))
        month_sales_mysql_1 = curs.fetchone()  # 전부
        curs.execute('select %s, sum(total_price) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (prevMonth[0:4]+'.'+prevMonth[5:7], prevMonth, ))
        month_sales_mysql_2 = curs.fetchone()  # 전부
        curs.execute('select %s, sum(total_price) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (prevMonth2[0:4]+'.'+prevMonth2[5:7], prevMonth2, ))
        month_sales_mysql_3 = curs.fetchone()  # 전부
        curs.execute('select %s, sum(total_price) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (prevMonth3[0:4]+'.'+prevMonth3[5:7], prevMonth3, ))
        month_sales_mysql_4 = curs.fetchone()  # 전부
        curs.execute('select %s, sum(total_price) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (prevMonth4[0:4]+'.'+prevMonth4[5:7], prevMonth4, ))
        month_sales_mysql_5 = curs.fetchone()  # 전부
        curs.execute('select %s, sum(total_price) from order_list where order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" and locate(%s, order_date) order by order_id desc;', (prevMonth5[0:4]+'.'+prevMonth5[5:7], prevMonth5, ))
        month_sales_mysql_6 = curs.fetchone()  # 전부

        mysql_l = [month_sales_mysql_1, month_sales_mysql_2, month_sales_mysql_3, month_sales_mysql_4, month_sales_mysql_5, month_sales_mysql_6]

        ##
        # 그래프 그리기
        # x축, y축 값 생성
        x = [] #날짜
        for list in mysql_l:
            x.append(list[0])
        response_date['xxx'] = x

        y = []
        for list in mysql_l:
            if list[1] is None:
                y.append(0)
            else:
                y.append(int(list[1]))

        x.reverse()
        y.reverse()
        response_date['yyy'] = y
        #

        plt.style.use('ggplot')

        plt.ticklabel_format(axis="y", style="plain")
        plt.plot(x, y, color='royalblue')
        plt.title('월별 매출액')
        plt.xlabel('< 날짜 >', fontsize=12)
        plt.ylabel('< 매출액 >', fontsize=12)
        plt.xticks(ticks=x, labels=x, rotation='vertical', fontsize=10)

        plt.ylim(min(y)-(min(y)*0.2), max(y)+(max(y)*0.2))

        plt.savefig('static/img/graph/monthSales.png', bbox_inches="tight")
        plt.close('all')

        response_date['img_graph'] = 'img/graph/monthSales.png'
        ##

        month_sales_list = []
        month_sales_list_l = []

        for list in mysql_l:
            for x in list:
                month_sales_list_l.append(x)

            if month_sales_list_l[1] is not None:
                month_sales_list_l[1] = format(int(month_sales_list_l[1]), ',d')
            else:
                month_sales_list_l[1] = 0

            month_sales_list.append(month_sales_list_l)
            month_sales_list_l = []

        response_date['month_sales_list'] = month_sales_list
        ######

    #
    elif id == 6:

        ### 회원 재구매율 ###
        # mysql
        curs.execute('select g.order_count, count(mb_id) from (select mb_id, count(order_id) as order_count from order_list where mb_id != "sasim" and order_state != "주문 취소" and order_state != "환불 완료" and order_state != "입금 확인 전" group by mb_id order by order_id desc) g group by g.order_count;')
        user_rebuy_mysql = curs.fetchall()  # 전부

        ##
        # 그래프 그리기
        # x축, y축 값 생성
        idx = ['1건(재구매x)', '2건 이상', '10건 이상']
        v = [0, ]
        sum1 = [0, ]
        sum2 = [0, ]

        for i in user_rebuy_mysql:
            if i[0] == 1:
                v[0] = i[1]
            elif i[0] >= 2 and i[0] < 10:
                sum1.append(i[1])
            elif i[0] >= 10:
                sum2.append(i[1])

        v.append(sum(sum1))
        v.append(sum(sum2))

        user_amount = sum(v)

        user_rebuy_list = []
        user_rebuy_list_l =[]

        for a in range(0, 3):
            user_rebuy_list_l.append(idx[a])
            user_rebuy_list_l.append(v[a])
            user_rebuy_list_l.append(round((v[a]/user_amount), 3)*100)

            user_rebuy_list.append(user_rebuy_list_l)
            user_rebuy_list_l =[]

        #
        user_rebuy_series = pd.Series(v, index=idx)

        plt.title('회원 재구매율')
        colors = ['silver', '#ff9999', '#8fd9b6']
        explode = [0.2, 0, 0]
        wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 3}

        plt.pie(user_rebuy_series, wedgeprops=wedgeprops, labels=idx, autopct='%.1f%%', colors=colors, explode=explode, shadow=True, counterclock=False)
        plt.legend(loc=(1, 0.7))

        plt.savefig('static/img/graph/userRebuy.png', bbox_inches="tight")
        plt.close('all')

        response_date['img_graph'] = 'img/graph/userRebuy.png'
        ##

        response_date['user_rebuy_list'] = user_rebuy_list
        ######

    return render(request, 'statsCheck_detail.html', response_date)


# 관리자 - 식물 목록
def admin_plantList(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # Mysql
    curs.execute('SELECT * FROM plant_table order by pl_id DESC;')
    plantList = curs.fetchall()  # 전부

    #
    if request.method == "POST":

        admin_search_txt = request.POST["admin_search_txt"]

        if admin_search_txt != '':
            # Mysql
            curs.execute('SELECT * FROM plant_table WHERE pl_id = %s or pl_name = %s order by pl_id DESC;', (admin_search_txt, admin_search_txt,))
            plantList = curs.fetchall()  # 전부

            if not plantList:
                response_date['noSearch_txt'] = '검색 결과가 없습니다.'

    response_date['plantList'] = plantList

    return render(request, 'admin_plantList.html', response_date)


# 관리자 - 식물 목록 / 상세
def admin_plantList_detail(request, pl_id):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # Mysql
    curs.execute('SELECT * FROM plant_table WHERE pl_id = %s;', (pl_id,))
    plantList_detail = curs.fetchone()  # 1

    response_date['plantList_detail'] = plantList_detail

    ##
    #
    if request.method == "POST":
        category = request.POST["category"]
        name = request.POST["name"]
        animal = request.POST["animal"]
        effect = request.POST["effect"]
        place = request.POST["place"]
        size = request.POST["size"]
        time = request.POST["time"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        img1 = request.POST["img1"]
        img2 = request.POST["img2"]

        curs.execute('UPDATE plant_table SET pl_category = %s, pl_name = %s, pl_animal = %s, pl_effect = %s, pl_place = %s, pl_size = %s, pl_time = %s, pl_price = %s, pl_stock = %s, pl_img = %s, pl_detail = %s WHERE pl_id = %s', (category, name, animal, effect, place, size, time, price, stock, img1, img2, pl_id,))
        conn.commit()

        return redirect('admin_plantList_detail', pl_id=pl_id)

    return render(request, 'admin_plantList_detail.html', response_date)


# 관리자 - 주문 목록
def admin_orderList(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # Mysql
    curs.execute('SELECT * FROM order_list WHERE order_id != "200001" order by order_id DESC;')
    orderList = curs.fetchall()  # 전부

    #
    if request.method == "POST":

        admin_search_txt = request.POST["admin_search_txt"]

        if admin_search_txt != '':
            # Mysql
            curs.execute('SELECT * FROM order_list WHERE order_id = %s or mb_id = %s order by order_id DESC;', (admin_search_txt, admin_search_txt,))
            orderList = curs.fetchall()  # 전부

            if not orderList:
                response_date['noSearch_txt'] = '검색 결과가 없습니다.'

    response_date['orderList'] = orderList

    return render(request, 'admin_orderList.html', response_date)


# 관리자 - 식물 목록 / 상세
def admin_orderList_detail(request, order_id):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # Mysql
    curs.execute('SELECT * FROM order_list WHERE order_id = %s;', (order_id,))
    orderList_detail = curs.fetchone()  # 1

    phone = orderList_detail[4].split('-')

    response_date['orderList_detail'] = orderList_detail
    response_date['phone'] = phone

    # Mysql
    curs.execute('SELECT * FROM order_items WHERE order_id = %s;', (order_id,))
    orderList_detail_items = curs.fetchall()  # all
    response_date['orderList_detail_items'] = orderList_detail_items

    ##
    #
    if request.method == "POST":
        price = request.POST["price"]
        shipName = request.POST["shipName"]
        phone1 = request.POST["phone1"]
        phone2 = request.POST["phone2"]
        phone3 = request.POST["phone3"]
        phone123 = phone1 + "-" + phone2 + "-" + phone3
        postcode = request.POST["postcode"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        msg = request.POST["msg"]
        payment = request.POST["payment"]
        state = request.POST["state"]

        curs.execute('UPDATE order_list SET total_price = %s, order_name = %s, order_phone = %s, order_postcode = %s, order_address = %s, order_address_detail = %s, order_msg = %s, order_state = %s, payment = %s WHERE order_id = %s', (price, shipName, phone123, postcode, address1, address2, msg, state, payment, order_id,))
        conn.commit()

        return redirect('admin_orderList_detail', order_id=order_id)

    return render(request, 'admin_orderList_detail.html', response_date)


# 관리자 - 주문 아이템 목록
def admin_orderItemList(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # Mysql
    curs.execute('SELECT * FROM order_items order by order_id DESC;')
    orderItemList = curs.fetchall()  # 전부

    #
    if request.method == "POST":

        admin_search_txt = request.POST["admin_search_txt"]

        if admin_search_txt != '':
            # Mysql
            curs.execute('SELECT * FROM order_items WHERE order_id = %s order by order_id DESC;', (admin_search_txt,))
            orderItemList = curs.fetchall()  # 전부

            if not orderItemList:
                response_date['noSearch_txt'] = '검색 결과가 없습니다.'

    response_date['orderItemList'] = orderItemList

    return render(request, 'admin_orderItemList.html', response_date)


# 관리자 - 주문 아이템 목록
def admin_cartList(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # Mysql
    curs.execute('SELECT * FROM cart order by addCart_date DESC;')
    cartList = curs.fetchall()  # 전부

    #
    if request.method == "POST":

        admin_search_txt = request.POST["admin_search_txt"]

        if admin_search_txt != '':
            # Mysql
            curs.execute('SELECT * FROM cart WHERE mb_id = %s order by addCart_date DESC;', (admin_search_txt,))
            cartList = curs.fetchall()  # 전부

            if not cartList:
                response_date['noSearch_txt'] = '검색 결과가 없습니다.'

    response_date['cartList'] = cartList

    return render(request, 'admin_cartList.html', response_date)


# 회원탈퇴 전 진행 주문 유무 체크
def check_pw_sub(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 주문 상태 체크
    curs.execute('SELECT mb_id, order_id, order_state FROM order_list WHERE mb_id = %s and order_state!="주문 취소" and order_state!="배송 완료" and order_state!="환불 완료"', (userid,))
    orderStateCheck = curs.fetchall()  # all

    if orderStateCheck:
        response_date['orderStateCheck_txt'] = '진행 중인 주문이 있어 탈퇴가 불가능합니다.'
        response_date['orderStateCheck'] = orderStateCheck

        return render(request, 'check_pw_sub.html', response_date)
    #

    return redirect('check_pw', sort=2)

