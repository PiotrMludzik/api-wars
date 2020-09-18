# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                   routes handling
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, redirect
import controller as ctrl

app = Flask(__name__)
app.secret_key = '#I\'ll be back!:D'  # encrypt session variables


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
        planetsData=ctrl.planets_get_data(page_number),
        columnsName=ctrl.columns_name_get(),
        pages_number=ctrl.pagination_number_get('planets'),
        active_page=page_number
    )


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
