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


@app.route('/<subject>/<int:page_number>')
def subject_page(subject, page_number):
    """ Shows a page listing the data specified in the subject variable. """
    return render_template(
        'index.html',
        subjectName=subject,
        subjectData=ctrl.subject_get_data(subject, page_number),
        columnsName=ctrl.columns_name_get(subject),
        pages_number=ctrl.pagination_number_get(subject),
        active_page=page_number
    )


# ----------------------------------------------------- main code -----------------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
