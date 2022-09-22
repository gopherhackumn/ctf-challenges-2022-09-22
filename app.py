from flask import Flask, abort, render_template_string

app = Flask(__name__)

posts = {
    1: "flag #2 is gopher{leaky_urls}",
    2: "i wrote this blog website all by myself!",
}

@app.after_request
def apply_caching(response):
    response.headers["X-GopherHack-Flag-3"] = "gopher{always_check_the_headers}"
    return response

@app.route("/")
def index():
    return render_template_string("""
        <p>welcome to my blog</p>

        <ul>
            <li><a href="/post/2">first post</a></li>
        </ul>

        <!-- flag #1 is gopher{don't_hide_secrets_in_comments} -->
    """)

@app.route("/post/<int:id>")
def post(id):
    post_contents = posts.get(id)
    if not post_contents: return abort(404)

    return render_template_string(post_contents)
