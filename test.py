from flask import Flask,jsonify,request
app = Flask(__name__)
contacts = [
    {
        'id': 1,
        'Name': 'Kalrav',
        'Contact': '+91 9316588142',
        'Done': False
    },
    {
        'id': 2,
        'Name': 'Archana',
        'Contact': '+91 9825027489',
        'Done': False
    }
]
@app.route('/add-data',methods= ['post'])

def AddTask():
    if not request.json:
        return jsonify({
            'status': 'error',
            'Message': 'Please Provide The Data'        
            },404)
    contact = {
            'id': contacts[-1]['id']+1,
            'Name': request.json['Name'],
            'Contact': request.json.get('Contact',''),
            'Done': False    
    }


    contacts.append(contact)

    return jsonify({
        'status': 'success',
        'message': 'Task Added Successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data': contacts
    })    

if (__name__ == '__main__'):
    app.run(debug = True)