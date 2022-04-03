from flask import Flask, render_template, request, redirect,  url_for
from datetime import date
posts = [{'author': 'Alina',
          'title': 'Article1',
          'content': 'First blog app',
          'date':'01-01-01'
         },
         {'author': 'Ivan Ivanov',
          'title': 'Article2',
          'content': 'First blog app2',
          'date':'02-02-02'
          },
         {'author': 'Petr petrov',
          'title': 'Article3',
          'content': 'First blog app3',
          'date':'03-03-03'
          }] 

app = Flask(__name__)

@app.route("/")
@app.route("/main_page")
def main_page():
    return render_template('main_page.html', posts=posts)


@app.route("/post/<title>")
def post_page(title):
    index = [post['title'] for post in posts].index(title)
    return render_template('post.html', post=posts[index])


@app.route("/post/new_post", methods=['POST', 'GET'])
def new_post():
    d = dict()
    if request.method == 'POST':
        d['author'] = request.form['Author_name']
        d['title'] = request.form['Post_title']
        d['content'] = request.form['content']
        d['date'] = date.today()
        posts.append(d)
        return redirect(url_for('main_page'))
    else:
        return render_template('database.html')

app.run()
