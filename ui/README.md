The Bartendro UI requires the following pieces of software to be installed:

werkzeug - http://werkzeug.pocoo.org/docs/
jinja2 - http://jinja.pocoo.org/docs/
wtforms - http://wtforms.simplecodes.com/

If you're installing into Raspbian then you can get all the dependencies in one go:

apt-get install nginx uwsgi uwsgi-plugin-python python-werkzeug python-jinja2 python-setuptools python-wtforms python-serial python-smbus python-sqlite python-sqlalchemy memcached python-memcache python-rpi.gpio python-flask sqlite3

If you'd like to have python dependencies installed with pip:

pip install flask flask-sqlalchemy wtforms python-memcached pyserial flask-login


Starting Bartendro UI for the first time
========================================

Database
--------

To start Bartendro for the first time, you'll need to copy the bartendro.db.default
file to bartendro.db in the ui directory. This provides a clean database with all
the required tables for you to start playing with.

Starting
--------

Then, once you're ready, run:

   # sudo ./bartendro_server --debug

That should start the server on all interfaces on your machine. Bartendro's WiFi address is 
always 10.0.0.1 and the wired ethernet ip address is assigned by DHCP. To see the addresses
for Bartendro, see the Network Info box on the options page.

Software only mode
------------------

If you're running the code on anything but a Raspberry Pi connected to full Bartendro hardware,
you'll need to do:

   # sudo ./bartendro_server --debug --software-only

Otherwise the software will attempt to communicate with the hardware that isn't present
and fail. In the software only mode the bartendro UI will run an attempt to do everything
it can, short of actually communicating with the hardware. If you are running in
software only mode, you do no need to run the bartendro_server.py program under sudo. Sudo
rights are only needed to communicate with the hardware.

Nginx
-----

To have Nginx present Bartendro on localhost:8080, you'll need to copy (or symlink) the nginx config in ui/nginx/bartendro.conf to /etc/nginx/conf.d/

Access Bartendro and Espresso
-----------------------------

Bartendro is available at http://localhost:8080
Espresso is available at http://localhost:8080/espresso
