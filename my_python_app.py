from flask import Flask, render_template, request
import socket

app = Flask(__name__)


def scan_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error:
        return "Unable to resolve the hostname."


@app.route('/run-my-python-app')
def run_my_python_app():
    try:
        # Di sini Anda dapat mengeksekusi kode Python yang diinginkan.
        # Contoh: Jalankan fungsi "main()" dari file Python yang Anda inginkan.
        result = main()
        return f"Hasil eksekusi: {result}"
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"


@app.route('/')
def home():
    project_data = {
        'title': 'IP Address Scanner',
        'description': 'This project was created with my team...',
        'image_url': '',
        # Ini mungkin perlu disesuaikan dengan kebutuhan Anda.
        'project_link': '/Projek Jarkom/app.py'
    }
    return render_template('index1.html', project_data=project_data)


@app.route('/scan', methods=['POST'])
def scan():
    website = request.form['website']
    ip_address = scan_ip_address(website)
    return render_template('result.html', website=website, ip_address=ip_address)


@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run()
