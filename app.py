import logging
from chalice import Chalice

app = Chalice(app_name='loopmoon-api')
app.log.setLevel(logging.DEBUG)
app.debug = True


@app.route('/')
def index():
    return {'hello': 'worldd'}


@app.route('/event', methods=['POST'])
def event():
    request = app.current_request
    event = request.json_body

    # Respond appropriate to Slack request URL challenge
    if event['type'] == 'url_verification':
        return {'challenge': event['challenge']}
