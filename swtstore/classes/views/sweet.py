# -*- coding utf-8 -*-
# classes/views/sweet.py


from flask import Module, jsonify, request, render_template, redirect,\
                    url_for, abort, json

from swtstore.classes.models import Context
from swtstore.classes.models import Sweet
from swtstore.classes.models.um import User


sweet = Module(__name__)

@sweet.route('/<id>', methods=['GET'])
def showSweet(id):
    #current_user = User.getCurrentUser()
    #if current_user is None:
    #    return redirect(url_for('index'))

    #user = current_user.to_dict()
    print "recvd sweet id: %s" % (id)
    sweet = Sweet.query.get(id)
    if sweet:
        print "sweet found " + str(sweet)
        return render_template('specific_sweet.html', sweet=sweet)
    else:
        abort(404)


