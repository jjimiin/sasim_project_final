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


def test_main(request):
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

        # q1 식물 기른 경험 여부
        q1 = request.POST['q1']
        response_date['q1_all'] = q1
        if q1 == 'Y':
            q1_1 = request.POST['q1_1'] # 까다로운 식물 가능 수치
            q1_1 = int(q1_1)
            response_date['q1_1_all'] = q1_1

            if q1_1 == 2:
                response_date['q1_1'] = '#매우잘견딤'
                response_date['q1_2'] = '#잘견딤'
                response_date['testResult_detail_t'] = '식물 관리 방법만 찾아 보면 관리하기 쉬운 식물들을 추천해드려요.'
                response_date['testResult_detail_t2'] = '간단한 관리만으로도 잘 자라는 식물들입니다.'
            elif q1_1 == 3:
                response_date['q1_2'] = '#잘견딤'
                response_date['q1_3'] = '#관심조금'
                response_date['testResult_detail_t'] = '아직 까다로운 작업을 하기 힘든 분들에게도 잘 기를 수 있는 식물들을 추천해드려요.'
                response_date['testResult_detail_t2'] = '관리에 너무 힘쓰지 않아도 잘 자라는 식물들입니다.'
            elif q1_1 == 4:
                response_date['q1_3'] = '#관심조금'
                response_date['q1_4'] = '#관심필요'
                response_date['testResult_detail_t'] = '식물을 자주 길러본 분들이라면 관리할 수 있는 식물을 추천해드려요.'
                response_date['testResult_detail_t2'] = '관심을 주지 않으면 잘 자라지 못하니 관리에 신경을 써주셔야 하는 식물들입니다.'
            elif q1_1 == 5:
                response_date['q1_4'] = '#관심필요'
                response_date['q1_5'] = '#매우관심필요'
                response_date['testResult_detail_t'] = '까다로운 식물도 많이 길러본 분들이라면 기를 수 있는 식물을 추천해드려요.'
                response_date['testResult_detail_t2'] = '관심을 자주 주면서 관리를 많이 해줘야 하는 식물들입니다.'

        else:
            q1_1 = 2

            response_date['q1_1'] = '#매우잘견딤'
            response_date['q1_2'] = '#잘견딤'
            response_date['testResult_detail_t'] = '초보자나 바쁜 분들도 쉽게 기를 수 있는 있는 식물들을 추천해드려요.'
            response_date['testResult_detail_t2'] = '많거나 까다로운 관리를 해주지 않아도 잘 자라는 식물들입니다.'
        #

        #
        # q2 반려동물 여부
        q2 = request.POST['q2']
        response_date['q2_all'] = q2
        if q2 == 'Y':
            q2_1 = request.POST['q2_1'] # 관리 가능 수치
            q2_1 = int(q2_1)
            response_date['q2_1_all'] = q2_1

            if q2_1 == 5:
                response_date['q2_1'] = '#반려동물안심'
                response_date['testResult_detail_a'] = '동물과 사이좋게 지낼 수 있는 식물이니 안심해도 된답니다.'
            elif q2_1 == 4 or q2_1 == 3:
                response_date['q2_1'] = '#반려동물안심'
                response_date['q2_2'] = '#반려동물주의'
                response_date['testResult_detail_a'] = '동물이 먹거나 냄새를 가까이 와서 맡지 않도록 주의가 필요한 식물들도 있습니다.'

        else:
            q2_1 = 1

            response_date['q2_1'] = '#반려동물안심'
            response_date['q2_2'] = '#반려동물주의'
            response_date['q2_3'] = '#반려동물위험'
            response_date['testResult_detail_a'] = '동물들과 사이좋게 지내기 힘든 식물들도 있으니 주의해서 살펴보세요.'
        #

        #
        # 장소 햇빛량
        q3 = request.POST['q3']
        q3 = int(q3)
        response_date['q3_all'] = q3

        if q3 == 5:
            response_date['q3_1'] = '#햇빛매우가득'
            response_date['q3_2'] = '#햇빛가득'
            response_date['testResult_detail_p'] = '햇빛이 아주 잘 드는 곳을 좋아하는 식물들입니다.'
        elif q3 == 4:
            response_date['q3_2'] = '#햇빛가득'
            response_date['q3_3'] = '#햇빛보통'
            response_date['testResult_detail_p'] = '햇빛이 잘 드는 곳을 좋아하는 식물들입니다.'
        elif q3 == 3:
            response_date['q3_3'] = '#햇빛보통'
            response_date['q3_4'] = '#햇빛조금'
            response_date['testResult_detail_p'] = '햇빛이 적당히 드는 곳을 좋아하는 식물들입니다.'
        elif q3 == 2:
            response_date['q3_4'] = '#햇빛조금'
            response_date['q3_5'] = '#햇빛매우조금'
            response_date['testResult_detail_p'] = '햇빛을 조금만 싶어하는 식물들입니다.'

        #

        #
        # 장소 크기
        q4 = request.POST['q4']
        q4 = int(q4)
        response_date['q4_all'] = q4

        if q4 == 1:
            response_date['q4_1'] = '#매우작음'
            response_date['testResult_detail_s'] = '작은 식물로 좁은 공간에서도 식물이 잘 자랄 수 있습니다.'
        elif q4 == 2:
            response_date['q4_1'] = '#매우작음'
            response_date['q4_2'] = '#작음'
            response_date['testResult_detail_s'] = '살짝 작은 식물이므로 너무 좁지만 않은 공간이라면 잘 자랄 수 있습니다.'
        elif q4 == 3:
            response_date['q4_2'] = '#작음'
            response_date['q4_3'] = '#보통'
            response_date['testResult_detail_s'] = '크진 않지만 너무 좁은 공간에는 식물이 자라기 힘들 수 있으니 여유 공간을 잘 살펴주세요.'
        elif q4 == 4:
            response_date['q4_3'] = '#보통'
            response_date['q4_4'] = '#큼'
            response_date['testResult_detail_s'] = '식물이 살짝 클 수도 있으니 여유 공간이 있는지 충분히 확인해주세요.'
        elif q4 == 5:
            response_date['q4_4'] = '#큼'
            response_date['q4_5'] = '#매우큼'
            response_date['testResult_detail_s'] = '크게 자라는 식물이니 넓고 높은 공간을 마련해주시면 식물이 좋아합니다.'
        #

        # 
        #
        curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND pl_place = %s AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (q2_1, q3, (q4-1), q4, (q1_1-1), q1_1,))
        result_list = curs.fetchmany(4) # 4개

        curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (q2_1, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1,))
        result_list_x = curs.fetchall() # 전부

        #
        # 겹치는 항목 확인
        if result_list:
            result_list_s = []
            for a in result_list_x:
                result_list_s.append(a)

            for x in result_list:
                i = 0
                for i in range(len(result_list_s)):
                    if x == result_list_s[i]:
                        result_list_s[i] = 0
                        i += 0
                        
            # 겹치는 항목 삭제
            t = 0
            for t in range(len(result_list_s)):
                if 0 in result_list_s:
                    result_list_s.remove(0)
                t += 1
        ##

        #
        # 중요도
        q5 = request.POST['q5']
        response_date['q5_all'] = q5

        #
        # 관리 빈도 및 난이도
        if q5 == '1':
            response_date['plant_list_txt3'] = '관리 난이도별로 준비했어요.'

            if q1_1 == 2:
                response_date['result_list_total_1_1'] = '#매우쉬움'
                response_date['result_list_total_1_2'] = '#쉬움'
            elif q1_1 == 3:
                response_date['result_list_total_1_1'] = '#쉬움'
                response_date['result_list_total_1_2'] = '#보통'
            elif q1_1 == 4:
                response_date['result_list_total_1_1'] = '#보통'
                response_date['result_list_total_1_2'] = '#어려움'
            elif q1_1 == 5:
                response_date['result_list_total_1_1'] = '#어려움'
                response_date['result_list_total_1_2'] = '#매우어려움'
                
            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND pl_time = %s;', (q2_1, (q3-1), q3, (q4-1), q4, (q1_1-1),))
            result_list_total_1 = curs.fetchall()  # 전부
            response_date['result_list_total_1'] = result_list_total_1[:3]

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND pl_time = %s;', (q2_1, (q3-1), q3, (q4-1), q4, q1_1,))
            result_list_total_2 = curs.fetchall()  # 전부
            response_date['result_list_total_2'] = result_list_total_2[:3]

        #
        # 크기
        elif q5 == '2':
            response_date['plant_list_txt3'] = '식물 크기별로 준비했어요.'

            if q4 == 1:
                response_date['result_list_total_1_2'] = '#매우작음'
            elif q4 == 2:
                response_date['result_list_total_1_1'] = '#매우작음'
                response_date['result_list_total_1_2'] = '#작음'
            elif q4 == 3:
                response_date['result_list_total_1_1'] = '#작음'
                response_date['result_list_total_1_2'] = '#보통'
            elif q4 == 4:
                response_date['result_list_total_1_1'] = '#보통'
                response_date['result_list_total_1_2'] = '#큼'
            elif q4 == 5:
                response_date['result_list_total_1_1'] = '#큼'
                response_date['result_list_total_1_2'] = '#매우큼'

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND pl_size = %s AND (pl_time >= %s and pl_time <= %s);', (q2_1, (q3-1), q3, (q4-1), (q1_1-1), q1_1,))
            result_list_total_1 = curs.fetchall() # 전부
            response_date['result_list_total_1'] = result_list_total_1[:3]

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND pl_size = %s AND (pl_time >= %s and pl_time <= %s);', (q2_1, (q3-1), q3, q4, (q1_1-1), q1_1,))
            result_list_total_2 = curs.fetchall() # 전부
            response_date['result_list_total_2'] = result_list_total_2[:3]

        #
        # 효과
        elif q5 == '3':
            response_date['plant_list_txt3'] = '식물 효과별로 준비했어요.'

            response_date['result_list_total_1_1'] = '#공기정화'
            response_date['result_list_total_1_2'] = '#가습'
            response_date['result_list_total_1_3'] = '#벌레퇴치'

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s) AND (pl_effect like %s);', (q2_1, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1, '3%',))
            result_list_total_1 = curs.fetchall()  # 전부
            response_date['result_list_total_1'] = result_list_total_1[:3]

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s) AND (pl_effect like %s);', (q2_1, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1, '_3_',))
            result_list_total_2 = curs.fetchall()  # 전부
            response_date['result_list_total_2'] = result_list_total_2[:3]

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s) AND (pl_effect like %s);', (q2_1, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1, '%3',))
            result_list_total_3 = curs.fetchall()  # 전부
            response_date['result_list_total_3'] = result_list_total_3[:3]


        # 반려동물 위험성
        elif q5 == '4':
            response_date['plant_list_txt3'] = '반려동물 위험성별로 준비했어요.'

            if q2_1 < 3:
                response_date['result_list_total_1_1'] = '#반려동물안전'
                response_date['result_list_total_1_2'] = '#반려동물주의'
                response_date['result_list_total_1_3'] = '#반려동물위험'

                curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE (pl_animal >= %s and pl_animal <= %s) AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (3, 4, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1,))
                result_list_total_2 = curs.fetchall()  # 전부
                response_date['result_list_total_2'] = result_list_total_2[:3]

                curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal <= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (2, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1,))
                result_list_total_3 = curs.fetchall()  # 전부
                response_date['result_list_total_3'] = result_list_total_3[:3]

            elif q4 < 5:
                response_date['result_list_total_1_2'] = '#반려동물주의'
                response_date['result_list_total_1_1'] = '#반려동물안전'

                curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE (pl_animal >= %s and pl_animal <= %s) AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (3, 4, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1,))
                result_list_total_2 = curs.fetchall()  # 전부
                response_date['result_list_total_2'] = result_list_total_2[:3]

            elif q4 == 5:
                response_date['result_list_total_1_1'] = '#반려동물안전'

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal = %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (5, (q3-1), q3, (q4-1), q4, (q1_1-1), q1_1,))
            result_list_total_1 = curs.fetchall()  # 전부
            response_date['result_list_total_1'] = result_list_total_1[:3]

        # 일조량
        elif q5 == '5':
            response_date['plant_list_txt3'] = '일조량별로 준비했어요.'

            if q3 == 5:
                response_date['result_list_total_1_1'] = '#햇빛매우가득'
                response_date['result_list_total_1_2'] = '#햇빛가득'
            elif q3 == 4:
                response_date['result_list_total_1_1'] = '#햇빛가득'
                response_date['result_list_total_1_2'] = '#햇빛보통'
            elif q3 == 3:
                response_date['result_list_total_1_1'] = '#햇빛보통'
                response_date['result_list_total_1_2'] = '#햇빛조금'
            elif q3 == 2:
                response_date['result_list_total_1_1'] = '#햇빛조금'
                response_date['result_list_total_1_2'] = '#햇빛매우조금'

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND pl_place = %s AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (q2_1, q3, (q4-1), q4, (q1_1-1), q1_1,))
            result_list_total_1 = curs.fetchall()  # 전부
            response_date['result_list_total_1'] = result_list_total_1[:3]

            curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND pl_place = %s AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (q2_1, (q3-1), (q4-1), q4, (q1_1-1), q1_1,))
            result_list_total_2 = curs.fetchall()  # 전부
            response_date['result_list_total_2'] = result_list_total_2[:3]

        ##

        #
        if not result_list:
            return render(request, 'test_result.html', response_date)

        else:
            response_date['testResult'] = result_list
            response_date['testResult_s'] = result_list_s[:4]

            # 추천 기록 저장
            recommendId = str(q2_1) + str(q3 - 1) + str(q3) + str(q4 - 1) + str(q4) + str(q1_1 - 1) + str(q1_1)

            curs.execute('update member_table set recommendId = %s where mb_id = %s', (recommendId, userid,))
            conn.commit()
            ##

            return render(request, 'test_result.html', response_date)

    else:
        return render(request, 'test_main.html', response_date)


