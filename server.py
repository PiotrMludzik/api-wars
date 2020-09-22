# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                   routes handling
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, redirect
import controller as ctrl
import data_constants as dc
import utilities as util


app = Flask(__name__)
app.secret_key = '#I\'ll be back!:D'  # encrypt session variables


# ---------------------------------------------------- main route -----------------------------------------------------

@app.route('/')
def index():
    """ Shows starter page. """
    return redirect('/planets/1')


@app.route('/<subject>/<int:page_number>')
def subject_page(subject, page_number):
    """ Shows a page listing the data specified in the subject variable. """
    subject_data = ctrl.data_get(subject, page_number)
    button_data = ctrl.button_data_get(subject, subject_data)

    return render_template(
        'index.html',
        subjects_list=dc.SUBJECT_ORDER,
        subject_name=subject,
        subject_data=subject_data,
        button_data=button_data,
        column_names=ctrl.column_names_get(subject),
        pages_number=ctrl.pagination_number_get(subject),
        page_active=page_number
    )


# ----------------------------------------------------- api route -----------------------------------------------------

@app.route('/<subject>', methods=['POST'])
@util.json_response
def api_data(subject):
    pass


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
