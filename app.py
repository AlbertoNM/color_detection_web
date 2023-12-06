from flask import Flask, render_template, Response
import cv2

app = Flask(__name__, static_folder="css/")

# def generate():
    
#     cap = cv2.VideoCapture(0)

#     while True:
        
#         ret, frame = cap.read()
#         frame = cv2.flip(frame, 1)
        
#         if ret:
#             (flag, encodeImage) = cv2.imencode('.jpg', frame)
#             if not flag:
#                 continue
#             yield(b'--frame\r\n' b'Conten-Type: image\jpeg\r\n\r\n' + bytearray(encodeImage) + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/video')
# def video_feed():
#     return Response(generate(),
#             mimetype= 'multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug = True)
    # app.run(host = "0.0.0.0", port = 5000)