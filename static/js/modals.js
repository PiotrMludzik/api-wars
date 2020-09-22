// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                               client: modals components
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

import {c} from './constants.js'
import {utilities as util} from "./utilities.js";


export let modal = {
    Data: function (button, buttonData) {
        // Injects the modal window with the data.
        const modalWindow = modalWindowGet(buttonData);
        const targetElement = document.querySelector('.modal-container');

        targetElement.innerHTML = modalWindow;
        initCleanAfterCloseModalWindow();

        function modalWindowGet(buttonData) {
            // Builds the modal window with a data.
            return `
                <div class="modal fade" id="modal-button-data" tabindex="-1" role="dialog">
                    <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">${util.capitalize(buttonData[c.index.dataName])} of ${buttonData[c.index.recordName]}</h5>
                                <button type="button" class="close" data-dismiss="modal">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                <p>${buttonData[c.index.data]}</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }
        function initCleanAfterCloseModalWindow() {
            // Adds the event listeners fired when close the modal window to cleans a html elements.
            $('#modal-button-data').on('hidden.bs.modal', function () {
                $(this).remove();
            });
        }
    }
}