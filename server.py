from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello, World!, This is my new server'
    return render_template('index.html')



@app.route('/<string:page_name>')
def html_page (page_name):
    return render_template(page_name)


def write_to_csv(data):
    name=data['email']
    sub = data['subject']
    msg = data['message']
    with open('database.csv', mode='a', newline='')as database2:
        csv_writer= csv.writer (database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,sub,msg])


def write_to_file(data):
    name=data['email']
    sub = data['subject']
    msg = data['message']
    with open('database.txt', mode='a')as database:
        file= database.write(f'\n{name}, {sub}, {msg}')


@app.route('/submit_form', methods=['POST', 'GET'])  # post means the browser want us to save data and it won't show in the url unlike get which mean browser want us to send data
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html', name=data['email'])

        # email=request.form.get('email')
        # subject=request.form.get('subject')
        # msg=request.form.get('message')
        #return render_template('thankyou.html', name =email,sub=subject, msg=msg)

    else:
        return 'Something went wrong, please try again'
# we can create a decorate rout for each page we call or doas above which is more flixbile and dynamic
# @app.route('/index.html')
# def my_home_page():
#     return render_template('index.html')
#
# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def my_components():
#     return render_template('components.html')


# @app.route('/<username>/<int:post_id>')
# def say_my_name(username=None, post_id=0):
#     return render_template('index.html', name=username, post_id=post_id)
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/blog')
# def blog():
#     return 'This is my blog'
#
#
# @app.route('/blog/2020/dogs')
# def blog_dogs():
#     return 'This is my dog!'
