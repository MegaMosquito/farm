from flask import Flask, send_file, render_template, redirect, url_for
import requests

BIND_ADDRESS = '0.0.0.0'
BIND_PORT = 5000
app = Flask(__name__)

PRINTERS = {
  "Sidewinder": {
    "name": "Artillery Sidewinder X1",
    "photo": "Sidewinder.png",
    "control_url": "http://192.168.123.80",
    "cam_url_1": "http://192.168.123.82:8080",
    "cam_url_2": "http://192.168.123.81:8080/?action=stream",
    "light_api_init": "http://192.168.123.82:7777/neopixel/v1/init/21/24",
    "light_api_toggle": "http://192.168.123.82:7777/neopixel/v1/toggle"
  },
  "Genius": {
    "name": "Artillery Genius",
    "photo": "Genius.png",
    "control_url": "http://192.168.1.1",
    "cam_url_1": "http://192.168.1.1",
    "cam_url_2": "http://192.168.1.1",
    "light_api_init": "http://192.168.1.1:7777",
    "light_api_toggle": "http://192.168.1.1:7777"
  }
}

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html', printers=PRINTERS)

@app.route('/favicon.ico', methods=['GET'])
def send_favicon():
  return send_file('/favicon.ico')

@app.route('/printer/<printer_id>', methods=['GET'])
def printer_detail(printer_id: str):
  printer = PRINTERS.get(printer_id)
  if not printer:
    return "Printer not found", 404
  return render_template('printer.html', printer=printer, printer_id=printer_id)

if __name__ == '__main__':
  app.run(host=BIND_ADDRESS, port=BIND_PORT, debug=True)

