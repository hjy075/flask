from flask import Blueprint, render_template

board_blue = Blueprint('board_blue', __name__)

@board_blue.route('/board_list')
def board_list() :
    html = render_template('board/board_list.html')
    return html

@board_blue.route('/board_write')
def board_write() :
    html = render_template('board/board_write.html')
    return html

@board_blue.route('/board_read')
def board_read() :
    html = render_template('board/board_read.html')
    return html

@board_blue.route('/board_modify')
def board_modify() :
    html = render_template('board/board_modify.html')
    return html
