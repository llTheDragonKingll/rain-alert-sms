# 🌧️ Rain Alert SMS Notifier (Python)

A Python automation project that checks weather forecasts using an API and sends an SMS alert if rain is expected in the next few hours.

---

## 🚀 Features

* 🌐 Fetches weather data using OpenWeatherMap API
* 🌧️ Detects rain based on weather condition codes
* 📱 Sends SMS alerts using Twilio
* ⏱️ Checks upcoming hours (next 12 hours forecast)

---

## 🛠️ Tech Stack

* Python
* Requests (API calls)
* Twilio (SMS service)

---

## 📂 Project Structure

```
rain-alert/
│
├── main.py
└── README.md
```

---

## ⚙️ How to Run

1. Clone the repository
2. Install required libraries:

```
pip install requests twilio
```

3. Open `main.py` and update the following values:

---

## 🔧 Required Configuration

Replace the placeholders in `main.py`:

```python
api_key = "YOUR_API_KEY"
account_sid = "YOUR_TWILIO_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

FROM_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
TO_NUMBER = "YOUR_PHONE_NUMBER"
```

---

### 📍 Location (optional, already set to MUMBAI)

```python
LATITUDE = 19.075983
LONGITUDE = 72.877655
```

👉 You can change these values to your own location if needed.

---

## 📌 Notes

* This project uses **OpenWeatherMap API** for weather data
* Rain is detected using weather condition codes (< 700)
* SMS is sent only if rain is expected
* API keys and phone numbers are not included for security reasons

---

## ⭐ Acknowledgement

Built as part of my Python learning journey.

---

⭐ If you like this project, consider giving it a star!
