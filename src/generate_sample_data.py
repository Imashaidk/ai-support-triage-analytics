"""
Data Generation Script for AI Support Triage & SLA Breach Prevention Engine
Generates realistic multi-tier enterprise support tickets with SLA metrics and text bodies.
"""

import os
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_support_data(n_samples: int = 3500, random_state: int = 42) -> pd.DataFrame:
    random.seed(random_state)
    np.random.seed(random_state)

    categories = {
        "Technical Support": [
            ("Production API returning 500 error on checkout endpoint", "Our payment processing service has been dropping 45% of customer transactions since 10:00 AM UTC. We need immediate engineering escalation."),
            ("Kubernetes cluster node failure after v2.4 upgrade", "Three worker nodes entered NotReady state immediately following our maintenance window upgrade. Pods are in CrashLoopBackOff."),
            ("Database connection timeout during peak load", "PostgreSQL connection pool exhausted. Response latency spiked to 8500ms. Clients are receiving Gateway Timeout errors."),
            ("Webhook deliveries failing with SSL handshake error", "All inbound webhook events from our CRM are being rejected with SSL cert verification failure. Please assist."),
            ("SSO SAML authentication loop with Okta identity provider", "Employees cannot access the main dashboard. The login page redirects continuously after successful IdP authentication."),
            ("Memory leak observed on background worker service", "RAM utilization spikes to 99% within 4 hours of deployment. System OOM killer terminates core ingestion workers."),
            ("Data synchronization lag between primary and replica nodes", "Read replicas are 45 minutes behind master node. Real-time reporting dashboard shows stale metrics."),
            ("GraphQL query complexity limit exceeded on reporting queries", "Our automated ETL pipeline is failing with QueryComplexityError. We need query depth quota increased."),
            ("File export to AWS S3 bucket failing with AccessDenied", "Automated daily CSV exports are failing with permission errors even though IAM policy has PutObject granted."),
            ("Mobile SDK crash on Android 14 launch", "The latest mobile SDK release (v4.2.1) causes a fatal SIGSEGV exception on Android 14 devices.")
        ],
        "Billing & Invoicing": [
            ("Disputed charge on invoice INV-2026-8891", "We were billed for 50 additional seat licenses that were deactivated last month. Please issue a corrected invoice and credit memo."),
            ("Unable to update corporate credit card details in billing portal", "When attempting to save the new corporate Mastercard, the billing UI throws 'Transaction declined by issuer'. Please verify."),
            ("Request for annual upfront contract discount & wire transfer details", "Our procurement department requires official bank wire transfer instructions and a formal quote for our 2027 enterprise renewal."),
            ("Duplicate invoice issued for September subscription cycle", "We received two separate invoices for the same billing period (INV-9021 and INV-9022). Please cancel the duplicate."),
            ("VAT tax exempt certificate validation needed", "Our European entity qualifies for reverse charge VAT. Attached is our certificate for verification and tax exemption."),
            ("Refund request for unused enterprise add-on modules", "We purchased the Advanced Analytics module last quarter but did not activate it. Per our MSA agreement, we request a prorated refund."),
            ("Payment receipt missing for fiscal year-end tax audit", "Our auditors require signed payment receipts for all transactions between Q1 and Q4. Please export these immediately."),
            ("Currency billing mismatch from USD to EUR", "Our master services agreement specifies invoicing in EUR, but the latest bill arrived in USD. Please correct the currency.")
        ],
        "Account & Security": [
            ("Urgent: Suspicious login attempt from unrecognized IP in Eastern Europe", "Our security operations center detected unauthorized API token generation from an IP in Bucharest. Please freeze API credentials immediately."),
            ("Executive account locked out after multiple MFA failures", "Our CFO is locked out of the enterprise tenant and cannot approve quarterly payroll files. Urgent reset required."),
            ("Request for SOC-2 Type II audit report & penetration test summary", "Our vendor risk management review is due this Friday. We need the latest SOC 2 Type II report and third-party pentest executive summary."),
            ("Revoke admin access for terminated employee immediately", "John Doe (employee ID #4491) was offboarded today. Please revoke all Okta SSO provisions and GitHub integration tokens."),
            ("Enforce mandatory FIDO2 hardware key authentication across all admin accounts", "To comply with our ISO 27001 audit, we need domain-wide FIDO2 hardware token enforcement enabled for all org admins."),
            ("Audit log export request for compliance investigation", "We need immutable audit logs for user activity across the security settings panel for the last 90 days.")
        ],
        "General Inquiries": [
            ("Inquiry regarding 2027 product roadmap and feature deprecation", "Could your product management team share the anticipated timeline for the legacy REST v1 deprecation?"),
            ("Demo request for new conversational AI support module", "Our regional operations team would like to schedule a 30-minute demonstration of the automated ticketing platform."),
            ("Documentation clarification on rate limiting headers", "The developer docs state 1000 requests/minute, but we observe 429 throttling at 800 requests. Please clarify."),
            ("Request to transfer workspace ownership to new team lead", "Our project director has transitioned to another division. We need workspace administrative ownership transferred."),
            ("Holiday support coverage and emergency escalation matrix", "Please provide the scheduled holiday support contact directory and escalation contacts for upcoming Q4 holidays.")
        ]
    }

    tiers = ["Tier 1 Global Enterprise", "Tier 2 Mid-Market", "Tier 3 Growth"]
    tier_weights = [0.25, 0.45, 0.30]

    channels = ["Web Portal", "Email", "Live Chat", "API / Integration"]
    channel_weights = [0.45, 0.35, 0.15, 0.05]

    records = []
    base_time = datetime(2026, 1, 15, 8, 0, 0)

    category_keys = list(categories.keys())
    category_weights = [0.40, 0.25, 0.15, 0.20]  # Realistic ticket volume skew

    for i in range(1, n_samples + 1):
        cat = np.random.choice(category_keys, p=category_weights)
        tier = np.random.choice(tiers, p=tier_weights)
        channel = np.random.choice(channels, p=channel_weights)

        # Pick random subject and body pair
        template_subj, template_body = random.choice(categories[cat])

        # Add minor random noise/variation to text
        time_offset_days = np.random.randint(0, 240)
        time_offset_hours = np.random.randint(0, 23)
        time_offset_mins = np.random.randint(0, 59)
        ticket_time = base_time + timedelta(days=time_offset_days, hours=time_offset_hours, minutes=time_offset_mins)

        # SLA Target depends on Tier and Category
        if tier == "Tier 1 Global Enterprise":
            sla_target_hours = 4.0 if cat in ["Technical Support", "Account & Security"] else 8.0
        elif tier == "Tier 2 Mid-Market":
            sla_target_hours = 8.0 if cat in ["Technical Support", "Account & Security"] else 16.0
        else:
            sla_target_hours = 16.0 if cat in ["Technical Support", "Account & Security"] else 24.0

        # Simulate resolution time (log-normal distribution)
        if cat == "Technical Support":
            res_mean = 6.5 if tier == "Tier 1 Global Enterprise" else 11.0
            res_sigma = 0.5
        elif cat == "Account & Security":
            res_mean = 4.0 if tier == "Tier 1 Global Enterprise" else 7.5
            res_sigma = 0.4
        elif cat == "Billing & Invoicing":
            res_mean = 7.0 if tier == "Tier 1 Global Enterprise" else 14.0
            res_sigma = 0.4
        else:
            res_mean = 5.0
            res_sigma = 0.3

        resolution_time_hours = round(float(np.random.lognormal(mean=np.log(res_mean), sigma=res_sigma)), 2)
        resolution_time_hours = max(0.5, resolution_time_hours)

        sla_breach = 1 if resolution_time_hours > sla_target_hours else 0

        # Sentiment score (-1.0 to +1.0)
        if cat == "Account & Security" or "outage" in template_body.lower() or "500 error" in template_body.lower():
            sentiment_score = round(float(np.random.normal(loc=-0.65, scale=0.25)), 2)
        elif cat == "Billing & Invoicing" and "dispute" in template_subj.lower():
            sentiment_score = round(float(np.random.normal(loc=-0.45, scale=0.20)), 2)
        elif cat == "General Inquiries":
            sentiment_score = round(float(np.random.normal(loc=0.35, scale=0.20)), 2)
        else:
            sentiment_score = round(float(np.random.normal(loc=-0.15, scale=0.30)), 2)
        sentiment_score = max(-1.0, min(1.0, sentiment_score))

        # CSAT score (1 to 5)
        if sla_breach == 1 or sentiment_score < -0.5:
            csat = int(np.random.choice([1, 2, 3], p=[0.55, 0.35, 0.10]))
        else:
            csat = int(np.random.choice([3, 4, 5], p=[0.10, 0.40, 0.50]))

        # Urgency label
        if tier == "Tier 1 Global Enterprise" and (cat in ["Technical Support", "Account & Security"] or sentiment_score < -0.4):
            urgency = "Critical"
        elif cat in ["Technical Support", "Account & Security"] or tier == "Tier 1 Global Enterprise":
            urgency = "High"
        elif cat == "Billing & Invoicing":
            urgency = "Medium"
        else:
            urgency = "Low"

        # Construct full ticket text
        ticket_text = f"Subject: {template_subj}\nDescription: {template_body}"

        records.append({
            "ticket_id": f"TCK-{20260000 + i}",
            "created_at": ticket_time.strftime("%Y-%m-%d %H:%M:%S"),
            "customer_id": f"CUST-{random.randint(100, 999)}",
            "customer_tier": tier,
            "channel": channel,
            "ticket_subject": template_subj,
            "ticket_body": template_body,
            "full_ticket_text": ticket_text,
            "department": cat,
            "urgency": urgency,
            "sla_target_hours": sla_target_hours,
            "actual_resolution_hours": resolution_time_hours,
            "sla_breach": sla_breach,
            "sentiment_score": sentiment_score,
            "csat_score": csat
        })

    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "enterprise_support_tickets.csv")
    
    print("Generating synthetic enterprise dataset...")
    df = generate_synthetic_support_data(n_samples=3500)
    df.to_csv(out_path, index=False)
    print(f"Dataset successfully created at {out_path} with {len(df)} rows and {len(df.columns)} columns.")
    print("\nDepartment Distribution:\n", df['department'].value_counts())
    print("\nSLA Breach Rate:\n", df['sla_breach'].value_counts(normalize=True))
