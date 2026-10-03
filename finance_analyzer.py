"""AI + Excel Finance Analyzer
Reads financial_data.csv and produces a concise financial analysis.
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).with_name("financial_data.csv")

def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    """Load and validate the transaction dataset."""
    df = pd.read_csv(path)
    required = {"Date", "Description", "Category", "Type", "Amount"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    if df["Date"].isna().any() or df["Amount"].isna().any():
        raise ValueError("Date and Amount columns contain invalid values.")
    return df

def analyze(df: pd.DataFrame) -> dict:
    """Calculate core finance metrics and potential duplicate transactions."""
    income = df.loc[df["Type"].str.lower() == "income", "Amount"].sum()
    expenses = df.loc[df["Type"].str.lower() == "expense", "Amount"].sum()
    net_cash_flow = income - expenses
    savings_rate = (net_cash_flow / income * 100) if income else 0.0
    expense_by_category = (
        df.loc[df["Type"].str.lower() == "expense"]
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    duplicate_mask = df.duplicated(
        subset=["Date", "Description", "Category", "Type", "Amount"],
        keep=False,
    )
    duplicates = df.loc[duplicate_mask].sort_values(
        ["Date", "Description", "Amount"]
    )
    return {
        "total_income": income,
        "total_expenses": expenses,
        "net_cash_flow": net_cash_flow,
        "savings_rate": savings_rate,
        "expense_by_category": expense_by_category,
        "duplicates": duplicates,
    }

def print_report(results: dict) -> None:
    """Print a management-friendly analysis report."""
    print("\n=== AI + Excel Finance Analyzer ===")
    print(f"Total income:    {results['total_income']:,.2f}")
    print(f"Total expenses:  {results['total_expenses']:,.2f}")
    print(f"Net cash flow:   {results['net_cash_flow']:,.2f}")
    print(f"Savings rate:    {results['savings_rate']:.2f}%")
    print("\nExpense by category:")
    for category, amount in results["expense_by_category"].items():
        print(f"  - {category}: {amount:,.2f}")
    duplicates = results["duplicates"]
    print("\nPotential duplicate transactions:")
    if duplicates.empty:
        print("  None detected.")
    else:
        print(duplicates.to_string(index=False))
    print("\nAI-review prompts:")
    print("  1. Explain the largest expense categories.")
    print("  2. Review potential anomalies or duplicates.")
    print("  3. Summarize three business-relevant observations.")
    print("  4. Suggest follow-up questions using only the dataset.")

if __name__ == "__main__":
    data = load_data()
    results = analyze(data)
    print_report(results)
