from flask import Flask , jsonify , request
app = Flask(__name__)


@app.route('/v1/process' , methods=['post'])
def process():
    '''this is the call back from kavenagar . will get sender message and will check if it is valid, then answer back'''
    data = request.form
    sender = data["form"]
    message = data["message"]
    print ({f"received {massage} from {processed}")
    ret = {"message" : "processed"}
    return jsonify(data) , 200

def send_sms():
    pass

def check_serial():
    pass