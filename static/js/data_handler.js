// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                                client: data handlers
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

import {c} from './constants.js'


export let dataHandler = {
    apiPost: function (url, requestData, showModalWindow) {
        // Sends the data to the API, and calls callback function.
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
            .then(response => response.json())  // parse the response as JSON
            .then(responseData => showModalWindow(responseData));
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
            let dictRequest = {};
            dictRequest[c.api.key] = data;
            return dictRequest;
        }
    }
}