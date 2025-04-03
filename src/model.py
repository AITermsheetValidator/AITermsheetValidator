# models/qa_model.py
import re
def sum_risk_levels(text):
    """Calculate the total risk and possible risk from the document."""
    total_risk = 0
    total_possible_risk = 0
    
    # Split the text into lines
    lines = text.splitlines()
    
    # Iterate through each line
    for line in lines:
        # Check if the line contains "Risk Level"
        if "Risk Level" in line:
            # Clean the line to remove unwanted characters like **, parentheses, etc.
            clean_line = re.sub(r'[^\w\s/]', '', line)  # Removes non-alphanumeric characters except / and spaces
            
            # Use regular expression to find numbers
            numbers = re.findall(r'\d+', clean_line)  # Find all numbers in the string
            
            if numbers:
                # Assume the first number is the numerator
                numerator = int(numbers[0])
                
                # Assume denominator is 10 if it's not explicitly given
                denominator = 10
                
                total_risk += numerator  # Add the numerator to total risk
                total_possible_risk += denominator  # Add the denominator to total possible risk
    
    return total_risk, total_possible_risk



def evaluate_risk_level(risk_percentage):
    """Evaluate risk based on the calculated risk percentage."""
    if risk_percentage < 30:
        return "Accept"
    elif 30 <= risk_percentage <= 70:
        risk_message = f"\nCurrent risk percentage is {risk_percentage}"
        return f"Please get reviewed by expert.{risk_message}"
       


    else:
        return "Reject"


def calculate_risk_and_evaluation(document):
    """Calculate risk percentage and evaluate risk level based on document content."""
    total_risk, total_possible_risk = sum_risk_levels(document)
    
    # Calculate the risk percentage
    if total_possible_risk > 0:
        risk_percentage = (total_risk / total_possible_risk) * 100
        risk_evaluation = evaluate_risk_level(risk_percentage)
        return risk_percentage, risk_evaluation
    else:
        return None, "No valid risk levels found."

# Read document content (replace with actual path to your document)
file_path = 'output/risk_summary.txt'  # Update with your file path

with open(file_path, 'r') as file:
    document = file.read()

# Calculate risk and get the evaluation
risk_percentage, risk_evaluation = calculate_risk_and_evaluation(document)