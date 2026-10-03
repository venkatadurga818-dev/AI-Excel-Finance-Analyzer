# AI + Excel Finance Analyzer

AI-assisted finance analysis project that combines Microsoft Excel, Python, CSV data, and AI to organize financial transactions, analyze cash flow, detect anomalies, and produce structured business insights.

## Project Objective

Finance workflows often involve repetitive tasks such as classifying transactions, reconciling records, analyzing expenses, and preparing monthly reports. This project demonstrates how spreadsheet analysis, Python automation, and AI-assisted review can make those workflows more organized and efficient while preserving human judgement.

## What This Project Does

- Organizes financial transaction data
- Separates income and expenses
- Calculates total income and expenses
- Calculates net cash flow
- Calculates savings rate
- Summarizes expenses by category
- Flags potentially unusual or duplicate transactions
- Produces a concise management summary
- Provides structured output suitable for Excel-based analysis

## Tools Used

- Microsoft Excel
- Python
- CSV
- Pandas
- AI-assisted analysis

## Project Workflow

```text
Transaction Data
      ↓
Data Organization
      ↓
Income / Expense Classification
      ↓
Python + Excel Analysis
      ↓
Cash Flow & Category Analysis
      ↓
Anomaly Identification
      ↓
AI-Assisted Review
      ↓
Verified Business Insights
```

## Files

| File | Description |
|---|---|
| `README.md` | Project documentation |
| `financial_data.csv` | Synthetic transaction dataset |
| `finance_analyzer.py` | Python finance-analysis script |

## How to Run

Install the dependency:

```bash
pip install pandas
```

Run:

```bash
python finance_analyzer.py
```

The script reads `financial_data.csv`, calculates income/expense metrics, summarizes expenses by category, detects potential duplicates, and prints management-oriented insights.

## Example AI Prompt

```text
You are a finance analyst.

Review the transaction data and:

1. Separate income and expenses.
2. Identify the three largest expense categories.
3. Calculate the savings rate from the provided totals.
4. Flag unusual or potentially duplicate transactions.
5. Provide three practical observations.

Use only information available in the dataset.
Do not invent missing data.
Clearly distinguish facts from recommendations.
```

## Disclaimer

The included dataset is synthetic and does not contain personal financial information. AI-generated observations should be checked against the underlying transaction data before being used for financial decisions.
