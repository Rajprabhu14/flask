from flask import Flask, redirect, url_for, request, render_template, make_response, session
app = Flask(__name__)
app.secret_key = 'rajprabhu'
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template("index.html", user_check=True, username=username )
    return render_template("index.html", user_check=False)
@app.route('/hello/')
def hello_world():
    return '<html><body><h1>Hello World</h1></body></html>'
app.add_url_rule('/', 'test/', hello_world)
@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)

@app.route('/score/<int:mark>/')
def score_sheet(mark):
    return render_template('score.html', score= mark)

@app.route('/python/')
def show_python():
    return 'welcome Python'

@app.route('/flask')
def show_flask():
    return 'welcome flask'

@app.route('/admin')
def hello_admin():
    return 'Hello Admin!'

@app.route('/user/<guest>/')
def hello_guest(guest):
    return 'Hello %s' % guest

@app.route('/user/<name>/')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

@app.route('/success/<name>/')
def success(name):
    return 'Welcome %s!' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        print(session['username'])
        return redirect(url_for('index'))
    return '''
      <form action = "" method = "post">
        <p><input type="text" name="username"/></p>
        <input type="submit" value="Login"/>
      </form>
    '''
    # if request.method == 'POST':
    #     user = request.form['nm']
    #     return redirect(url_for('success', name=user))
    # else:
    #     user = request.args.get('nm')
    #     return redirect(url_for('success', name=user))

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == 'POST':
        # dict = {'Physics': 197, 'Chemistry': 195, 'Maths': 200}
        dict = request.form
        resp = make_response(render_template('result.html', result=dict))
        resp.set_cookie('name', dict["Name"])
        return resp

@app.route('/student/')
def student():
    return render_template('student.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
