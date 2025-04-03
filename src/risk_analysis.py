# risk_analysis.py
import json
import requests
def assess_risk(answer):
    # Define risk conditions (example)
    try:
        url = "https://api.perplexity.ai/chat/completions"

        headers = {
            "Authorization": f"Bearer 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",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "sonar",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a legal and financial expert analyzing term sheets. The user enters a certain sentence about the term sheet, and you analyze the risk level(1-10)."
                },
                {
                    "role": "user",
                    "content": f"Context: {answer}\nAnalyse the risk level\n."
                }
                
            ],
            "max_tokens": 123,
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_responses(responses):
    risk_report = {}
    for section, answers in responses.items():
        risk_report[section] = []
        for question, answer in answers.items():
            risk_score = assess_risk(answer)
            risk_report[section].append({"question": question, "answer": answer, "risk": risk_score})
    return risk_report

def save_risk_report(report, output_path):
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=4)
