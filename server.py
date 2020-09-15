# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                   routes handling
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import Flask, redirect, render_template
import data_handler as dh
import utilities as util
import constants as c

app = Flask(__name__)


# ---------------------------------------------------- main route -----------------------------------------------------

@app.route('/')
def index():
    """ Shows main page with the planets' list. """
    return render_template(
        'index.html',
        columns_order=c.PLANETS_COLUMN_ORDER,
        columns_name=util.prepare_header_names(c.PLANETS_COLUMN_ORDER),
        planets_data=dh.get_planet_data()
    )


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
