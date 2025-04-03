# report_generator.py
import json

def generate_risk_summary(report_data):
    summary = "Term Sheet Risk Evaluation Report\n"
    summary += "="*50 + "\n"
    for section, details in report_data.items():
        summary += f"\n{section}\n" + "-"*30 + "\n"
        for item in details:
            summary += f"Question: {item['question']}\n"
            summary += f"Answer: {item['answer']}\n"
            summary += f"Risk Level: {item['risk']}\n"
            summary += "-"*30 + "\n"
    return summary

def save_summary_to_file(summary, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(summary)
