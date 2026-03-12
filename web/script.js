async function fetchWeather(lat, lon) {
    const display = document.getElementById('weather-display');
    try {
        const res = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`);
        const data = await res.json();
        display.innerHTML = `
            <div class="temp">${data.current_weather.temperature}°C</div>
            <p>Wind Speed: ${data.current_weather.windspeed} km/h</p>
        `;
    } catch (e) {
        display.innerHTML = "Error loading weather.";
    }
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (pos) => fetchWeather(pos.coords.latitude, pos.coords.longitude),
            () => fetchWeather(12.97, 77.59) // Default fallback
        );
    }
}

// Auto-run on load
window.onload = getLocation;
