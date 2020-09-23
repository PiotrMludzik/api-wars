// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                                     client: DOM
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

import {c} from './constants.js'
import {dataHandler as dh} from "./data_handler.js";
import {modal} from "./modals.js";


export let dom = {
    buttonData: {
        initEventListener: function () {
            // Inits event listeners for the button's data.
            const buttons = document.querySelectorAll('.button-data');
            buttons.forEach(button => {
                button.addEventListener('click', this.click)
            });
        },
        click: function (event) {
            // Click event on the button data.
            event.preventDefault();
            const button = event.target;
            const buttonData = buttonDataGet(button);

            dh.apiPost(c.api.URL, dh.prepareRequestData(buttonData[c.key.data]), data => {
                console.log(data);  // NOTE: the development code.
            });

            // modal.Data(button, buttonData);  // TODO: put this line into callback fuction above.

            function buttonDataGet (button) {
                // Collects the data necessary to display the modal window.
                let buttonData = {};
                buttonData[c.key.recordName] = button.dataset.recordName;
                buttonData[c.key.columnName] = button.dataset.columnName;
                buttonData[c.key.data] = button.dataset.data;

                return buttonData;
            }
        }
    }
}