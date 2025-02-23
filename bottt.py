import os
import datetime
import requests
from getpass import getpass
import telebot
from concurrent.futures import ThreadPoolExecutor

# Token cố định
TOKEN = "7446145238:AAE272hDRYFx6hWka_BF5AkV5IPGbA7b5bY"
bot = telebot.TeleBot(TOKEN)

def gui_theo_doi(username, password, coo1, coo2, muc_tieu):
    cookies = {
        '_ga': 'GA1.2.379003127.1700346804',
        '_gid': 'GA1.2.2030621174.1700346804',
        coo1: coo2,
    }
    headers = {
        'authority': 'instamoda.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
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
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
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
        'username': muc_tieu,
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
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
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
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
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
        'userName': muc_tieu,
    }
    response = requests.post(
        f'https://instamoda.org/tools/send-follower/{id}',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    if response.json()['status'] == 'success':
        print(f'Đã tăng follow cho @{muc_tieu} ')

@bot.message_handler(commands=['start'])
def bat_dau(message):
    bot.send_message(message.chat.id, "✨ Chào mừng bạn đến với bot! ✨\n\nĐây là bot tăng follow Instagram giúp bạn tăng người theo dõi và tương tác một cách dễ dàng và nhanh chóng. 🚀\n\n📌 Nếu có thắc mắc hoặc cần hỗ trợ, liên hệ với lập trình viên: @gglllw")
    bot.send_message(message.chat.id, "Hãy gửi tôi tên tài khoản giả mạo.")
    bot.register_next_step_handler(message, lay_ten_nguoi_dung)

def lay_ten_nguoi_dung(message):
    username = message.text
    bot.send_message(message.chat.id, f"Tên người dùng: {username}. Vui lòng gửi mật khẩu.")
    bot.register_next_step_handler(message, lay_mat_khau, username)

def lay_mat_khau(message, username):
    password = message.text
    bot.send_message(message.chat.id, "Đã nhận, đang chờ đăng nhập...")
    bot.send_message(message.chat.id, "Gửi tôi tên tài khoản bạn muốn tăng follow.")
    bot.register_next_step_handler(message, lay_muc_tieu, username, password)

def lay_muc_tieu(message, username, password):
    muc_tieu = message.text
    bot.send_message(message.chat.id, f"Đang kiểm tra tài khoản giả mạo và tài khoản mục tiêu: {muc_tieu}...")
    headers = {
        'authority': 'instamoda.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
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
            executor.submit(gui_theo_doi, username, password, cookie_name, cookie_value, muc_tieu)
        bot.send_message(message.chat.id, f"Đã tăng follow cho tài khoản thành công!")
    else:
        bot.send_message(message.chat.id, "Đăng nhập thất bại, vui lòng kiểm tra lại tên người dùng và mật khẩu của tài khoản giả mạo.")

bot.polling(none_stop=True)