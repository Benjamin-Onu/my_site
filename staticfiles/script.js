const searchBtn = document.querySelector(".search-container #Search-btn");
const searchInput = document.querySelector(".search-container .search-input");
console.log(searchBtn, searchInput);

searchBtn.addEventListener('click', function(){
    // searchInput.classList.add("active-search");
    searchInput.classList.toggle("active-search");    
    console.log(searchInput);
})

// document.querySelector('main').addEventListener('click', () => {
//     searchInput.classList.remove("active-search");
// })


let searchFunc = () => {
    console.log("search function called");

    let searchInputValue = searchInput.value.trim();
    console.log(searchInputValue);

    // USING AJAX TO GET DATA FROM SERVER
    // Create a new XMLHttpRequest object
    // define the URL and the HTTP method (GET or POST). It's a GET request because we're requesting a page.

    // Set the response type to JSON.

    let http = new XMLHttpRequest();
    http.responseType = "json";
    let url = "http://localhost:8000/search/" + searchInputValue;
    /**
     * The url could look like this:
    http://localhost:8000/search/searchInputValue

    This would make a request to the server to get data based on the search input value.

    We're using the GET method to retrieve data from the servser.
    In the urls.py file, we've defined a route for the search view, which takes a parameter called "search_term".
    This parameter is passed to the view function and used to query the database for matching results.
     */
    http.open("GET", url, true);
    //The first argument sets the http method.
    //In the second argument, we pass the file where our data lives.
    //The last argument sets the request to be async.

    /*
    The url could look like this:
    http://localhost:8000/search/searchInputValue

    This 
    */
    http.send();

    http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            console.log(response);
            let results = document.querySelector('.search-results');
            results.innerHTML = "";
            // Loop through the response array and create an article element for each result.
            response.forEach(result => {
                let article = document.createElement('article');
                let h2 = document.createElement('h2');
                let p = document.createElement('p');
                h2.textContent = result.title;
                p.textContent = result.content;
                article.appendChild(h2);
                article.appendChild(p);
                results.appendChild(article);
            });
        }
    }
}

searchBtn.addEventListener('click', searchFunc);


// Send the form data to the server using AJAX
// Create a new XMLHttpRequest object
// define the URL and the HTTP method (POST). It's a POST request because we're sending data to the server.

// Set the response type to JSON.

// Send the form data using the send() method.

// Handle the response from the server using the onreadystatechange event.
