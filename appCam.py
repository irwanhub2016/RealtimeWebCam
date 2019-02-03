from flask import Flask, render_template, Response, request

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

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

def shutdown_server():
    func = request.environ.get('192.168.1.6:80')
    if func is None:
        raise RuntimeError("No Running")
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown()
    shutdown_server()
    return 'Server is shutting down ...'

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=1, threaded=True)
