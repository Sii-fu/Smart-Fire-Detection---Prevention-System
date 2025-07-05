# 🔥 Smart Fire Detection & Prevention System

A simulated IoT-based fire safety system built with **Cisco Packet Tracer** and **Python**, designed to detect fire hazards in real time, send emergency alerts, and automate fire suppression – all before disaster strikes.

## 🚀 Overview

Fire hazards in residential and commercial areas often escalate due to **late detection** and **slow emergency response**. This project demonstrates a **network-integrated smart fire safety system** that:

- Detects fire and smoke instantly using sensors
- Sends **real-time alerts** to residents and fire stations
- Activates sprinklers and opens emergency exits automatically
- Notifies emergency responders via a **switch-based alert system**

> Simulated entirely in **Cisco Packet Tracer** with backend logic scripted in **Python** + **Firebase**.

---

## 🧠 Key Features

### 🔎 Fire Detection
- Flame sensors monitor for fire continuously
- Realtime logging and alert generation

### 📡 Emergency Alerts
- Automated **email notifications** to users and firefighters
- **Siren activation** for instant in-house alerts
- **Switch-based emergency alert** to fire station network

### 💧 Automated Fire Response
- Smart **water sprinkler** system triggers automatically
- **Emergency exit system** unlocks doors/windows for evacuation

### 🌐 Network Integration
- DHCP & RIP for dynamic IP assignment and quick routing
- IoT devices integrated through smart controllers
- Firebase used for storing fire incident data in real time

---

## 🏗️ System Architecture

```txt
+------------------------+
|   Fire Monitoring IoT  |
|  (Flame Sensor, SBC)   |
+----------+-------------+
           |
           v
+------------------------+
|      IoT Server        |
| + Email Server         |
| + Firebase DB          |
+----------+-------------+
           |
           v
+------------------------+
|   Home Network Router  |
|  ↔ DHCP + RIP Enabled  |
+----------+-------------+
           |
           v
+------------------------+
| Fire Station Network   |
| (Notification System)  |
+------------------------+
