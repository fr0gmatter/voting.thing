from bottle import route, run, request, response, template
ELECTORAL_ROLL_SERVICE="http://aec.fr0g.ovh:5000/"

@route('/')
def homepage():
    return template('template/home.tpl')

@route('/vote/<key>', method='GET')
def give_ballot_form( key ):
    # TODO: check ELECTORAL_ROLL_SERVICE goes here
    return template('template/vote.tpl', anon_voter_id=key)

@route('/vote/<key>', method='POST')
def lodge_vote( key ):
    # Process the vote form
    # For example, something like:
    #   value = request.POST.get('value')
    #
    # TODO: notify ELECTORAL_ROLL_SERVICE that the vote has been lodged  (optional)
    # TODO: count the vote (optional)
    return template('template/thankyou.tpl', anon_voter_id=key)

run(host='0.0.0.0', port=5001, debug=True, reloader=True)
