import requests
from datetime import date
def send_request(hostname, score):
    # Data
    data = {
        'hostname': hostname,
        'training_score': score,
        'training_finish': date.today()

    }

    # Custom headers
    headers = {
        'content-type': 'multipart/form-data'
    }

    # Get response from server
    try:
        response = requests.post('http://10.20.195.140/info_collector', data=data)
    except:
        print("An exception occurred")