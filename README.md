# 🌧️ Rain Alert SMS Notifier (Python)

A Python automation project that checks weather forecasts and sends an SMS alert if rain is expected.

---

## 🚀 Features

* 🌐 Fetches weather data using OpenWeatherMap API
* 🌧️ Detects rain using weather condition codes
* 📱 Sends SMS alerts using Twilio
* ⏱️ Can be scheduled to run periodically using PythonAnywhere

---

## 🛠️ Tech Stack

* Python
* Requests (API calls)
* Twilio (SMS service)
* PythonAnywhere

---

## 📂 Project Structure

```text
rain-alert-sms/
│
├── main.py
└── README.md
```

---

## ⚙️ How to Run

1. Install required libraries:

```bash
pip install requests twilio
```

2. Open `main.py` and update:

```python
api_key = "YOUR_API_KEY"
account_sid = "YOUR_TWILIO_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

FROM_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
TO_NUMBER = "YOUR_PHONE_NUMBER"
```

3. Run:

```bash
python main.py
```

---

## 💡 Notes

* Uses OpenWeatherMap API for forecast data
* Sends SMS only when rain is expected
* API keys and phone numbers are not included for security
* Can be scheduled on PythonAnywhere for automatic checks

---

## ⭐ About this project

Built while learning Python and experimenting with APIs, automation, and real-world use cases.
