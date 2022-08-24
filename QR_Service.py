from bottle import route, run, response
from io import BytesIO
import qrcode

@route('/hello')
def hello():
    return "Hello World!"

@route('/qr/<data>')
def qr(data):
    membuf = BytesIO()
    img = qrcode.make(data) 
    img.save(membuf, format="png")
    response.set_header('Content-Type', 'image/png')
    return membuf.getvalue()
 
run(host='localhost', port=5000, debug=True)
