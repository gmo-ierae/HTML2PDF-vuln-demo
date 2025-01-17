# Copyright (c) GMO Cybersecurity by Ierae, Inc. All rights reserved.

from flask import (
    Flask,
    request,
    render_template,
    send_file
)

import uuid
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# wkhtmltopdfを利用したPDF生成を行うエンドポイント
@app.route('/receipt', methods=['POST'])
def receipt_pdf():

    file_id = str(uuid.uuid4())

    receipt_to = request.form.get('receipt_to') or ''
    template = open('./templates/pdf_template.html').read().replace('###to###', receipt_to)

    cmd = ['/usr/local/bin/wkhtmltopdf', '-', f'./data/{file_id}.pdf']
    subprocess.run(cmd, input=template.encode(), timeout=5, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return send_file(f'data/{file_id}.pdf', download_name='receipt.pdf')


# 内部用エンドポイントを想定したもの
@app.route('/internal', methods=['GET'])
def internal():
    if request.remote_addr != '127.0.0.1':
        return 'internal access only'

    return 'This is an internal page'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
