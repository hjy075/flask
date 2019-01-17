from flask import Blueprint, render_template, request
from user import user_dao

user_blue = Blueprint('user_blue', __name__)

@user_blue.route('/user_login')
def user_login() :
    html = render_template('user/user_login.html')
    return html

@user_blue.route('/user_join')
def user_join() :
    html = render_template('user/user_join.html')
    return html

@user_blue.route('/user_modify')
def user_modify() :
    html = render_template('user/user_modify.html')
    return html

@user_blue.route('/user_join_pro', methods=['post'])
def user_join_pro() :
    # 파라미터 데이터 추출
    user_name = request.form['user_name']
    user_id = request.form['user_id']
    user_pw = request.form['user_pw']

    # print(user_name)
    # print(user_id)
    # print(user_pw)
    # 저장한다.
    user_dao.add_user(user_name, user_id, user_pw)

    return 'OK'

# 아이디 중복 체크
@user_blue.route('/check_user_id', methods = ['post'])
def check_user_id() :
    user_id = request.form['user_id']

    result = user_dao.check_user_id(user_id)

    return result


