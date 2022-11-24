from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
from decouple import config

# Create your views here.



# # MySQL Connection
conn = pymysql.connect(host=config('db_host'), user='sasim', password=config('db_password'), db='sasim', charset='utf8')

# Connection 으로 Cursor 생성
curs = conn.cursor() # curs가 DB fetch 관리


def login(request):
    response_date = {}

    if request.method == "POST":
        userid = request.POST['userid']
        password = request.POST['password']

        response_date['userid'] = userid

        check = 0

        # Mysql 에 Account 있는지 체크
        curs.execute('SELECT * FROM member_table WHERE mb_id = %s', (userid, ))

        # Account 체크
        account = curs.fetchone() # 행 가져오기

        if userid == '':
            response_date['login_blank_error'] = '아이디를 입력해주세요.'
            return render(request, 'login.html', response_date)

        elif password == '':
            response_date['login_blank_error2'] = '비밀번호를 입력해주세요.'
            return render(request, 'login.html', response_date)

        else:
            if not account:
                # conn.commit()
                response_date['login_id_error'] = '잘못된 아이디입니다.'
                return render(request, 'login.html', response_date)

            else:
                curs.execute('SELECT * FROM member_table WHERE mb_id = %s AND mb_pw = %s', (userid, password))
                # Account 체크
                account = curs.fetchone()  # 행 가져오기

                if not account:
                    response_date['login_pw_error'] = '잘못된 비밀번호입니다.'
                    return render(request, 'login.html', response_date)

                else:
                    conn.rollback() # 복원
                    # conn.close()
                    check = 1

                    request.session['check'] = check
                    request.session['account'] = account

                    return redirect('home')

    else:
        return render(request, 'login.html')


def logout(request):
    # logout(request)
    request.session.modified = True
    del request.session['account']

    # check = 0
    # request.session['check'] = check
    return redirect('home')


def terms(request):
    response_date = {}

    if request.method == "POST":
        agree1 = request.POST.get("chk1", None)
        agree2 = request.POST.get("chk2", None)

        if agree1 != None and agree2 != None:
            return render(request, 'signup.html')

        else:
            response_date['agree_error'] = '이용약관과 개인정보 수집 및 이용에 대한 동의를 전부 해주세요.'
            return render(request, 'terms.html', response_date)

    else:
        return render(request, 'terms.html')


