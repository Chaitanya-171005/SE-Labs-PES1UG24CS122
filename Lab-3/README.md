# Lab 3 – Component Modelling & Architectural Pattern Selection

**Course:** Software Engineering (SE) Lab  
**SRN:** PES1UG24CS122  
**System:** Hyperlocal Courier Dispatch & Tracking Engine  
**Chosen Architecture:** Microservices

---

## Objective

Model the internal structure of the **Hyperlocal Courier Dispatch & Tracking Engine** (from Lab 1) as a **UML Component Diagram**, select a suitable software architecture pattern, and justify the choice.

## Architecture Decision

We chose the **Microservices Architecture** for this system. Each capability (request intake, dispatch/assignment, tracking, routing, OTP verification, notifications) is built as an independently deployable service, communicating through well-defined provided/required interfaces via an API Gateway.

See `Lab_3_Justification.pdf` for the full 1-page justification (scaling, fault isolation, security, and performance reasoning tied to the Lab 1 requirements).

## Files in this folder

| File | Description |
|------|-------------|
| `Component_Diagram.pdf` | UML Component Diagram (draw.io style) |
| `Lab_3_Justification.pdf` | 1-page architecture justification |
| `README.md` | This file |

## Components (11)

| Component | Stereotype | Responsibility |
|-----------|-----------|----------------|
| Sender Client App | «client» | External actor – creates/tracks courier requests |
| Delivery Rider App | «client» | External actor – receives assignments, shares location |
| API Gateway | «component» | Single entry point; authN/authZ, TLS, routing |
| Courier Request Service | «component» | Creates and manages delivery requests |
| Dispatch & Assignment Service | «component» | Matches nearest rider (≤3 km), assigns jobs |
| Tracking Service | «component» | Real-time GPS status feed (<2s latency) |
| Route Optimization Service | «component» | Multi-stop route planning |
| OTP Verification Service | «component» | Secure delivery-confirmation OTP handling |
| Notification Service | «component» | Push/SMS status notifications |
| Data Store | «database» | Shared persistence for delivery/OTP data |
| Location / GPS Service | «external» | External positioning provider |

## Interfaces (9)

`IClientPortal`, `IRiderPortal`, `ICourierRequest`, `ITrackingFeed`, `IDispatch`, `IRoutePlan`, `INotify`, `IOtpVerify`, `ILocation` — plus `IPersistence` shown as «use» dependencies to the Data Store.

Interfaces use standard UML **ball (provided)** and **socket (required)** notation. Services depend on the Data Store through «use» dependencies.

## Requirements Traceability

- **NFR-001 (<2s telemetry latency):** met by independently scaling the Tracking Service.
- **NFR-002 (restricted delivery/OTP data access):** enforced via the API Gateway + dedicated OTP Verification Service and least-privilege access.

## How to view / edit

The diagram is provided as a PDF. To edit, recreate or import it in [draw.io](https://app.diagrams.net) using the same components, interfaces, and «use» dependencies shown in the diagram.