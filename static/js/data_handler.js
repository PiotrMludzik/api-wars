// --------------------------------------------------------------------------------------------------------------------
//                                                       API Wars
//                                                client: data handlers
//                                                        v 1.0
// --------------------------------------------------------------------------------------------------------------------

export let dataHandler = {
    api_post: function (url, data, callback) {
        // Sends the data to the API, and calls callback function
        fetch(url, {
            method: 'POST',
            body: JSON.stringify(data),
            credentials: 'same-origin',
            contentType: 'application/json'
        })
            .then(response => response.json())  // parse the response as JSON
            .then(json_response => callback(json_response));
    }
}