def signup(request):
    response_date = {}

    if request.method == "POST":

        userid = request.POST["userid"]
        password = request.POST["1st_password"]
        name = request.POST["name"]
        phone1 = request.POST["phone1"]
        phone2 = request.POST["phone2"]
        phone3 = request.POST["phone3"]
        email = request.POST["email"]
        postcode = request.POST["postcode"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]

        response_date['userid'] = userid
        response_date['name'] = name
        response_date['phone1'] = phone1
        response_date['phone2'] = phone2
        response_date['phone3'] = phone3
        response_date['email'] = email
        response_date['postcode'] = postcode
        response_date['address1'] = address1
        response_date['address2'] = address2

        phone = phone1 + '-' + phone2 + '-' + phone3

        # id 존재 체크
        curs.execute('SELECT * FROM member_table WHERE mb_id = %s', (userid,))
        # Account 체크
        id_check = curs.fetchone()  # 행 가져오기

        if id_check:
            response_date['id_error'] = '사용 불가능한 아이디입니다.'

            return render(request, 'signup.html', response_date)

        elif userid and password and name and email and phone2 and phone3 is not None:
            if password == request.POST["2nd_password"]:

                curs.execute('INSERT INTO member_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (userid, password, name, phone, email, postcode, address1, address2, phone1, phone2, phone3, '',))
                conn.commit()
                # conn.close()

                return redirect('home')

            else:
                response_date['pw_error'] = '비밀번호를 다시 확인해주세요.'

                return render(request, 'signup.html', response_date)

        else:
            response_date['blank_error'] = '필수 정보를 입력해주세요.'

            return render(request, 'signup.html', response_date)
    else:
        return render(request, 'signup.html')


# 회원 목록
def user_list(request):
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
    curs.execute('SELECT * FROM member_table WHERE mb_id != "sasim";')
    user_list = curs.fetchall()  # 전부

    #
    if request.method == "POST":

        admin_search_txt = request.POST["admin_search_txt"]

        if admin_search_txt != '':
            # Mysql
            curs.execute('SELECT * FROM member_table WHERE mb_id = %s;', (admin_search_txt,))
            user_list = curs.fetchall()  # 전부

            if not user_list:
                response_date['noSearch_txt'] = '검색 결과가 없습니다.'

    response_date['user_list'] = user_list

    #
    return render(request, 'user_list.html', response_date)



# 회원 목록
def user_list_detail(request, mb_id):
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
    curs.execute('SELECT * FROM member_table WHERE mb_id = %s;', (mb_id,))
    user_list_detail = curs.fetchone()  # 1

    response_date['user_list_detail'] = user_list_detail

    ##
    #
    if request.method == "POST":
        name = request.POST["name"]
        phone1 = request.POST["phone1"]
        phone2 = request.POST["phone2"]
        phone3 = request.POST["phone3"]
        phone = phone1 + "-" + phone2 + "-" + phone3
        email = request.POST["email"]
        postcode = request.POST["postcode"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        recommendId = request.POST["recommendId"]

        curs.execute('UPDATE member_table SET mb_name = %s, mb_phone = %s, mb_email = %s, mb_postcode = %s, mb_address = %s, mb_address_detail = %s, mb_phone_txt1 = %s, mb_phone_txt2 = %s, mb_phone_txt3 = %s, recommendId = %s where mb_id = %s', (name, phone, email, postcode, address1, address2, phone1, phone2, phone3, recommendId, mb_id,))
        conn.commit()

        return redirect('user_list_detail', mb_id=mb_id)

    #
    return render(request, 'user_list_detail.html', response_date)


def mypage_profile(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # Account 체크
    curs.execute('SELECT * FROM member_table WHERE mb_id = %s', (userid,))
    account = curs.fetchone()  # 1

    response_date['account'] = account
    #

    response_date['userid'] = account[0]
    response_date['userpw'] = account[1]

    #
    return render(request, 'mypage_profile.html', response_date)


# 회원정보 수정
def modify_profile(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    # 수정 완료 버튼
    if request.POST['modifyPrFButton'] == '완료':
        # 입력받은 데이터 가져옴
        phone1 = request.POST["phone1"]
        phone2 = request.POST["phone2"]
        phone3 = request.POST["phone3"]
        email = request.POST["email"]
        postcode = request.POST["postcode"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]

        phone = phone1 + '-' + phone2 + '-' + phone3

        # 데이터 수정
        curs.execute('UPDATE member_table SET mb_phone = %s, mb_email = %s, mb_postcode = %s, mb_address = %s, mb_address_detail = %s, mb_phone_txt1 = %s, mb_phone_txt2 = %s, mb_phone_txt3 = %s where mb_id = %s', (phone, email, postcode, address1, address2, phone1, phone2, phone3, userid))
        conn.commit()

        # Account 체크
        curs.execute('SELECT * FROM member_table WHERE mb_id = %s', (userid,))
        account = curs.fetchone()  # 1

        request.session.modified = True
        del request.session['account']

        request.session['account'] = account

        response_date['account'] = account

        #
        return render(request, 'mypage_profile.html', response_date)

    ###

    #
    # 수정 취소 버튼
    elif request.POST['modifyPrFButton'] == '취소':
        #
        return redirect('mypage_profile')
    ###

    #
    return render(request, 'modify_profile.html', response_date)


# 회원정보 수정, 회원 탈퇴 > 비밀번호 확인
def check_pw(request, sort):
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

    # Account 체크
    curs.execute('SELECT * FROM member_table WHERE mb_id = %s', (userid,))
    account = curs.fetchone()  # 1

    response_date['account'] = account
    #

    # 아이디 가리기
    id_protect = userid[0]
    for n in range(int(len(userid)) -1):
        id_protect += '*'

        response_date['id_protect'] = id_protect
    #

    # 입력받은 비밀번호 값
    chk_password = request.POST.get("chk_password")

    # 비밀번호를 입력받았을 때
    if chk_password:

        # Account 체크
        curs.execute('SELECT * FROM member_table WHERE mb_id = %s', (userid,))
        chk_account = curs.fetchone()  # 1

        #
        # 비밀번호가 일치 할 경우 페이지 이동
        if chk_password == chk_account[1]:

            # 로그인 확인 값
            chk_ok = request.POST["chk_ok"]
            response_date['chk_ok'] = chk_ok

            # 회원정보 수정으로 이동
            if sort == 1:
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

                return render(request, 'modify_profile.html', response_date)

            # 회원 탈퇴 진행
            elif sort == 2:
                # 해당 회원의 구매 기록 id 'sasim'으로 변경
                curs.execute('UPDATE order_list SET mb_id = "sasim" where mb_id=%s;', (userid,))
                conn.commit()

                # 해당 회원 문의 데이터 삭제
                curs.execute('UPDATE board_contact_contact SET mb_id = "sasim" where mb_id = %s', (userid,))
                conn.commit()

                # 해당 회원 데이터 삭제
                curs.execute('delete from member_table where mb_id = %s', (userid,))
                conn.commit()

                # logout(request)
                request.session.modified = True
                del request.session['account']

                return redirect('mypage_unregister')

        # 일치하지 않을 경우, 페이지 유지
        else:
            # response_date['match_error'] = '*비밀번호가 일치하지 않습니다.'

            return redirect('check_pw',  sort)
        ###
    ###

    #
    return render(request, 'check_pw.html', response_date)


# 회원 탈퇴
def mypage_unregister(request):
    response_date = {}

    check = request.session.get('check')
    account = request.session.get('account')

    if account:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    return render(request, 'mypage_unregister.html', response_date)


# 비밀번호 변경
def mypage_modify(request, sort):
    response_date = {}

    response_date['sort'] = sort

    check = request.session.get('check')
    account = request.session.get('account')

    userid = account[0]

    # Mysql 에 Account 있는지 체크
    curs.execute('SELECT * FROM member_table WHERE mb_id = %s', (userid,))
    # Account 체크
    account = curs.fetchone()  # 행 가져오기

    userpw = account[1]
    username = account[2]
    userphone = account[3]
    useremail = account[4]
    useraddress = account[6]

    response_date['userid'] = userid
    response_date['check'] = check
    response_date['userpw'] = userpw
    response_date['username'] = username
    response_date['userphone'] = userphone
    response_date['useremail'] = useremail
    response_date['useraddress'] = useraddress

    ####

    #
    if request.method == "POST":

        # sort == 1
        if sort == 1:
            current_password = request.POST["current_password"]
            new_password = request.POST["new_password"]
            confirm_password = request.POST["confirm_password"]

            if current_password and new_password and confirm_password is not None:
                if current_password == userpw:

                    if new_password == confirm_password:
                        curs.execute('UPDATE member_table SET mb_pw = %s where mb_id = %s', (new_password, userid))
                        conn.commit()

                        userpw = new_password
                        response_date['userpw'] = userpw

                        return render(request, 'success.html', response_date)

                    else:
                        response_date['confirm_pw_error'] = '새 비밀번호를 다시 확인해주세요.'
                        return render(request, 'mypage_modify.html', response_date)

                else:
                    response_date['current_pw_error'] = '비밀번호가 일치하지 않습니다.'
                    return render(request, 'mypage_modify.html', response_date)

            else:
                response_date['blank_pw_error'] = '비밀번호를 입력해주세요.'
                return render(request, 'mypage_modify.html', response_date)

        # if sort == 1 .


    # "POST"
    # else
    else:
        return render(request, 'mypage_modify.html', response_date)
    # request.method.
