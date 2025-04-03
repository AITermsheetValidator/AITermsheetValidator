# advanced_questions_termsheet.py

# Transaction Details - Identify risks in ownership and valuation
transaction_questions = [
    "Are there any discrepancies between the pre-closing and post-closing shareholding patterns?",
    "Does the proposed transaction lead to dilution of promoters' equity beyond the permissible limit?",
    "Is the valuation consistent with comparable industry benchmarks?",
    "Are the terms of advisory equity justified based on the value being delivered?",
    "Could the proposed instruments (equity/preference shares) potentially alter voting dynamics?"
]

# Key Considerations - Detect conflicts, inconsistencies, and operational risks
key_considerations_questions = [
    "Does the board composition give disproportionate control to any party?",
    "Are there any inconsistencies between pre-emptive rights and anti-dilution provisions?",
    "Are there clauses that may lead to conflicts between ROFO and ROFR rights?",
    "Do the lock-in and vesting conditions introduce unnecessary complexities that may affect promoter incentives?",
    "Could tag-along or drag-along clauses lead to forced exits or conflicts of interest?",
    "Are affirmative voting rights overly restrictive, limiting operational flexibility?",
    "Is the liquidation preference clause favorable to the investor but detrimental to the promoters?",
    "Do exit mechanisms conflict with drag-along rights or impose burdensome conditions?"
]

# Documentation and Incidental Matters - Legal and compliance-related risks
documentation_questions = [
    "Are the conditions precedent aligned with statutory approvals and regulatory compliance?",
    "Are there potential conflicts between representations, warranties, and statutory requirements?",
    "Do standstill provisions unduly limit the company's ability to pursue alternate deals?",
    "Are the events of default clauses too stringent, posing a risk of premature termination?"
]

# General Clauses - Strategic and operational flexibility
general_clauses_questions = [
    "Could confidentiality or exclusivity clauses limit future fundraising or partnerships?",
    "Are termination clauses well-defined to avoid ambiguity in case of disputes?",
    "Do amendment provisions provide sufficient flexibility without introducing loopholes?",
    "Could the governing law or jurisdiction create enforcement challenges in case of legal disputes?"
]

# Schedules and Shareholding Patterns - Hidden shifts in ownership and power
schedules_questions = [
    "Does the post-closing shareholding pattern indicate a loss of control for promoters?",
    "Are there any unexpected shifts in shareholding that might impact decision-making?"
]

# Compile All Questions by Section
all_questions = {
    "Transaction Details": transaction_questions,
    "Key Considerations": key_considerations_questions,
    "Documentation and Incidental Matters": documentation_questions,
    "General Clauses": general_clauses_questions,
    "Schedules and Shareholding Patterns": schedules_questions
}
