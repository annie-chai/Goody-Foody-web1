import requests
from django.shortcuts import render, redirect

from core.settings import API_URL as root
from utils.decorators import user_login_required

root += '/comment'


def regist40(request):
    return render(request, 'regist40.html')


def deletemsg40(request,pk):
    if request.method == 'GET':
        return render(request, 'deletemsg40.html')

    restaurant_msg_id = pk
    data = {
        'account': request.COOKIES['user_id'],
        "restaurant_msg_id":pk
    }

    r = requests.post(
        f'{root}/delete/',
        data=data,
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    return redirect('/comment/')


#   <test>

@user_login_required
def comment_all(request):
    r = requests.get(
        f'{root}/menu_review/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    result = r.json()
    menus = result['data']
    return render(request, 'menu.html', {'menus': menus})

@user_login_required
def comment(request):
    restaurant_id = request.GET.get('restaurant_id')
    r = requests.get(
        f'{root}/detail/',
        params={'restaurant_id': restaurant_id},
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    data = r.json()
    comments = data['data']
    return render(request, 'menu.html', {'comments': comments})



# <test2>
# @user_login_required
# def comment(request):
#     if request.method == 'POST':
#
#         restaurant_id = request.POST['restaurant_id']
#         account = request.COOKIES['user_id']
#         content = request.POST['content']
#         time = request.POST['time']
#         data = {
#
#             "restaurant_id ":restaurant_id,
#             "account":account,
#             "content":content,
#             "time": time
#         }
#         r = requests.post(
#             f'{root}/add/',
#             data=data,
#             cookies={'sessionid': request.COOKIES['sessionid']}
#         )
#         print(r.json())
#     r = requests.get(
#         f'{root}/all/',
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     if r.status_code == 401:
#         return redirect('/logout/')
#
#     result = r.json()
#     restaurant_msgs = result['data']
#     print(restaurant_msgs)
#     return render(request, 'comment.html', {'restaurant_msgs': restaurant_msgs})

# @user_login_required
# def comment_add(request):
#     if request.method == 'GET':
#         return render(request, 'comment.html')
#     restaurant_msg_id=request.POST['restaurant_msg_id']
#     restaurant_id = request.POST['restaurant_id']
#     content	 = request.POST['content']
#     time = request.POST['time']
#     data = {
#         'restaurant_msg_id': restaurant_msg_id,
#         'restaurant_id': restaurant_id,
#         'account': ,
#         'content': content,
#         'time': time,
#     }
#     r = requests.post(
#         f'{root}/add/',
#         data=data,
#     )
#     result = r.json()
#     return render(request, 'comment.html', {'message': result['message']})


# @user_login_required
# def deletemsg40(request):
#     if request.method == 'GET':
#         return render(request,'deletemsg40.html')

#     restaurant_msg_id= request.POST['restaurant_msg_id']
#     data = {
#         'account': request.COOKIES['user_id']
#     }

#     r = requests.post(
#         f'{root}/delete/{restaurant_msg_id}/',
#         data=data,
#         cookies={'sessionid': request.COOKIES['sessionid']}
#     )
#     result = r.json()
#     return render(request, 'deletemsg40.html', {'message': result['message']})
# <test2>
@user_login_required
def comment(request):
# def comment(request,pk):
    if request.method == 'POST':
        # restaurant_msg_id = request.POST['restaurant_msg_id']
        restaurant_id = request.POST['restaurant_id']
        # restaurant_id = pk
        account = request.COOKIES['user_id']
        content	 = request.POST['content']
        data = {
            # "restaurant_msg_id":restaurant_msg_id,
            "restaurant_id ":restaurant_id,
            "account":account,
            "content":content,
            # "time": time
        }
        r = requests.post(
            f'{root}/add/',
            data=data,
            cookies={'sessionid': request.COOKIES['sessionid']}
        )
        print(r.json())
    r = requests.get(
        f'{root}/all/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )
    if r.status_code == 401:
        return redirect('/logout/')

    result = r.json()
    restaurant_msgs = result['data']
    print(restaurant_msgs)
    return render(request, 'comment.html', {'restaurant_msgs': restaurant_msgs})
