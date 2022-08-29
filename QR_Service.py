from bottle import route, run, request, response, template
from io import BytesIO
import qrcode
import yaml
import hashlib

registered_keys={}
ballot_url={}
ballot_hash={}
data_file_name="datafile.yml"
BASEURL="http://127.0.0.1:5000/election/"

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


#@route('/<key>')
def get_value(key):
    if key in registered_keys.keys():
        return registered_keys[key]
    else:
        return "Fail. " + str(key) + " not registered"

#@route('/set/<key>', method='POST')
def set_value(key):
    value = request.POST.get('value')
    set_kv( key, value )

#@route('/set', method='POST')
def set_pair():
    value = request.POST.get('value')
    key = request.POST.get('key')
    set_kv(key, value)

def set_kv(key, value):
    print("set_kv()\t", key, "\t", value )
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
    qrdata=""    # string to encode
    if data in registered_keys.keys():
        # use the value registered to this key
        qrdata=registered_keys[data]
    else:
      	# use the key
        qrdata=data
        # or throw an error
        #return( "Key not registered: ", data)
    print( "generating QR code with data: ", qrdata)
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
    #print( "handle_qr_form(): ", value )
    return qr(value)

## vote-specific endpoints
@route('/register', method='GET')
def registerget():
    # GET. display a registration page
    # POST. process the registration form
    return template('template/register.tpl')


@route('/register', method='POST')
def registerpost():
    # POST. process the registration form
    label = request.POST.get('label')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    EV = request.POST.get('EV')
    storage_payload = {}
    storage_payload['EV']=EV
    storage_payload['fname']=fname
    storage_payload['lname']=lname
    #print( "storing at key:\t", label, "\t", storage_payload)
    set_kv(label, storage_payload)
    return( "OK")


@route('/get_vote_link', method='GET')
def get_vote_link():
    # GET. display a registration page
    # POST. process the registration form
    return template('template/get_vote_link.tpl')

def generate_url(label):
    global BASEURL
    global ballot_url
    string_to_hash = str(registered_keys[label])
    result = hashlib.md5(string_to_hash.encode())
    result = result.hexdigest()
    print( "hash: ", result )
    url = BASEURL + result
    print( "url: ", url)
    ballot_url[label]=url
    ballot_hash[label]=result
    print( ballot_url )
    return( url )

@route('/votingthing/get_vote_link', method='POST')
def vtget_vote_link_post():
    # GET. display a registration page
    # POST. process the registration form
    label = request.POST.get('label')
    generate_url(label)   # stored in ballot_url so we don't need the return value
    if label in registered_keys:
        registered_keys[label]['link_given']=True
        return qr( ballot_url[label])
    else:
        return( "invalid id. key ", label, " not found in the datastore")

@route('/votingthing/check', method='POST')
def vtcheck_post():
    hash = request.POST.get('hash')
    print( ballot_url.values() )
    if hash in ballot_hash.values():
        return("OK")
    else:
        return("INVALID")

load_database()
run(host='localhost', port=5000, debug=True, reloader=True)
