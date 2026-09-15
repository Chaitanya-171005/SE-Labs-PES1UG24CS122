# Lab 2 — Agile Backlog Creation & Sprint Simulation in Jira

**Course:** Software Engineering (SE) — Lab 2  
**Name:** Chaitanya Krishna M  
**SRN:** PES1UG24CS122  
**Section:** 5th Semester, Section B  
**Problem Statement #23:** Hyperlocal Courier Dispatch & Tracking Engine  
**Date of Completion:** 26 August 2026

---

## 1. Objective

Use Jira to convert the functional requirements identified in Lab 1 into Agile backlog items (Epics and User Stories), prioritize and estimate them with Fibonacci-based Story Points, run and simulate sprints on a Scrum board, and analyse progress using Burndown Charts.

## 2. Project Overview

The **Hyperlocal Courier Dispatch & Tracking Engine** is an on-demand courier platform that manages local parcel delivery from request creation through final delivery verification. It lets sender clients create courier requests, assigns nearby delivery riders, supports live tracking and rider location monitoring, optimizes multi-stop delivery routes, and verifies successful delivery using destination-based OTP verification.

| Field | Value |
| --- | --- |
| Project | Hyperlocal Courier Dispatch |
| Project Key | HCD |
| Board | HCD board |
| Method | Scrum |
| Epics | 3 |
| User Stories | 8 |
| Total Story Points | 31 |
| Sprints Completed | 2 |
| Workflow | To Do → In Progress → Done |

**Jira Workspace:** https://pes1ug24cs122.atlassian.net/jira/software/c/projects/HCD/summary

> **Note:** Both sprints were planned and executed as a simulation within a single on-campus lab session (one day), not over calendar weeks. The sprint time-boxes shown below are simulated.

## 3. Epics and User Stories

### Epics

| Epic ID | Epic |
| --- | --- |
| HCD-1 | Courier Request & Dispatch |
| HCD-2 | Delivery Tracking & Routing |
| HCD-3 | Delivery Completion & Verification |

### User Stories

| ID | User Story | Epic | Priority | Story Points |
| --- | --- | --- | --- | --- |
| HCD-4 | Create Courier Request | HCD-1 | High | 3 |
| HCD-5 | Validate Courier Request | HCD-1 | High | 2 |
| HCD-6 | Assign Nearby Delivery Rider | HCD-1 | High | 5 |
| HCD-7 | Track Delivery Status | HCD-2 | High | 3 |
| HCD-8 | View Live Rider Location | HCD-2 | High | 5 |
| HCD-9 | Optimize Delivery Route | HCD-2 | Medium | 8 |
| HCD-10 | Complete Delivery | HCD-3 | High | 3 |
| HCD-11 | Verify Delivery with OTP | HCD-3 | High | 2 |
| | **Total** | | | **31** |

Story Points were assigned using the Fibonacci scale (2, 3, 5, 8) based on the relative effort, complexity, uncertainty and risk of each story. Higher values were given to more complex work such as route optimization (8).

## 4. Sprint Simulation

### Sprint 1 — HCD Sprint 1 (simulated, 1 lab session)
**Goal:** Complete the core courier request, validation, rider assignment, and delivery tracking flow.

| ID | User Story | Points |
| --- | --- | --- |
| HCD-4 | Create Courier Request | 3 |
| HCD-5 | Validate Courier Request | 2 |
| HCD-6 | Assign Nearby Delivery Rider | 5 |
| HCD-7 | Track Delivery Status | 3 |
| | **Sprint Total** | **13** |

All four stories moved through To Do → In Progress → Done. Committed 13 pts, completed 13 pts, remaining 0 pts.

### Sprint 2 — HCD Sprint 2 (simulated, 1 lab session)
**Goal:** Complete delivery tracking, route optimization, and secure delivery verification.

| ID | User Story | Points |
| --- | --- | --- |
| HCD-8 | View Live Rider Location | 5 |
| HCD-9 | Optimize Delivery Route | 8 |
| HCD-10 | Complete Delivery | 3 |
| HCD-11 | Verify Delivery with OTP | 2 |
| | **Sprint Total** | **18** |

All four stories moved through To Do → In Progress → Done. Committed 18 pts, completed 18 pts, remaining 0 pts.

## 5. Burndown Analysis

| Sprint | Committed | Completed | Remaining |
| --- | --- | --- | --- |
| HCD Sprint 1 | 13 pts | 13 pts | 0 pts |
| HCD Sprint 2 | 18 pts | 18 pts | 0 pts |

Both sprints reached 0 remaining Story Points. Because the sprints were simulated in a compressed session rather than over a full one-week period, both charts show a sharp reduction in remaining work rather than a gradual daily burndown, so they should not be read as a realistic measure of daily velocity.

## 6. Reflection (Summary)

1. **Did estimations reflect actual effort?** Estimates gave a reasonable relative representation of effort (smaller stories like OTP verification got fewer points; complex route optimization got 8). As a simulation, they can't be compared to real dev hours but were useful for planning.
2. **Was the backlog well-prioritized?** Yes. Core courier workflow (create/validate requests, assign riders, tracking) was High priority; route optimization was Medium, so essential functionality was completed first in Sprint 1.
3. **How did the simulated sprint align with the plan?** Both sprints aligned fully — all 8 stories completed across the two sprints following the To Do → In Progress → Done workflow.
4. **What did the burndown chart show about capacity?** The full scope was completed within planned work, but the compressed simulation makes the burndown sharper than a real sprint would be.

## 7. Folder Contents

```
Lab2/
├── README.md                   
└── Lab2_Deliverable_PES1UG24CS122.pdf   
```

## 8. Deliverables Checklist

- Jira backlog with Epics and User Stories
- Story point assignments
- Sprint board (Active Sprint view) — both sprints
- Burndown charts (Sprint 1 and Sprint 2)
- Reflection questions answered (see deliverable PDF, Section 08)
- Live Jira workspace available for instructor demonstration