#!/usr/bin/env python
from flask import Flask, render_template, Response
import binascii
import sys

# emulated camera
from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    response = Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

   # print(sys.getsizeof(gen(Camera()))

    print(sys.getsizeof(response))
    
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
