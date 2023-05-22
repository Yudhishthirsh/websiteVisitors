import csv
from flask import Flask, request, render_template
import parameter

app = Flask(__name__)
ip_addresses = []

@app.route('/')
def index():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip_addresses.append(ip_address)
    column_name = 'IPAddress'
    with open(parameter.fileName, 'a', newline='') as file:
        if file.tell() == 0:
            file.write(column_name + '\n')
        writer = csv.writer(file)
        writer.writerow([ip_address])
        return render_template('index.html', ip_address=ip_address)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)