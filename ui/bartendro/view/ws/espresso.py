# -*- coding: utf-8 -*-
import logging
from time import sleep
from werkzeug.exceptions import ServiceUnavailable
from bartendro import app, db, mixer
from flask import Flask, request
from flask.ext.login import current_user
from bartendro.model.drink import Drink
from bartendro.model.booze import Booze
from bartendro.model.dispenser import Dispenser
from bartendro.form.booze import BoozeForm
from bartendro import fsm
from bartendro.error import BartendroBusyError, BartendroBrokenError, BartendroCantPourError, BartendroCurrentSenseError
from bartendro.router.driver import MOTOR_DIRECTION_FORWARD, MOTOR_DIRECTION_BACKWARD

log = logging.getLogger('bartendro')


@app.route('/ws/espresso/pour/<int:disp>')
def ws_pour_espresso(disp):
    if app.globals.get_state() == fsm.STATE_ERROR:
        return "error state"

    dispenser = db.session.query(Dispenser).filter_by(id=disp).first()
    if not dispenser:
        return "Cannot test dispenser. Incorrect dispenser."

    try:
        app.mixer.dispense_ml(dispenser, app.options.test_dispense_ml)
    except BartendroBrokenError:
        raise InternalServerError

    return ""
