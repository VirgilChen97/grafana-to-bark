import requests
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/<path>', methods=['POST'])
def handle_post(path):
    # 从请求体中获取 title 字段和 message 字段
    data = request.get_json()
    title = data.get('title', '')
    message = data.get('message', '')

    # 构建要发送到 https://api.day.app 的数据
    payload = {
        "body": message,
        "title": title
    }
    iconUrl = os.environ["ICON_URL"]
    if iconUrl:
        payload["icon"] = iconUrl
    group = os.environ["GROUP"]
    if group:
        payload["group"] = group

    # 发送 POST 请求到 https://api.day.app
    response = requests.post(f'https://api.day.app/{path}', json=payload)

    # 返回响应给请求者
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
