from flask import render_template, request, current_app, redirect
from pugsley.mc import bp

@bp.route('/mc/')
def mc():
    return redirect("/static/mc/index.html")
