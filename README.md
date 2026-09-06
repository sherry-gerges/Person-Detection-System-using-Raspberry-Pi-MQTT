# Person Detection System using Raspberry Pi and MQTT

## 📌 Project Overview

This project is a simple **Person Detection IoT System** built using a **Raspberry Pi**, a **Line Sensor**, and **MQTT**.

The system continuously monitors the sensor to detect whether a person is present. The detection status is published to an MQTT topic using **HiveMQ Cloud**, allowing other IoT devices or applications to receive the sensor data remotely.

---

## 🛠️ Technologies Used

* Raspberry Pi
* Python
* GPIO Zero
* Line Sensor
* MQTT
* Paho MQTT
* HiveMQ Cloud
* SSL/TLS

---

## 🔌 Components

* Raspberry Pi
* Line Sensor
* Jumper Wires
* Internet Connection

### GPIO Connection

| Component   | Raspberry Pi GPIO |
| ----------- | ----------------- |
| Line Sensor | GPIO 17           |

---

## ⚙️ How It Works

1. The Raspberry Pi initializes the Line Sensor connected to **GPIO 17**.
2. The program connects securely to **HiveMQ Cloud** using MQTT over TLS.
3. The sensor value is read continuously.
4. The detected value is published to the MQTT topic:

```text
SIC/support
```

5. If a person is detected, the system:

   * Prints `Person detected`
   * Publishes `Person detected` to the MQTT topic.

6. If no person is detected, the system:

   * Prints `No person detected`
   * Publishes `No Person detected` to the MQTT topic.

7. The system checks the sensor every **3 seconds**.

---

## 📡 MQTT Configuration

The project uses **HiveMQ Cloud** as the MQTT broker.

The connection uses:

* **Protocol:** MQTT
* **Port:** `8883`
* **Security:** SSL/TLS
* **Authentication:** Username & Password
* **Topic:** `SIC/support`

> ⚠️ Never upload your real MQTT password to GitHub. Store credentials securely using environment variables or a separate configuration file.

---

## 📦 Required Python Libraries

Install the required libraries using:

```bash
pip install paho-mqtt gpiozero
```

The project also uses Python's built-in:

```python
ssl
time
signal
```

---

## ▶️ Running the Project

After connecting the Line Sensor to GPIO 17, run:

```bash
python3 main.py
```

The terminal will display either:

```text
Person detected
```

or:

```text
No person detected
```

The corresponding status is also sent through MQTT.

---

## 📁 Project Structure

```text
Person-Detection-MQTT/
│
├── main.py
└── README.md
```

---

## 🚀 Future Improvements

Possible improvements include:

* Adding an LCD to display the detection status.
* Adding LEDs for visual indication.
* Sending notifications when a person is detected.
* Creating a web dashboard to display real-time MQTT data.
* Storing detection events in a database.
* Adding multiple sensors for more accurate detection.

---

👩‍💻 Author

Sherry Gerges

Electrical Engineering Student

Interested in:

IoT
Embedded Systems
Communication Systems
Python
Raspberry Pi

---

## 📄 License

This project is created for educational and IoT learning purposes.
