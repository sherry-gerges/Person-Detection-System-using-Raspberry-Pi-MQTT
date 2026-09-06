# 👤 Person Detection System using Raspberry Pi & MQTT

A simple IoT-based **Person Detection System** built using a **Raspberry Pi**, a **Line Sensor**, and the **MQTT protocol**.

The system continuously monitors the sensor and publishes the detection status to a **HiveMQ Cloud MQTT broker**. This allows another IoT device or application subscribed to the same MQTT topic to receive the sensor data remotely.

---

## 🚀 Features

* Detects whether a person/object is present using a Line Sensor.
* Uses Raspberry Pi GPIO to read the sensor.
* Sends sensor readings using the MQTT protocol.
* Uses **HiveMQ Cloud** as the MQTT broker.
* Secure MQTT communication using **TLS/SSL**.
* Publishes data every 3 seconds.
* Displays the detection status in the Raspberry Pi terminal.

---

## 🛠️ Hardware Components

* Raspberry Pi
* Line Sensor
* Jumper wires
* Breadboard
* Power supply

---

## 💻 Software & Technologies

* Python
* Raspberry Pi GPIO
* `gpiozero`
* `paho-mqtt`
* MQTT
* HiveMQ Cloud
* TLS/SSL

---

## 🔌 Hardware Connection

The Line Sensor is connected to **GPIO 17** of the Raspberry Pi.

| Component       | Raspberry Pi                                |
| --------------- | ------------------------------------------- |
| Line Sensor OUT | GPIO 17                                     |
| Line Sensor VCC | 5V / 3.3V according to sensor specification |
| Line Sensor GND | GND                                         |

> Make sure the sensor's output voltage is safe for the Raspberry Pi GPIO.

---

## 📡 MQTT Configuration

The project uses **HiveMQ Cloud** as the MQTT broker.

```python
MQTT_HOST = "f7559e3e38f94eb7bfc2906b6be26633.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
```

### MQTT Topic

The sensor data is published to:

```text
SIC/support
```

Another MQTT client can subscribe to this topic to receive the sensor readings.

---

## 🔐 Authentication

The MQTT connection uses a username and password:

```python
client.username_pw_set(USERNAME, PASSWORD)
```

TLS encryption is enabled using:

```python
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
```

### ⚠️ Security Note

Do **not** upload your real HiveMQ password to GitHub.

Instead of writing your password directly in the source code, use environment variables:

```python
import os

USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")
```

Then configure the variables on your Raspberry Pi.

---

## 📦 Installation

Install the required Python libraries:

```bash
pip install paho-mqtt gpiozero
```

If you're using a Raspberry Pi OS environment where GPIO dependencies are required, make sure the appropriate GPIO backend is installed and working.

---

## ▶️ Running the Project

Run the Python script:

```bash
python3 main.py
```

The system will continuously read the Line Sensor.

Example output:

```text
Person detected
No person detected
Person detected
Person detected
```

At the same time, the sensor value is published to the MQTT broker every **3 seconds**.

---

## 🔄 How It Works

The system follows this process:

```text
Line Sensor
     ↓
Raspberry Pi GPIO 17
     ↓
Python Program
     ↓
MQTT Client
     ↓
TLS/SSL Connection
     ↓
HiveMQ Cloud
     ↓
SIC/support Topic
     ↓
Subscriber / IoT Application
```

The Raspberry Pi reads the sensor value:

```python
payload = sensor.value
```

Then publishes it to HiveMQ:

```python
client.publish("SIC/support", payload)
```

If the sensor value is `1`, the program prints:

```text
Person detected
```

Otherwise:

```text
No person detected
```

---

## 📁 Project Structure

```text
Person-Detection-MQTT/
│
├── main.py
└── README.md
```

---

## 🌐 MQTT Communication

The project demonstrates how MQTT can be used for IoT communication.

### Publisher

The Raspberry Pi acts as the **MQTT Publisher**.

It publishes:

```text
Topic: SIC/support
Payload: 0 or 1
```

### Broker

**HiveMQ Cloud** acts as the MQTT Broker.

### Subscriber

Any MQTT client subscribed to:

```text
SIC/support
```

can receive the sensor data.

---

## 🎯 Project Goal

The goal of this project is to demonstrate a basic **IoT monitoring system** where sensor data is collected by a Raspberry Pi and transmitted remotely using **MQTT** and **HiveMQ Cloud**.

This architecture can be extended to support:

* Remote monitoring
* Smart security systems
* IoT dashboards
* Multiple sensors
* Automated alerts
* Smart home applications

---

## 👩‍💻 Technologies Used

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Raspberry Pi | Main controller         |
| Line Sensor  | Person/object detection |
| Python       | Programming language    |
| GPIO Zero    | GPIO control            |
| Paho MQTT    | MQTT communication      |
| HiveMQ Cloud | MQTT broker             |
| TLS/SSL      | Secure communication    |

---

## 📜 License

This project was created for educational and IoT development purposes.
