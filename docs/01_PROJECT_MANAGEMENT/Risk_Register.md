# Enterprise Project Risk Register & Mitigation Strategy

| Project | Current Risk Status | Last Reviewed | Review Cadence |
| :--- | :--- | :--- | :--- |
| **AI Support Triage Engine** | 🟢 Controlled (No Critical Blockers) | October 2026 | Weekly Sprint Review |

---

## 1. Risk Scoring Methodology

Risk Severity is determined using a $5 \times 5$ Risk Matrix:
$$\text{Risk Score} = \text{Probability (1–5)} \times \text{Impact (1–5)}$$

* **Low (1–6):** Managed via standard team operating procedures.
* **Medium (8–12):** Active mitigation required; reviewed bi-weekly.
* **High (15–20):** Escalated to PM and Tech Leads; immediate mitigation controls.
* **Critical (25):** Project blocker; triggers immediate steering committee review.

---

## 2. Risk Matrix Heatmap

| Impact $\rightarrow$ <br> Probability $\downarrow$ | 1 (Negligible) | 2 (Minor) | 3 (Moderate) | 4 (Major) | 5 (Catastrophic) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **5 (Almost Certain)** | 5 | 10 | 15 | 20 | 25 |
| **4 (Likely)** | 4 | 8 | 12 | **R-03 (16)** | 20 |
| **3 (Possible)** | 3 | 6 | **R-02 (9)** | **R-01 (12)** | **R-04 (15)** |
| **2 (Unlikely)** | 2 | 4 | 6 | **R-05 (8)** | 10 |
| **1 (Rare)** | 1 | 2 | 3 | 4 | 5 |

---

## 3. Comprehensive Risk Log

| Risk ID | Category | Risk Description | Prob (1-5) | Imp (1-5) | Score | Mitigation Strategy (Preventive) | Contingency Plan (Corrective) | Risk Owner | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **R-01** | **Compliance / Legal** | Customer tickets contain unredacted PII (credit cards, passwords, SSNs) violating GDPR / CCPA. | 3 | 4 | **12** | Implement automated regex and Spacy NER token anonymization pre-processing layer prior to any model ingestion. | Isolate offending records immediately; re-run sanitized pipeline; notify data protection officer. | Compliance Lead / ML Eng | 🟡 Active |
| **R-02** | **Technical / ML** | Class imbalance in training data causes poor recall on rare but critical "Security Breach" tickets. | 3 | 3 | **9** | Apply SMOTE, class-weight rebalancing (`scale_pos_weight`), and focal loss tuning. | Route any ticket with specific high-risk keywords ("breach", "compromise", "hacked") directly via rule-based override. | Data Scientist | 🟢 Mitigated |
| **R-03** | **Operational / Adoption** | Support agents distrust automated AI classifications and continue manually re-reading all tickets. | 4 | 4 | **16** | Introduce SHAP explainability tags showing rationale; involve 10 senior agents in co-designing the UI. | Run weekly 30-min office hours; highlight time saved and recognize top AI-collaborative agents. | Change Mgmt Lead / PM | 🟡 In Progress |
| **R-04** | **Technical / Quality** | Model hallucination or misclassification causes a critical P1 outage ticket to be misrouted. | 3 | 5 | **15** | Implement confidence thresholding: any prediction with confidence $< 75\%$ is routed to a human supervisor triage queue. | Maintain a 15-minute SLA watchdog monitoring unassigned P1 tickets to trigger SMS alerts to the on-call lead. | Lead Architect | 🟢 Mitigated |
| **R-05** | **Architecture / Infra** | Spikes in incoming ticket volume cause API latency $> 5$ seconds during enterprise incident surges. | 2 | 4 | **8** | Implement asynchronous message queue (e.g., Redis/Celery architecture) and model quantization/caching. | Auto-scale cloud containers; fallback to lightweight TF-IDF model if latency exceeds 2.5s. | DevOps / Data Eng | 🟢 Mitigated |

---

## 4. Governance & Monitoring Protocol
1. **Weekly PM Standup:** Review newly identified risks and re-score active ones.
2. **Post-Sprint Audit:** Validate that preventive controls for R-01 and R-04 have zero regressions.
3. **Trigger Thresholds:** Any score crossing 15 requires an emergency architecture review within 24 hours.
