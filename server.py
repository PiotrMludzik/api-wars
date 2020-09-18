# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                   routes handling
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, redirect
import controller as ctrl

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
        columnsName=ctrl.get_columns_name(),
        planetsData=ctrl.planets_get_data(page_number)  # Fixme: get planets' data from actual page
    )


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
