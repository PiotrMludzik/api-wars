// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                                client: data handlers
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

import {c} from './constants.js'


export let dataHandler = {
    apiPost: function (url, requestData, showModalWindow, modalWindowData) {
        // Sends a request and receives response from the server, than calls callback function.
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
            .then(response => response.json())
            .then(responseData => {
                modalWindowData[c.data.key.data] = responseData[c.api.key.header][c.api.key.swapi][c.api.key.response];
                showModalWindow(modalWindowData);
            });
    },
    prepareRequestData: function (rowData) {
        // Prepares the valid request data.
        const preparedData = changeStringToList(rowData);
        return makeDictRequest(preparedData);

        function changeStringToList(data) {
            // Changes a string data to a list.
            return data.split(', ');
        }
        function makeDictRequest(data) {
            // Create a valid dictionary request.
            return {
                [c.api.key.header]: {
                    [c.api.key.swapi]: {
                        [c.api.key.request]: data
                    }
                }
            };
        }
    }
}