### 1. Top 2 Critical Customer Friction Themes

*   **Theme 1: Opaque Fee Structures and Post-Transaction Cost Surprises**  
    *   **Context:** Over 55% of analyzed feedback highlights frustration with charges appearing without prior disclosure. Users cite confusion across three main flows: auto-debit fees during SIP executions, unexpected brokerage/statutory levies on order statements, and undisclosed deductions during fund withdrawals/redemptions. Even satisfied UI users demand clearer upfront breakdowns.
*   **Theme 2: Delayed Customer Support for Transaction Failures**  
    *   **Context:** Approximately 16% of reviews explicitly complain that support takes up to 3 business days to resolve payment/transaction failure inquiries. In fintech, unaddressed failed debits directly erode user trust regarding capital safety.

---

### 2. Identified Recurring Fee Confusion Point

*   **Depository Participant (DP) & Regulatory Transaction Charges**  
    *   *User Perception:* Customers interpret statutory and depository deductions (such as DP charges on equity sell orders, stamp duty, or payment gateway charges on SIP auto-debits) as "hidden brokerage" or "unauthorized withdrawal deductions" because they are only visible after order execution or statement generation.

---

### 3. Actionable Product Recommendations

#### For Theme 1: Fee Transparency & Cost Disclosure
1.  **Pre-Execution Cost Breakdown Sheet:**
    *   Embed an expandable *"Charges & Taxes"* bottom-sheet on the final order placement/SIP setup screen.
    *   Display a real-time ledger itemizing Brokerage, STT, Exchange Fees, GST, and applicable DP charges before the user confirms the order.
2.  **Contextual "Net Realizable Value" Indicator on Withdrawals:**
    *   When a user initiates an equity sale or withdrawal, display the exact gross amount minus estimated charges/applicable exit loads, showing the final net credit amount clearly.

#### For Theme 2: Transaction Failure Support Turnaround
1.  **Automated Payment Lifecycle Tracker:**
    *   Deploy a real-time visual tracker (Initiated → Bank Processing → Failed/Reversed) for failed auto-debits and orders, detailing the banking partner’s standard refund SLA (e.g., T+2 days) and unique UTR numbers.
2.  **Instant Self-Serve AI Resolution Bot:**
    *   Create an automated workflow in Help & Support specifically for transaction failures that checks server/bank logs instantly and creates high-priority auto-reconciliation tickets, removing the 3-day SLA bottleneck.

---

### 4. Weekly Product Pulse Summary

> **Weekly Product Pulse: Sentiment & Friction Review**  
> **Volume Analyzed:** 100 customer reviews  
> **Core Sentiment:** Mixed. While our core investment flows and dark mode UI continue to receive praise, satisfaction is substantially suppressed by pricing opacity and slow transaction-failure support.
>
> **Key Findings:**  
> 1. **Pricing Ambiguity:** Over half of all reviewed cohorts reported friction regarding post-transaction deductions, including auto-debit mandates, order statement brokerage, and withdrawal-related charges (predominantly DP and regulatory fees).  
> 2. **Support Lag on High-Stress Events:** Resolution times of up to 3 days for failed financial transactions create high churn risk and panic regarding capital security.  
>
> **Action Items:**  
> - **Sprint Priority:** Ship an upfront "Estimated Charges Breakdown" modal on all order execution, SIP setup, and redemption screens.  
> - **Support Engineering:** Partner with the Core Banking/Payments team to launch an instant self-serve refund tracker to bring transaction-failure ticket response times from 72 hours to under 5 minutes.

---

### 5. Standardized Fee Explanation Snippet: Depository Participant (DP) Charge

*   **Nature of Charge:** A flat regulatory fee levied by the depositories (CDSL/NSDL) and the depository participant whenever shares are debited from your demat account upon selling.
*   **Applicability:** Levied once per trading day per company (stock), irrespective of the number of shares sold. It does not apply to intraday trades or buy orders.
*   **Billing Mechanism:** Directly deducted from your trading ledger/sale proceeds rather than your linked bank account.
*   **Fixed Tariff:** Consists of a non-negotiable fee mandated by the depository plus a nominal Depository Participant processing charge, subject to applicable 18% GST.