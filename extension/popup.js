const btn = document.getElementById("find");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Finding length...";
    chrome.tabs.query({ currentWindow: true, active: true }, function(tabs) {
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "https://yt-2znm.onrender.com/summary?url=" + url, true);
        xhr.responseType = 'json';
        xhr.onload = function() {
            var jsonResponse = xhr.response;
            var htmlString = "";
            for (var key in jsonResponse) {
                if (jsonResponse.hasOwnProperty(key)) {
                    htmlString += key + ": " + jsonResponse[key] + "<br>";
                }
            }
            const p = document.getElementById("output");
            p.innerHTML = htmlString;

            btn.disabled = false;
            btn.innerHTML = "Find Length";
        }
        xhr.send();
    });
});
