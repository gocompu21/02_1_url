from django.shortcuts import render
from django.http import HttpResponse

blog_list_db = [
    {
        "id": 1,
        "title": "장고는 너무 재밌어. 그래 계속해",
        "content": "내용입니다.",
        "author": "user1",
    },
    {
        "id": 2,
        "title": "파이썬도 매우 재미져~~~~~커밋할래",
        "content": "Content 2",
        "author": "user2",
    },
    {
        "id": 3,
        "title": "그런가봐. 바이브 코딩은 더 재미있어....정말 다 하겠다.",
        "content": "Content 3",
        "author": "user3",
    },
]

user_list_db = [
    {
        "id": 1,
        "username": "user1",
        "email": "user1@gmail.com",
        "password": "password1",
    },
    {
        "id": 2,
        "username": "user2",
        "email": "user2@gmail.com",
        "password": "password2",
    },
    {
        "id": 3,
        "username": "user3",
        "email": "user3@gmail.com",
        "password": "password3",
    },
]


def index(request):
    return HttpResponse("Hello World")


def blog_list(request):
    context = {
        "blog_list": blog_list_db,
        "hello": [10, 20, 30, 40, 50],
    }
    return render(request, "main/blog_list.html", context)


def blog_details(request, pk):
    blog = blog_list_db[pk - 1]
    context = {
        "blog": blog,
    }
    return render(request, "main/blog_details.html", context)


def accounts_details(request, username):
    finduser = None
    for user in user_list_db:
        if user["username"] == username:
            finduser = user
            break
    if finduser is None:
        return HttpResponse("User not found")
    context = {
        "finduser": finduser,
    }
    return render(request, "main/accounts_details.html", context)


def test(request):
    study_list = [
        {
            "day": "화요일",
            "day_class": "orange",
            "title": "브레인해킹스쿨 : 뇌과학으로 사용자를 사로잡는...",
            "level": "입문",
            "level_class": "level-yellow",
            "instructor": "스터디장 강성준 & Jun",
            "avatar_color": "#1f2937",
        },
        {
            "day": "화요일",
            "day_class": "",
            "title": "데이터 기반 회고: 나의 하루를 증명하는 리포트 만들기",
            "level": "입문",
            "level_class": "level-yellow",
            "instructor": "스터디장 Hero",
            "avatar_color": "#ddd",
        },
        {
            "day": "화요일",
            "day_class": "orange",
            "title": "프리랜서를 위한, 내 전문성 전자책 4주 안에 완성하기",
            "level": "중급",
            "level_class": "level-red",
            "instructor": "스터디장 송아영",
            "avatar_color": "#333",
        },
        {
            "day": "화요일",
            "day_class": "orange",
            "title": "외주비 0원! 4주만에 만드는 팔리는 브랜드 영상",
            "level": "입문",
            "level_class": "level-yellow",
            "instructor": "스터디장 DECK",
            "avatar_color": "#555",
        },
        {
            "day": "수요일",
            "day_class": "orange",
            "title": "나만의 세계관으로 팬을 만드는, 눈에 확 끌리는 영상 뚝딱 완성",
            "level": "입문",
            "level_class": "level-yellow",
            "instructor": "스터디장 물결2",
            "avatar_color": "#777",
        },
    ]
    context = {
        "study_list": study_list,
    }
    return render(request, "main/test.html", context)


def test2(request):
    questions = []
    for i in range(1, 26):
        questions.append(
            {
                "id": i,
                "question": f"Python 문제 {i}: 다음 중 올바른 설명은 무엇입니까?",
                "options": [
                    f"보기 {i}-1: Python은 컴파일 언어이다.",
                    f"보기 {i}-2: Django는 프론트엔드 프레임워크이다.",
                    f"보기 {i}-3: 리스트는 변경 불가능(Immutable)하다.",
                    f"보기 {i}-4: 튜플은 변경 가능(Mutable)하다.",
                    f"보기 {i}-5: 정답은 이 보기입니다.",
                ],
            }
        )

    context = {"questions": questions}
    return render(request, "main/test2.html", context)


# Create your views here.
