const form = document.getElementById('searchForm');
const resultsContainer = document.getElementById('results');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    const searchQuery = formData.get('q');

    if (searchQuery) {
        const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(searchQuery)}`;

        console.clear();
        console.log(`Searching for: ${searchQuery}`);

        fetchSeriesData(apiUrl);
    } else {
        console.log("Please enter a TV series name to search.");
    }
});

async function fetchSeriesData(url) {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        console.log("--- API Search Results (JSON Data) ---");
        console.log(data);

        displayResults(data);

    } catch (error) {
        console.error("Fetch error:", error.message);
        resultsContainer.innerHTML = `<p style="color: red;">Error fetching data: ${error.message}</p>`;
    }
}

function displayResults(data) {
    resultsContainer.innerHTML = '';

    if (data && data.length > 0) {
        data.forEach(item => {
            const show = item.show;

            const article = document.createElement('article');

            const h2 = document.createElement('h2');
            h2.textContent = show.name;
            article.appendChild(h2);

            const link = document.createElement('a');
            link.href = show.url;
            link.textContent = 'View Details';
            link.target = '_blank';
            article.appendChild(link);

            const img = document.createElement('img');
            const imageUrl = show.image?.medium || 'https://via.placeholder.com/210x295?text=No+Image';

            img.src = imageUrl;
            img.alt = show.name;
            article.appendChild(img);

            const summaryDiv = document.createElement('div');
            summaryDiv.innerHTML = show.summary || '<p>No summary available.</p>';
            article.appendChild(summaryDiv);

            resultsContainer.appendChild(article);
        });
    } else {
        resultsContainer.innerHTML = '<p>No TV series found for your query.</p>';
    }
}