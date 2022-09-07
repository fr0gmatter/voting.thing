from bottle import route, run, request, response, template
import uuid

# ELECTORAL_ROLL_SERVICE="http://aec.fr0g.ovh:5000/"

apikey="A1njklfs"
electionkey="E2nmlaskle"

box={}
# load a box from disk, or use a script to populate a
# bunch of random names

@route('/')
def homepage():
    return template('template/BallotBox.tpl', version="0.0.1", apikey=apikey, electionkey=electionkey)

@route('/lodge', method='POST')
def lodge_vote():
    global box    # declare global variable to put votes in
    # This microservice:
    # 1. accepts any valid json object.
    # 2. stores it in a box
    # 3. returns a REST response
    #
    # If an object is invalid, reject the post.
    #
    akey = request.POST.get('apikey')
    ekey = request.POST.get('electionkey')
    if ( akey != apikey ):
        return '{ "code": "fail", "msg": "unauthorised" }'
    if ( ekey != electionkey ):
        return '{ "code": "fail", "msg": "invalid election" }'
    transaction_id = str( uuid.uuid4() )
    print( "receipt no: ", transaction_id )
    box[transaction_id] = request.POST.get('ballotpaper')
    print("stored: " , box[transaction_id] )
    return transaction_id

@route('/dump', method='POST')
def dump():
    akey = request.POST.get('apikey')
    if ( akey != apikey ):
        return '{ "code": "fail", "msg": "unauthorised" }'
    return( box )

run(host='0.0.0.0', port=5002, debug=True, reloader=True)
