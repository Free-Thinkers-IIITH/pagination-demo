from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args
from dblp import fetch_dblp


app = Flask(__name__)
app.template_folder = ''

posts = fetch_dblp('sha',1000) # for testing purposes


def get_posts(offset=0, per_page=10):
    return posts[offset: offset + per_page]


@app.route('/')
def index():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(posts)
    pagination_posts = get_posts(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('index.html',
                           posts=pagination_posts,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


if __name__ == '__main__':
    app.run(debug=True)