#
def test_result(request):
    check = request.session.get('check')
    account = request.session.get('account')

    userid = account[0]
    username = account[2]

    response_date = {}

    response_date['check'] = check
    response_date['account'] = account

    ####

    return render(request, 'test_result.html', response_date)


#
def test_result_list(request):
    check = request.session.get('check')
    account = request.session.get('account')

    userid = account[0]
    username = account[2]

    response_date = {}

    response_date['check'] = check
    response_date['account'] = account

    ####

    # 추천 기록 가져옴
    curs.execute('SELECT recommendId from member_table WHERE mb_id = %s;', (userid,))
    recommendId = curs.fetchone()  # 하나

    if recommendId[0] != '':
        curs.execute('SELECT pl_id, pl_name, FORMAT(pl_price, 0), pl_img FROM plant_table WHERE pl_animal >= %s AND (%s <= pl_place and pl_place <= %s) AND (pl_size >= %s and pl_size <= %s) AND (pl_time >= %s and pl_time <= %s);', (int(recommendId[0][0]), int(recommendId[0][1]), int(recommendId[0][2]), int(recommendId[0][3]), int(recommendId[0][4]), int(recommendId[0][5]), int(recommendId[0][6]),))
        result_list_s = curs.fetchall() # 전부

        #
        if result_list_s:
            response_date['testResult_s'] = result_list_s

            # 페이지
            page = request.GET.get('page', '1')

            # 페이지당 10개씩
            paginator = Paginator(result_list_s, 9)
            page_obj = paginator.get_page(page)

            response_date['page_obj'] = page_obj

            return render(request, 'test_result_list.html', response_date)

    return render(request, 'test_result_list.html', response_date)


#
def test_introduce(request):
    check = request.session.get('check')
    account = request.session.get('account')

    response_date = {}

    if account is not None:
        userid = account[0]
        username = account[2]

        response_date['check'] = check
        response_date['account'] = account

    ####

    return render(request, 'test_introduce.html', response_date)

