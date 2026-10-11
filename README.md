# I. Information Routing System
Rule-based system for classifying information and routing it to relevant stakeholders

# II. Classification

## Information Type Classification (V1)

This classification defines the business meaning of information submitted to the Information Routing System.

Information must be classified based on **what it represents in the business**, not how it is communicated or which department submits it.

### 1. Information Type Matrix

| Information Type | Business Definition | Key Question | Example |
|---|---|---|---|
| **Incident** | An unexpected, undesirable event or condition that deviates from accepted operating conditions. | What went wrong? | A production machine unexpectedly stops due to a motor failure. |
| **Change** | An actual or planned modification to an existing process, schedule, system, condition, or operating arrangement that may affect relevant stakeholders. | What is changing or has changed? | Production reschedules harvesting, requiring QC to adjust its sampling schedule. |
| **Request** | A communication asking another person or team to perform an action, provide information, or deliver a specific output. | What action or deliverable is needed? | Production requests IT to restore access to a reporting system. |
| **Proposal** | A suggested action, solution, or modification submitted for evaluation before a decision is made. | What should we consider doing? | Engineering proposes installing an additional sensor to improve process monitoring. |
| **Decision** | A choice or conclusion confirmed by an authorized person or body, establishing what has been approved, rejected, or selected. | What has been decided? | Management approves a new monthly financial closing schedule. |
| **Announcement** | Information communicated primarily to create awareness, without primarily representing an incident, change, request, proposal, or decision. | What do stakeholders need to know? | HR shares a general reminder about an existing company policy. |

## 2. Severity Classification Matrix (V1)

| Impact Dimension | Low | Medium | High | Critical |
|---|---|---|---|---|
| **Production** — Affect Production | Less than 15 minutes | 15 to less than 60 minutes | 60 to less than 240 minutes | 240 minutes or more |
| **Financial** — Estimated financial loss | Less than VND 5 million | VND 5M to less than 20M | VND 20M to less than 100M | VND 100M or more |
| **Quality** — Product quality impact | Minor deviation, resolved on-site | Rework required, no delivery impact | Batch hold affecting delivery schedule | Unsafe product already released to market |
| **Safety** — Occupational safety | No injury or significant hazard | Incident requiring first aid | Serious injury | Fatality or immediate risk of fatality |
| **Delivery** — Delivery delay | No delay against commitment | Less than 1 day late | 1 to less than 3 days late | 3 days late or more |

### Severity Assessment Rules

- **Highest severity applies:** If an event meets multiple criteria, the highest applicable severity determines the overall classification
- **Safety escalation:** Severe safety-related incidents require immediate escalation without waiting for complete financial or operational impact assessment