from typing import Any, Dict, List, Optional
from typing_extensions import TypedDict

class DebtState(TypedDict):
    name: Optional[str]
    type: Optional[str]
    balance: Optional[float]
    apr: Optional[float] | None
    min_payment: Optional[float]
    due_day: Optional[int]
    credit_limit: Optional[float]

class CashflowState(TypedDict):
    net_income_monthly: Optional[float]
    essential_expenses: Optional[float]
    extra_budget: Optional[float]
    emergency_fund_min: Optional[float]

class IssueState(TypedDict):
    level: Optional[str]
    field: Optional[str]
    message: Optional[str]

class DebtIntakeState(TypedDict):
    stage: Optional[str]
    source: Optional[str]
    debts: Optional[list[DebtState]]
    cashflow: Optional[CashflowState]
    usage_metadata: Optional[dict[str,Any]]
    issues: Optional[list[IssueState]]

