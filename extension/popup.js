const btn = document.getElementById("find");
const outputContainer = document.getElementById("output");

btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Finding length...";
    outputContainer.innerHTML = "";  // Clear previous results

    chrome.tabs.query({ currentWindow: true, active: true }, function(tabs) {
        const url = tabs[0].url;
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "https://yt-2znm.onrender.com/summary?url=" + url, true);
        xhr.responseType = 'json';

        xhr.onload = function() {
            if (xhr.status === 200) {
                const jsonResponse = xhr.response;
                let htmlString = "";

                for (const key in jsonResponse) {
                    if (jsonResponse.hasOwnProperty(key)) {
                        htmlString += key + ": " + jsonResponse[key] + "<br>";
                    }
                }

                outputContainer.innerHTML = htmlString;
            } else {
                outputContainer.innerHTML = "Error: Unable to fetch playlist information.";
            }

            btn.disabled = false;
            btn.innerHTML = "Find Length";
        }

        xhr.onerror = function() {
            outputContainer.innerHTML = "Error: Unable to connect to the server.";
            btn.disabled = false;
            btn.innerHTML = "Find Length";
        }

        xhr.send();
    });
});
