from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Change port as needed
