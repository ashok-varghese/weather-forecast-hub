# 🌤️ Global Weather Hub & Auto-Tracker

![GitHub Actions](https://img.shields.io/badge/Automation-GitHub_Actions-blue?logo=githubactions)
![Python](https://img.shields.io/badge/Backend-Python-yellow?logo=python)
![Status](https://img.shields.io/badge/Status-Live-green)

A professional weather dashboard that tracks global weather patterns and automatically updates itself every 24 hours using GitHub Actions.


## 🚀 How it Works
1. **Frontend:** A responsive web dashboard that uses the **Browser Geolocation API** to detect the user's current city and display live weather.
2. **Backend (Automation):** A Python script runs daily via **GitHub Actions** to fetch weather data for a fixed location and logs it to `weather_log.txt`.
3. **Continuous Contribution:** Every daily log update counts as a GitHub contribution, keeping the activity graph active.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Glassmorphism UI), Vanilla JavaScript.
- **Backend:** Python 3.x with `requests` library.
- **Automation:** GitHub Actions (Cron-scheduled workflows).
- **API:** [Open-Meteo](https://open-meteo.com/) (Free, no-key weather data).

## 📂 Project Structure
- `/web`: Contains the landing page files for the custom domain.
- `/api`: Contains the Python logic for daily tracking.
- `.github/workflows`: The automation logic for the "green squares."

## 📈 Contribution Goal
This project is designed to demonstrate proficiency in **CI/CD pipelines**, API integration, and maintaining a consistent development cycle.
