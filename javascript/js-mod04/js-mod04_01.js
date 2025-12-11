const form = document.getElementById('searchForm');

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

        console.log("API Search Results (JSON Data)");
        console.log(data);

        if (data && data.length > 0) {
            console.log("\nParsed Information for Top Result");
            const firstResult = data[0].show;

            console.log(`Title: ${firstResult.name}`);
            console.log(`Summary: ${firstResult.summary ? firstResult.summary.replace(/<[^>]*>?/gm, '').substring(0, 200) + '...' : 'No summary available'}`);
            console.log(`Genres: ${firstResult.genres.join(', ')}`);
            console.log(`Status: ${firstResult.status}`);
            console.log(`Rating: ${firstResult.rating.average || 'N/A'}`);
            console.log(`Link: ${firstResult.url}`);

        } else {
            console.log("No TV series found for your query.");
        }

    } catch (error) {
        console.error("Fetch error:", error.message);
    }
}