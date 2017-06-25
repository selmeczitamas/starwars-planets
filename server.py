from flask import Flask, render_template, request, redirect, session
import sql_queries

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    if 'username' in session:
        login_name = 'Logged in as ' + session['username']
        login_button = 'Log Out'
        login_url = '/logout'
        return render_template('index.html', login_name=login_name,
                                             login_button=login_button,
                                             login_url=login_url)
    else:
        login_name = ''
        login_button = 'Log in'
        login_url = '/login'
        return render_template('index.html', login_name=login_name,
                                             login_button=login_button,
                                             login_url=login_url)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = (username, password)
        sql_queries.add_new_user(user_data)
        return redirect('/')
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user_data = (username, password)
            user_check = sql_queries.check_user_login(user_data)
            if user_check[0][0] == username:
                session['username'] = request.form['username']
                return redirect('/')
    except:
        return redirect('/login')
    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=None)
