# -*- coding: utf-8 -*-
import time
from bartendro import app
from flask import render_template


@app.route('/espresso')
def espresso():

    return render_template("espresso", title="Serve Espresso", options=app.options)


@app.route('/espresso/config')
def espresso_config():

    return render_template("espresso_config", title="Configure Espresso", options=app.options)