
---

# DDoS Protection and Mitigation System

## Innovative Design Lab Phase 2

A Real-Time DDoS Detection and Mitigation System built using Python and Flask. This project monitors incoming traffic, detects abnormal request spikes, generates alerts, and optionally blocks malicious IP addresses through an interactive web dashboard.

---

## 📌 Project Overview

Distributed Denial of Service (DDoS) attacks can overwhelm servers by sending excessive requests, making services unavailable to legitimate users.

This project provides a lightweight and customizable solution that:

* Monitors requests per IP address in real time
* Detects abnormal traffic based on configurable thresholds
* Generates alerts for suspicious activity
* Automatically blocks malicious IP addresses (optional)
* Provides blacklist and whitelist management
* Displays live traffic statistics and charts

---

## 🚀 Features

* Real-time per-IP request monitoring
* Configurable maximum requests per second
* Adjustable sensitivity levels
* Auto-block functionality
* Blacklist and Whitelist management
* Live dashboard with traffic graph
* Recent alert display
* Attack simulation module for testing
* REST APIs for stats and monitoring

---

## 🛠️ Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* Flask-CORS
* SQLite
* HTML, CSS, JavaScript

---

## 🏗️ System Architecture

1. Flask Web Application (Frontend + Backend)
2. DDoS Detection Engine
3. SQLite Database
4. Monitoring Dashboard
5. Attack Simulation Script

The detection engine tracks requests per second for each IP address and compares them against configurable thresholds. If the limit is exceeded, alerts are generated and IPs can be automatically blocked.

---

## 📂 Project Structure

```
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── db.py               # Database models
├── ddos_engine.py      # Detection logic
├── simulate.py         # Attack simulation script
├── state.py            # Alert state management
├── requirement.txt     # Dependencies
├── templates/          # HTML templates
└── static/             # CSS, JS, assets
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirement.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧪 Running the Attack Simulation

To test the detection system:

```bash
python simulate.py
```

This script sends multiple rapid requests to simulate a DDoS attack.
You will see:

* Traffic spike on the dashboard
* Alert generation
* IP blocking (if auto-block is enabled)

---

## 🔐 How It Works

* Each incoming request is counted per IP per second.
* The system checks the configured threshold.
* If the request rate exceeds the limit:

  * An alert is generated.
  * The IP is blocked (if auto-block is enabled).
* Whitelisted IPs bypass detection logic.
* Blacklisted IPs are instantly blocked.

---

## 🎯 Learning Outcomes

This project demonstrates:

* Backend development using Flask
* API design and routing
* Database modeling using SQLAlchemy
* Real-time traffic monitoring logic
* Cybersecurity threat detection principles
* Modular system design

---

## 👥 Team Members

* Abinav Karthick S
* Kaashi T
* Rohan C S

---

## 📌 Future Enhancements

* Integration with firewall systems
* Machine learning-based anomaly detection
* Deployment on cloud infrastructure
* Role-based authentication system
* Real-time WebSocket monitoring

---

## 📄 License

This project is developed for academic purposes under Innovative Design Lab Phase 2.

---

