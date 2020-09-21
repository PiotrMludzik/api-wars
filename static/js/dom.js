// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                                     client: DOM
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

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
            modal.Data(button, buttonData);

            function buttonDataGet (button) {
                // Collects the data necessary to display the modal window.
                return [button.dataset.recordName, button.dataset.buttonDataName, button.dataset.buttonData];
            }
        }
    }
}