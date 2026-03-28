<script>
    /**
    * Quarto xAPI Tracker 2026
    * Verstuurt anonieme interacties naar de PHP-proxy.
    */

    // Deze placeholders worden tijdens de GitHub Action vervangen door echte waarden
    const proxyUrl = "PROXY_URL_PLACEHOLDER";
    const proxyKey = "PROXY_KEY_PLACEHOLDER";

    const xapiTracker = {
        // Verstuur het statement naar de PHP-proxy
        send: function(verbId, verbDisplay) {
        // Stop als de proxy niet is geconfigureerd (bijv. bij lokaal gebruik)
        if (proxyUrl.includes("PLACEHOLDER") || proxyUrl === "") {
            return;
        }

    const statement = {
        "verb": {
        "id": `http://adlnet.gov{verbId}`,
    "display": {"en-US": verbDisplay }
            },
    "object": {
        "id": window.location.href,
    "definition": {
        "name": {"en-US": document.title || "Quarto Page" }
                }
            }
        };

    fetch(proxyUrl, {
        method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    'X-Quarto-Proxy-Key': proxyKey
            },
    body: JSON.stringify(statement)
        }).catch(err => console.warn("xAPI Tracking error:", err));
    },

    // Track het laden van een pagina
    trackPage: function() {
        this.send("experienced", "experienced");
    }
};

    // Initialiseer tracking
    document.addEventListener("DOMContentLoaded", function() {
        xapiTracker.trackPage();

    // Optioneel: Track interacties zoals het klikken op tabbladen/navigatie
    // Quarto sites gebruiken vaak interne navigatie zonder volledige reload
    window.addEventListener('hashchange', function() {
        xapiTracker.trackPage();
    }, false);
});
</script>