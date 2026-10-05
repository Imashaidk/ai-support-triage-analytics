# Project Charter: AI-Powered Customer Support Triage & SLA Breach Prevention Engine

| Document Version | Status | Project Sponsor | Project Manager / Lead | Last Updated |
| :--- | :--- | :--- | :--- | :--- |
| **v1.0.0** | Approved | VP of Customer Experience (CX) | PM / Lead Business Analyst | October 2026 |

---

## 1. Executive Summary & Business Case

### 1.1 Business Context
Global Enterprise organizations handle tens of thousands of customer support tickets every month across technical, billing, account security, and feature inquiries. Currently, ticket categorization, priority assessment, and routing are performed manually by Tier-1 support representatives. 

This manual triage process introduces:
- **Triage Delay:** Average 2.8 hours elapsed before a ticket is routed to the appropriate subject-matter queue.
- **Misrouting Rates:** 18.4% of tickets are routed to incorrect departments, requiring secondary reassignment.
- **SLA Breaches:** 14.2% of high-severity enterprise tickets breach their contractual Service Level Agreements (SLAs), triggering contractual financial penalties and degrading customer retention.
- **Elevated Operational Overhead:** Over $312,000 annually in support agent labor dedicated purely to manual reading and tagging tickets.

### 1.2 Proposed Solution
The **AI-Powered Customer Support Triage & SLA Breach Prevention Engine** is an intelligent operational decision-support system. It automatically ingests tickets, applies Natural Language Processing (NLP) to classify department categories and sentiment, predicts SLA breach risk within 2 seconds of arrival, and suggests templated response resolutions for human verification.

---

## 2. Project Objectives & Success Metrics (OKRs)

### Strategic Objectives
1. **Accelerate Triage & First Response Time (FRT):** Reduce median initial routing time from 168 minutes to under 2 minutes.
2. **Minimize Contractual SLA Breaches:** Reduce enterprise SLA breach rates from 14.2% to under 3.5%.
3. **Optimize Operational Capacity:** Automate zero-touch routing for at least 75% of incoming tickets with high model confidence ($>85\%$).
4. **Boost Agent Productivity:** Equip support engineers with auto-drafted response recommendations, trimming average handle time (AHT) by 25%.

### Target KPI Scorecard
| Metric | Baseline (Current State) | Target (Post-Launch) | Measurement Cadence |
| :--- | :--- | :--- | :--- |
| **Manual Triage Time** | 2.8 hours (168 mins) | $< 2$ minutes (automated) | Real-time / Daily |
| **Routing Accuracy** | 81.6% (Manual) | $\ge 92.0\%$ (AI Model) | Weekly audit |
| **Enterprise SLA Breach Rate** | 14.2% | $< 3.5\%$ | Monthly |
| **Average Handle Time (AHT)** | 32.5 minutes | $< 24.0$ minutes | Bi-weekly |
| **Customer CSAT Score** | 3.7 / 5.0 | $\ge 4.4 / 5.0$ | Quarterly Survey |
| **Annualized Net Savings** | $0 (Baseline) | $\ge \$280,000$ | Annual Review |

---

## 3. Project Scope & Boundaries

### 3.1 In-Scope
- **Automated Multi-Class Classification:** Ingestion and classification of tickets into 4 core functional streams: *Technical Issues, Billing & Invoicing, Account & Security, and General Inquiries*.
- **Urgency & SLA Breach Scoring:** Machine learning model predicting breach likelihood (High, Medium, Low) based on historical resolution complexity and enterprise tier.
- **Sentiment & Churn Risk Detection:** Lexical and semantic scoring flagging escalating customer frustration.
- **Human-in-the-Loop (HITL) Fallback:** Confidence-based thresholding (scores $<0.75$ flag tickets for manual supervisor review).
- **Interactive Operational Dashboards:**
  - *Agent View:* Real-time ticket triage, confidence scores, and auto-generated reply templates.
  - *Executive View:* SLA countdown monitor, department queue health, and financial savings counter.
- **Privacy & Compliance Redaction:** Regex and NLP token masking for customer PII (credit cards, passwords, phone numbers, emails).

### 3.2 Out-of-Scope (Phase 1)
- Direct autonomous auto-reply to customers without human agent review (preventing hallucination risk).
- Voice/telephony audio transcription (restricted to written text: web portal, email, and live chat transcripts).
- Autonomous database modifications (e.g., automated refunds or password resets directly executed by AI).

---

## 4. Stakeholder Analysis & RACI Matrix

* **R** - Responsible (Executes the work)
* **A** - Accountable (Approves and owns final outcome)
* **C** - Consulted (Provides two-way input and feedback)
* **I** - Informed (Kept updated on progress)

| Project Milestone / Deliverable | Project Manager | Lead BA | Data Scientist | Support Leads | VP of CX | Security / Legal |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Project Charter & Scope** | **A / R** | C | C | C | I | I |
| **BRD & User Stories** | A | **R** | C | C | I | I |
| **PII & Data Compliance Approval** | A | C | C | I | I | **R** |
| **Data Pipeline & Model Development**| A | C | **R** | I | I | I |
| **UI Dashboard & Prototype** | A | **R** | **R** | C | I | I |
| **User Acceptance Testing (UAT)** | A | **R** | C | **R** | I | I |
| **Change Management & Pilot Rollout**| **R** | C | I | **R** | **A** | I |

---

## 5. Milestone Schedule & Timeline Overview

| Phase | Duration | Core Deliverables | Exit Criteria |
| :--- | :--- | :--- | :--- |
| **Sprint 1: Discovery & Foundations** | Weeks 1–2 | Project Charter, BRD, Data Ingestion, EDA | Approved BRD, Data Governance sign-off |
| **Sprint 2: ML Pipeline & Modeling** | Weeks 3–4 | Multi-task Classifier, SLA Model, SHAP Explainability | Classification Macro-F1 $\ge 0.88$ |
| **Sprint 3: App Dev & HITL Integration** | Weeks 5–6 | Streamlit Dashboard (Agent & Manager Views), Fallback Engine | End-to-end inference latency $< 1.5$s |
| **Sprint 4: Validation & Rollout** | Weeks 7–8 | UAT with 10 Support Agents, ROI Audit, Documentation | 90% agent task approval, zero critical bugs |

---

## 6. Budget & Resource Estimates

| Resource Category | Details | Est. Cost / Commitment |
| :--- | :--- | :--- |
| **Personnel Allocation** | 1 PM (50%), 1 BA (100%), 1 Data Scientist (100%), 2 Support Champions (20%) | Internal reallocation |
| **Cloud & Compute Infrastructure**| AWS / GCP Model Hosting, Feature Store, Vector/Inference cache | $650 / month |
| **Data Pipeline & Tooling** | Open-source ecosystem (Scikit-Learn, LightGBM, Streamlit, Pandas) | $0 (Open-Source) |
| **Contingency Reserve** | 15% allocation for schedule buffer & cloud overflow | $2,000 one-off |

---

## 7. Approval & Governance Sign-Off

* **Project Sponsor:** VP of Customer Experience — *Approved*
* **Lead Business Analyst / Project Manager:** Project Lead — *Approved*
* **Lead Data Scientist:** ML Engineer — *Approved*
