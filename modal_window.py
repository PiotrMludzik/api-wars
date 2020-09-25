# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                         modal window: html code for injection
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from yattag import Doc


def html_table_prepare(data):
    """ Returns a string that contains html code with data. """
    doc, tag, text = Doc().tagtext()

    with tag('h2'):
        text('Hello world!')

    return doc.getvalue()


    # <table class="table table-bordered table-striped">
    #     <thead class="table-dark">
    #         <tr>
    #             <th>
    #
    #             </th>
    #         </tr>
    #     </thead>
    #     <tbody>
    #         <tr>
    #             <td class="{{ r_column_name }}">
    #
    #             </td>
    #         </tr>
    #     </tbody>
    # </table>
