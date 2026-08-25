<div align="center">

# Lab 1 – Requirements Engineering & UML Use-Case Modelling

### Problem Statement #23: Hyperlocal Courier Dispatch & Tracking Engine

**Smart Cities, Transport & Logistics**

</div>

## Overview

This repository contains the requirements engineering and UML use-case modelling work for **Problem Statement #23 – Hyperlocal Courier Dispatch & Tracking Engine**.

The system is an on-demand package delivery platform that assigns local parcel pickups to nearby delivery riders, supports multi-stop route optimization, provides real-time delivery tracking, and uses OTP verification at the destination.

The primary stakeholders identified for the system are the **Sender Client**, **Delivery Rider**, and **Location/GPS Service**.

## Problem Statement

The **Hyperlocal Courier Dispatch & Tracking Engine** is designed to support local parcel delivery through an automated dispatch and tracking process.

The system allows the **Sender Client** to create an on-demand courier request by providing pickup and destination details. Once a request is created, the system identifies the nearest active delivery rider within a **3 km radius** and assigns the request to that rider.

The platform also supports:

- Real-time delivery status and rider location tracking
- Multi-stop route optimization for delivery riders
- Destination-based OTP verification
- Secure access to delivery and verification information

The problem statement specifically defines rider assignment within a **3 km radius** and requires delivery status and live GPS telemetry updates to reach the Sender Client with **under 2-second latency**.

## System Objectives

The main objectives of the system are to:

1. Enable the Sender Client to create courier requests efficiently.
2. Automatically assign requests to nearby active delivery riders.
3. Allow the Sender Client to track delivery progress and rider location.
4. Optimize routes when riders have multiple delivery stops.
5. Verify successful delivery using a destination OTP.
6. Provide responsive and secure delivery tracking.

## Actors

| Actor | Description |
| :--- | :--- |
| **Sender Client** | Creates courier requests and tracks delivery status and rider location. |
| **Delivery Rider** | Receives delivery assignments, follows routes, updates delivery progress, and completes deliveries using OTP verification. |
| **Location/GPS Service** | Provides location information used for rider tracking and route optimization. |

## Requirements Engineering

The system requirements were identified from the assigned problem scenario and documented using a structured requirements table.

### Functional Requirements

The project contains exactly **five functional requirements**:

| ID | Function |
| :---: | :--- |
| **FR-001** | Assign the nearest active delivery rider within a 3 km radius. |
| **FR-002** | Create an on-demand courier request using pickup and destination details. |
| **FR-003** | Provide delivery status and live GPS tracking to the Sender Client. |
| **FR-004** | Generate an optimized route for multiple delivery stops. |
| **FR-005** | Verify delivery using a destination OTP before completion. |

### Non-Functional Requirements

The project contains exactly **two non-functional requirements**:

| ID | Type | Requirement |
| :---: | :---: | :--- |
| **NFR-001** | Performance | Delivery status and live GPS telemetry updates shall reach the Sender Client with under 2-second latency. |
| **NFR-002** | Security | Delivery information and OTP verification data shall be restricted to authorized users. |

Each requirement includes a priority, measurable acceptance criteria, and rationale.

The complete requirements table is available in:

[**Requirements.md**](Requirements.md)

## UML Use-Case Model

The UML model represents the main interactions between the identified actors and the courier dispatch system.

### Use Cases

| ID | Use Case |
| :---: | :--- |
| **UC-01** | Create Courier Request |
| **UC-02** | Assign Delivery Rider |
| **UC-03** | Track Delivery |
| **UC-04** | View Live Rider Location |
| **UC-05** | Optimize Delivery Route |
| **UC-06** | Complete Delivery |
| **UC-07** | Verify Delivery OTP |

### UML Relationships

The diagram contains both required relationship types:

- **UC-01 `«include»` UC-02**  
  Creating a courier request includes assigning a delivery rider.

- **UC-06 `«include»` UC-07**  
  Completing a delivery includes verifying the destination OTP.

- **UC-04 `«extend»` UC-03**  
  Viewing the live rider location extends the delivery tracking functionality.

The UML diagram also contains the required system boundary and all identified actors.

The completed diagram is available in:

[**Use_Case_Diagram.pdf**](Use_Case_Diagram.pdf)

## Use-Case Flow Specification

The selected core use case for the detailed flow specification is:

**UC-01 – Create Courier Request**

### Primary Actor

**Sender Client**

### Preconditions

- The Sender Client is registered and has access to the courier service.
- The Sender Client has valid pickup and destination details.
- The courier service is available to process new requests.

### Postconditions

- A courier request is successfully created.
- The request is assigned to an active delivery rider within the specified 3 km radius.
- The Sender Client receives confirmation of the courier request.

### Main Success Scenario

1. The Sender Client selects the option to create a new courier request.
2. The system displays the courier request form.
3. The Sender Client enters the pickup location and destination details.
4. The system validates the entered pickup and destination information.
5. The system creates the courier request.
6. The system identifies the nearest active delivery rider within a 3 km radius.
7. The system assigns the courier request to the selected rider.
8. The system sends a dispatch notification to the Delivery Rider.
9. The system displays a confirmation of the assigned courier request to the Sender Client.
10. The use case ends successfully.

### Alternate Flow – No Eligible Rider Available

1. **At Step 6 of the Main Success Scenario, the system cannot find an active delivery rider within the 3 km radius.**
2. The system informs the Sender Client that no eligible rider is currently available.
3. The courier request is placed in a pending state.
4. The Sender Client may retry the request or cancel it.
5. The use case ends when the request is retried successfully or cancelled.

The complete use-case flow specification is available in:

[**Use_Case_Flow.pdf**](Use_Case_Flow.pdf)

## Folder Structure

```text
Lab-1/
│
├── README.md
├── Requirements.md
├── Use_Case_Diagram.pdf
└── Use_Case_Flow.pdf