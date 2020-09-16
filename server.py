# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                   routes handling
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, redirect
import constants as c
import controller as ctrl
import utilities as util

app = Flask(__name__)


# ---------------------------------------------------- main route -----------------------------------------------------

@app.route('/')
def index():
    """ Shows starter page. """
    return redirect('/planets/1')


@app.route('/planets/<int:page_number>')
def planets_page(page_number):
    """ Shows page with the planets' list. """
    return render_template(
        'index.html',
        pages_number=3,  # Fixme: implement pages_number
        active_page=page_number,
        columnsName=util.prepare_header_names(c.PLANETS_COLUMN_ORDER),
        planetsData=ctrl.planets_get_data()  # Fixme: get planets' data from actual page
    )


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
