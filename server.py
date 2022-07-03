from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<username>/<int:post_id>")  # <> is variable
def hello_world(username=None, post_id=None):
    # print(url_for('static', filename='vans.ico'))
    return render_template('index.html', name=username, post_id=post_id)


#
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/works.html")
# def work():
#     return render_template('works.html')
#
#
# @app.route("/blog")
# def blog():
#     return "<p>This is Blog, Hello!</p>"
#
#
# @app.route("/blog/2020/dogs")
# def blog2():
#     return "<p>This is my dog!</p>"

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow((email,subject,message))

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'
