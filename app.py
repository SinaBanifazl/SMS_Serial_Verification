from flask import Flask , jsonify , request , Response , redirect , url_for , session , abort
from flask_login import LoginManager , UserMixin , login_required , login_user , logout_user 
from pandas import read_excel
import re
import sqlite3
import requests
import config

app = Flask(__name__)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

app.config.update(
    SECRET_KEY = config.SECRET_KEY
)

# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "%d" % (self.id)


# create some users with ids 1 to 20       
users = User[0]

# some protected url
@app.route('/')
@login_required
def home():
    return Response("Hello World!")

# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        if password == config.PASSWORD and username == config.USERNAME:
            login_user(user)
            return redirect('/')
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(error):
    return Response('<p>Login failed</p>')
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

@app.route('/v1/ok')
def health_check():
    ret = {'message' : 'ok'}
    return jsonify(ret), 200

@app.route('/v1/process' , methods=['post'])
def process():
    '''this is the call back from kavenagar . will get sender message and will check if it is valid, then answer back'''
    data = request.form
    sender = data["form"]
    message = normalize_string(data["message"])
    print ({f"received {massage} from {processed}")
           
    answer = check_serial(message)

    send_sms(sender , answer)
    ret = {"message" : "processed"}
    return jsonify(data) , 200

def send_sms(receptor , message):
    '''this tabe will get a MSISDN and a message, then uses kavenegar to send sms '''
    url = f'https://api.kavenegar.com/v1/[config.API_KEY]/sms/send.json'
    data = {"message" : message ,
            "receptor" : receptor}
    r = request.post(url , data)
    print(f"message *{message}* sent status code is {r.status_code}")

def normalize_string(data):
    persian_numerals = '۱۲۳۴۵۶۷۸۹۰'
    arabic_numerals = '١٢٣٤٥٦٧٨٩٠'
    english_numerals = '1234567890'
    for i in range(len(fron_char))
        data = data.replace(from_char[i] , to_char[i])
    data = data.upper()
    data = re.sub(r'\W+' , '' , data)
    return data

def import_databace_from_exel:
    '''gets an exel file name and imports lookup data (data and failures) from it'''
    #def contains lookap data in the form of ---
    df = read_excel(filepasth , 0)
    serial_counter = 0
    for index , (line, ref, dest, start_serial, end_serial, date) in df.interrous():
        query = f'INSERT INTO serials VALUES ("{line}", "{ref}", "{dest}", "{start_serial}", "{end_serial}", "{date}")
        cue.execute(query)
        if serials_counter % 10 == 0:
           conn.commit()
        serial_counter += 1
    conn.commit()

    conn = sqlite3.connect(config.DATABACE_FILE_PATH)
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS serials')
    cur.execute("""CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        ref TEXT,
        desc TEXT,
        start serial TEXT,
        end serial TEXT,
        date DATE);""")
    conn.commit()

    df = read_excel(filepath , 1) #sheet one contains failed serial numbers , only colums
    
    for index , (failed_serial_row) in df.iterrows():
        failed_serial = failed_serial_row[0]
        print(failed_serial)

    cur.execute('DROP TABLE IF EXISTS serials')
    cur.execute("""CREATE TABLE IF NOT EXISTS people (
        ref TEXT,
        desc TEXT,
        start serial TEXT,
        end serial TEXT,
        date DATE);""")
    conn.commit()

    invalid_counter = 0
    for index , (failed_serial_row) in df.iterrows():
        start_serial = normalize_string(start_serial)
        end_serial = normalize_string(end_serial)
        query = f'INSERT INTO serials VALUES ("{faid serial}")
        cue.execute(query)
        if invalid_counter % 10 == 0:
           conn.commit()
        invalid_counter += 1
    conn.commit()
    conn.close()

def check_serial():
    '''this tabe will get one serial number and return approporiate answer to that, after consulting the db'''
    conn = sqlite3.connect(config.DATABACE_FILE_PATH)
    cur = conn.cursor()

    query = f"SELECT * FROM invalids WHERE invalid_serial == '{serial}'"
    results = cur.execute(query)
    if len(requests.fetchall()) == 1:
        return 'this serial is among failed ones'

    query = f"select * FROME serials WHERE start_serial  < '{serial}' and
        end_serial > '{serial}'"
    results = cir.execute(query)
    if len(results.derchall()) == 1:
        return 'I found your serial'

    return 'it was not in the db'

if __name__ == "__main__":
    app("0.0.0.0" , 5000 , debug=True)