# Lab 1 – Requirements Engineering & UML Use-Case Modelling

## Problem Statement #23: Hyperlocal Courier Dispatch & Tracking Engine

### System Overview

An on-demand courier platform that assigns local parcel pickups to nearby delivery riders, optimizes multi-stop routes, and uses OTP verification at the destination. The system enables senders to create requests, track deliveries in real time, and ensures secure and efficient delivery completion.

### Functional Requirements

| **Req ID** | **Description** | **Priority** | **Acceptance Criteria** | **Rationale** |
|:---:|---|:---:|---|---|
| **FR-001** | The system shall match an outgoing courier request with the nearest active delivery rider within a **3 km radius**. | **High** | **Pass:** An active rider within 3 km receives the dispatch notification.<br><br>**Fail:** An offline or out-of-range rider is assigned. | Ensures efficient rider assignment. |
| **FR-002** | The system shall allow the sender client to create an on-demand courier request by providing pickup and destination details. | **High** | **Pass:** A request is created when both locations are valid.<br><br>**Fail:** The request is rejected if either location is missing. | Enables the sender to initiate a delivery. |
| **FR-003** | The system shall provide the sender client with the current delivery status and live GPS location of the assigned delivery rider. | **High** | **Pass:** The sender can view the current status and latest rider location.<br><br>**Fail:** The updated status or location is unavailable. | Enables real-time delivery tracking. |
| **FR-004** | The system shall generate an optimized route for a delivery rider when multiple delivery stops are assigned. | **Medium** | **Pass:** The generated route includes all assigned stops in an ordered route.<br><br>**Fail:** One or more assigned stops are missing. | Improves efficiency for multiple deliveries. |
| **FR-005** | The system shall verify the delivery using a destination OTP before marking the courier request as completed. | **High** | **Pass:** Delivery is completed only after a valid OTP is entered.<br><br>**Fail:** An invalid OTP does not complete the delivery. | Confirms successful delivery at the destination. |

### Non-Functional Requirements

| **Req ID** | **Type** | **Description** | **Priority** | **Acceptance Criteria** | **Rationale** |
|:---:|:---:|---|:---:|---|---|
| **NFR-001** | Performance | The system shall transmit delivery status and live GPS telemetry updates from riders to the sender client with **under 2-second latency**. | **High** | **Pass:** At least 95% of updates are delivered within 2 seconds during simulated peak load.<br><br>**Fail:** More than 5% of updates exceed 2 seconds. | Ensures responsive real-time tracking for the sender. |
| **NFR-002** | Security | The system shall restrict delivery information and OTP verification data to authorized sender clients and delivery riders. | **High** | **Pass:** Unauthorized access is denied in all tested cases.<br><br>**Fail:** Any unauthorized access is permitted. | Protects delivery and verification information. |

### Actors Identified

| **Actor** | **Role in the System** |
|---|---|
| **Sender Client** | Creates courier requests and tracks delivery status and rider location. |
| **Delivery Rider** | Receives delivery assignments, follows routes, updates delivery progress, and completes deliveries using OTP verification. |
| **Location/GPS Service** | Provides location information used for rider tracking and route optimization. |