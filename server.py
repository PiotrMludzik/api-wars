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
        columnsName=util.prepare_header_names(c.PLANETS_COLUMN_ORDER),
        planetsData=dh.planets_prepare_html_data()
    )


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
