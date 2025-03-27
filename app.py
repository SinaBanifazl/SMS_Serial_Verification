from flask import Flask , jsonify , request
from pandas import read_excel
import requests
import config
app = Flask(__name__)


@app.route('/v1/process' , methods=['post'])
def process():
    '''this is the call back from kavenagar . will get sender message and will check if it is valid, then answer back'''
    data = request.form
    sender = data["form"]
    message = data["message"]
    print ({f"received {massage} from {processed}")
    send_sms(sender , 'hi ' + message)
    ret = {"message" : "processed"}
    return jsonify(data) , 200

def send_sms(receptor , message):
    '''this tabe will get a MSISDN and a message, then uses kavenegar to send sms '''
    url = f'https://api.kavenegar.com/v1/[config.API_KEY]/sms/send.json'
    data = {"message" : message ,
            "receptor" : receptor}
    r = request.post(url , data)
    print(f"message *{message}* sent status code is {r.status_code}")

def import_databace_from_exel:
    '''gets an exel file name and imports lookup data (data and failures) from it'''
    #def contains lookap data in the form of ---
    df = read_excel(filepasth , 0)
    for index , (line, ref, dest, start_serial, end_serial, date)
        print(line, ref, dest, start_serial, end_serial, date)

    df = read_excel(filepath , 1)
    #sheet one contains failed serial numbers , only colums
    for index , (failed_serial_row) in df.iterrows():
        failed_serial = failed_serial_row[0]
        print(failed_serial)

def check_serial():
    pass

if __name__ == "__main__":
    app("0.0.0.0" , 5000 , debug=True)