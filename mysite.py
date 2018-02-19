from flask import Flask,render_template
#render template uygulama içindeki html dosyasına erişiyor ve çalıştırıyor
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
