import os
import datetime
import requests
from getpass import getpass
import telebot
from concurrent.futures import ThreadPoolExecutor

# Thay "TOKEN_CUA_BAN" bằng token bot Telegram của bạn
TOKEN = "TOKEN_CUA_BAN"  # Token cố định
bot = telebot.TeleBot(TOKEN)


def gui_follow(username, password, coo1, coo2, tragrt):
    """
    Gửi follow đến tài khoản Instagram mục tiêu.

    Args:
        username: Tên người dùng Instagram (tài khoản ảo).
        password: Mật khẩu Instagram (tài khoản ảo).
        coo1: Tên cookie.
        coo2: Giá trị cookie.
        tragrt: Tên người dùng Instagram mục tiêu cần tăng follow.
    """
    cookies = {
        '_ga': 'GA1.2.379003127.1700346804',
        '_gid': 'GA1.2.2030621174.1700346804',
        coo1: coo2,
    }
    headers = {
        'authority': 'instamoda.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',  # Thay đổi ngôn ngữ sang tiếng Việt
        'referer': 'https://instamoda.org/tools',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    }
    response = requests.get('https://instamoda.org/tools/send-follower', cookies=cookies, headers=headers)
    for cookie_name, cookie_value in response.cookies.items():
        pass
    cookies = {
        '_ga': 'GA1.2.379003127.1700346804',
        '_gid': 'GA1.2.2030621174.1700346804',
        cookie_name: cookie_value,
    }
    headers = {
        'authority': 'instamoda.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8', # Thay đổi ngôn ngữ
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://instamoda.org',
        'referer': 'https://instamoda.org/tools/send-follower',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    }
    params = {
        'formType': 'findUserID',
    }
    data = {
        'username': tragrt,
    }
    response = requests.post('https://instamoda.org/tools/send-follower', params=params, cookies=cookies, headers=headers, data=data)
    id = response.text.split('<input type="hidden" name="userID" value="')[1].split('"')[0]
    cookies = {
        '_ga': 'GA1.2.379003127.1700346804',
        '_gid': 'GA1.2.2030621174.1700346804',
        cookie_name: cookie_value,
    }
    headers = {
        'authority': 'instamoda.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8', # Thay đổi ngôn ngữ
        'cache-control': 'max-age=0',
        'referer': 'https://instamoda.org/tools/send-follower',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    }
    response = requests.get(f'https://instamoda.org/tools/send-follower/{id}', cookies=cookies, headers=headers)
    cookies = {
        '_ga': 'GA1.2.379003127.1700346804',
        '_gid': 'GA1.2.2030621174.1700346804',
        cookie_name: cookie_value,
    }
    headers = {
        'authority': 'instamoda.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',  # Thay đổi ngôn ngữ
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://instamoda.org',
        'referer': f'https://instamoda.org/tools/send-follower/{id}',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    params = {
        'formType': 'send',
    }
    data = {
        'adet': '300',
        'userID': id,
        'userName': tragrt,
    }
    response = requests.post(
        f'https://instamoda.org/tools/send-follower/{id}',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    if response.json()['status'] == 'success':
        print(f'Đã gửi follow đến @{tragrt} ')


@bot.message_handler(commands=['start'])
def start(message):
    """
    Xử lý lệnh /start.
    """
    bot.send_message(message.chat.id, "✨ Chào bạn, rất vui được gặp bạn! ✨\n\nBot này giúp bạn tăng follow Instagram một cách dễ dàng và nhanh chóng. 🚀\n\n📌 Nếu có bất kỳ câu hỏi hoặc cần hỗ trợ, hãy liên hệ với lập trình viên: @gglllw")
    bot.send_message(message.chat.id, "Hãy gửi cho tôi tên tài khoản Instagram ảo của bạn.")
    bot.register_next_step_handler(message, lay_username)


def lay_username(message):
    """
    Lấy tên người dùng Instagram ảo.
    """
    username = message.text
    bot.send_message(message.chat.id, f"Tên tài khoản: {username}. Vui lòng gửi mật khẩu.")
    bot.register_next_step_handler(message, lay_password, username)


def lay_password(message, username):
    """
    Lấy mật khẩu Instagram ảo.
    """
    password = message.text
    bot.send_message(message.chat.id, "Đang chờ đăng nhập...")
    bot.send_message(message.chat.id, "Gửi tên tài khoản Instagram bạn muốn tăng follow.")
    bot.register_next_step_handler(message, lay_tragrt, username, password)


def lay_tragrt(message, username, password):
    """
    Lấy tên người dùng Instagram mục tiêu và thực hiện gửi follow.
    """
    tragrt = message.text
    bot.send_message(message.chat.id, f"Đang kiểm tra tài khoản ảo và tài khoản mục tiêu: {tragrt}.  Vui lòng chờ...")
    headers = {
        'authority': 'instamoda.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8', # Thay đổi ngôn ngữ
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://instamoda.org',
        'referer': 'https://instamoda.org/login',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    params = ''
    data = {
        'username': username,
        'password': password,
        'userid': '',
        'antiForgeryToken': '92e040589f9f0237f5ddd02297bbcf92',
    }
    response = requests.post('https://instamoda.org/login', params=params, headers=headers, data=data)

    if response.json()['status'] == 'success':
        for cookie_name, cookie_value in response.cookies.items():
            pass
        with ThreadPoolExecutor() as executor:
            executor.submit(gui_follow, username, password, cookie_name, cookie_value, tragrt)
        bot.send_message(message.chat.id, f"Đã gửi follow đến tài khoản của bạn!")
    else:
        bot.send_message(message.chat.id, "Đăng nhập thất bại. Vui lòng kiểm tra tên người dùng và mật khẩu của tài khoản ảo.")


bot.polling(none_stop=True)