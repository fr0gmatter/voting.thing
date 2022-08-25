from bottle import route, run, request, response, template
from io import BytesIO
import qrcode
import yaml

registered_keys={}
data_file_name="datafile.yml"

def load_database():
        global registered_keys
        print( "Loading database from disk")
        try:
            with open( data_file_name, 'r' ) as file:
                registered_keys = yaml.safe_load( file )
        except:
            print("Skipping load. Cannot open data file: ", data_file_name )

def save_database():
    print( "db:", registered_keys )
    f = open( data_file_name, 'w' )
    yaml.dump( registered_keys, f, allow_unicode=True )
    f.close()


@route('/dump')
def dump():
    response.set_header('Content-Type', 'application/json')
    return registered_keys

@route('/<key>')
def get_value(key):
    if key in registered_keys.keys():
        return registered_keys[key]
    else:
        return "Fail. " + str(key) + " not registered"


@route('/set/<key>', method='GET')
def serve_set_one_form(key):
    return template('template/set.tpl', key=key, key_input=str('value=' + key + ' disable'))


@route('/set', method='GET')
def serve_set_form():
    return template('template/set.tpl', key_input="")


@route('/set/<key>', method='POST')
def set_value(key):
    print("set_value()")
    value = request.POST.get('value')
    set_kv( key, value )

@route('/set', method='POST')
def set_endpoint():
    print("set_endpoint()")
    value = request.POST.get('value')
    key = request.POST.get('key')
    set_kv(key, value)

def set_kv(key, value):
    print("set_kv()\t", key, "\t", value )
    #    try:
#    value = request.POST.get('value')
#    key = request.POST.get('key')
#    except:
#        return "Fail. Need to post a 'value'"
    assert isinstance(value, object)
    print("value: " , value )
    if value != None:
        registered_keys[key] = value
        print( registered_keys )
        save_database()
    else:
        return "Fail. Need to post a 'value'"


@route('/qr/<data>')
def qr(data):
    qrdata=""
    if data in registered_keys.keys():
        # use the value registered to this key
        #print( "generating QR code for: ", grdata)
        qrdata=registered_keys[data]
    else:
        # use the key
        qrdata=data
        #return( "Key not registered: ", data)
    print( "generating QR code for: ", qrdata)
    membuf = BytesIO()
    img = qrcode.make(qrdata)
    img.save(membuf, format="png")
    response.set_header('Content-Type', 'image/png')
    return membuf.getvalue()


@route('/qr', method='GET')
def serve_qr_form():
    return template('template/qr.tpl', key_input="")

@route('/qr', method='POST')
def handle_qr_form():
    value = request.POST.get('value')
    print( "handle_qr_form(): ", value )
    return qr(value)

load_database()
run(host='localhost', port=5000, debug=True, reloader=True)
