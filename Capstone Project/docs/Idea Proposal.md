# Capstone Project: 1-Page Idea Proposal

## 1. Project Idea

- **Problem Statement:** In Syria and remote wild forests, environmental monitoring is severely hindered by unreliable government network infrastructure, frequent power outages, and the high cost of commercial IoT solutions. This lack of connectivity leaves farmers and forest rangers blind to imminent threats—such as sudden weather shifts, wildfires, and livestock loss—and unable to gather real-time, hyper-local climate data.
- **Specific Goal:** To design and build **SentinelMesh**, a cost-effective, solar-powered, independent IoT mesh network MVP using ESP32 microcontrollers (an edge node with a camera + sensors, and a backbone node). The system will bypass government networks by creating a self-sustaining local mesh. It will utilize Edge AI (specifically **YOLO**) and sensor data to provide four core functions:
  1. Real-time weather and soil moisture monitoring for agricultural optimization.
  2. Wildfire early warning via smoke/flame detection.
  3. Automated wildlife tracking and logging.
  4. Automated livestock/herd counting using YOLO object detection to help farmers monitor their animals remotely.

## 2. Relevance to Sustainable Development Goals (SDGs)

- **SDG 2 (Zero Hunger):** By providing farmers with real-time, hyper-local data on soil moisture and weather, the system enables data-driven agricultural decisions, directly improving crop yields. Furthermore, the **YOLO-based herd counting** assists farmers in protecting and managing their livestock, a critical source of food and income.
- **SDG 13 (Climate Action):** The wildfire detection capability allows for immediate alerts, preventing large-scale environmental destruction. Additionally, the independent solar power system promotes the use of renewable energy.
- **SDG 9 (Industry, Innovation, and Infrastructure):** The project builds a resilient, decentralized technological infrastructure (mesh networking) where traditional infrastructure (cellular/government networks) is absent or failing.
- **SDG 15 (Life on Land):** Automated wildlife tracking and logging help researchers and rangers monitor biodiversity and protect forest ecosystems.

## 3. Literature Examples

1. **"Wildfire Detection Using YOLO and IoT-based Edge Computing" (General Research):** Many recent studies focus on deploying lightweight object detection models (like YOLOv5 or YOLOv8) directly on edge devices (like ESP32-CAM or Raspberry Pi). This literature proves that running AI locally to detect smoke or fire is highly effective, reduces bandwidth needs, and provides faster alerts compared to cloud-only processing. This supports our edge-camera MVP design for fire alerts and validates our approach to deploying YOLO for multiple object detection tasks on the same hardware.
2. **"Smart Agriculture using Solar-Powered Wireless Sensor Networks" (e.g., *IEEE Sensors Journal*):** Research into agricultural IoT often highlights the limitations of relying on traditional power grids and Wi-Fi in rural areas. Studies demonstrate that combining solar energy harvesting with low-power wide-area networks (LPWAN) or mesh topologies creates highly reliable, long-term monitoring systems for soil, weather, and livestock. This validates our approach to powering the nodes with solar energy to create a self-sustaining network capable of handling continuous YOLO inference for herd monitoring.