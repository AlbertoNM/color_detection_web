from src import *

#* variable del servidor
app = Flask(__name__, static_folder="css/")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video_feed():
    return Response(generate(), mimetype= 'multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host = "0.0.0.0", port = 5005)
