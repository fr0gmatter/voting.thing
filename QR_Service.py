from bottle import route, run, request, response
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

@route('/set/<key>', method='POST')
def set(key):
#    try:
    value = request.POST.get('value')
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
    if data in registered_keys.keys():
        # use the value registered to this key
        qrdata=registered_keys[data]
    else:
        # use the key
        #qrdata=data
        return( "Key not registered: ", data)
    membuf = BytesIO()
    img = qrcode.make(qrdata)
    img.save(membuf, format="png")
    response.set_header('Content-Type', 'image/png')
    return membuf.getvalue()

load_database()
run(host='localhost', port=5000, debug=True, reloader=True)

