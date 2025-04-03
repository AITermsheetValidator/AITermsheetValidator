import json
import os
import logging
from ocr_extraction import extract_text_from_pdf, save_text_to_file
from qa_model import answer_question
from risk_analysis import analyze_responses, save_risk_report
from report_generator import generate_risk_summary, save_summary_to_file
from model import calculate_risk_and_evaluation
from advanced_questions_termsheet import all_questions

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define paths
DATA_DIR = "data"
OUTPUT_DIR = "output"

PDF_PATH = os.path.join(DATA_DIR, "TERM_SHEET_EQUITY.pdf")
TEXT_FILE_PATH = os.path.join(DATA_DIR, "termsheet.txt")
OUTPUT_JSON_PATH = os.path.join(OUTPUT_DIR, "results.json")
OUTPUT_SUMMARY_PATH = os.path.join(OUTPUT_DIR, "risk_summary.txt")


def process_pdf(pdf_path=PDF_PATH, text_file_path=TEXT_FILE_PATH, output_json=OUTPUT_JSON_PATH):
    """
    Extract text from the given PDF and answer predefined questions.
    """
    try:
        logging.info("Extracting text from PDF...")
        extracted_text = extract_text_from_pdf(pdf_path)
        save_text_to_file(extracted_text, text_file_path)

        logging.info("Answering predefined questions...")
        responses = {}
        for section, questions in all_questions.items():
            responses[section] = {}
            for question in questions:
                responses[section][question] = answer_question(question, extracted_text)

        logging.info("Analyzing risk and generating report...")
        risk_report = analyze_responses(responses)
        save_risk_report(risk_report, output_json)

        return risk_report
    except Exception as e:
        logging.error(f"Error in processing PDF: {e}")
        return None


def evaluate_risk(risk_report, output_summary=OUTPUT_SUMMARY_PATH):
    """
    Generate risk summary and calculate risk percentage.
    """
    try:
        logging.info("Generating risk summary...")
        risk_summary = generate_risk_summary(risk_report)
        save_summary_to_file(risk_summary, output_summary)

        logging.info("Calculating risk evaluation...")
        with open(output_summary, 'r') as file:
            document = file.read()

        risk_percentage, risk_evaluation = calculate_risk_and_evaluation(document)

        if risk_percentage is not None:
            logging.info(f"Risk Percentage: {risk_percentage:.2f}%")
            logging.info(f"Risk Evaluation: {risk_evaluation}")
        else:
            logging.warning(risk_evaluation)

        return risk_percentage, risk_evaluation
    except Exception as e:
        logging.error(f"Error in evaluating risk: {e}")
        return None, None


if __name__ == "__main__":
    logging.info("Starting Term Sheet Validation Process...")

    risk_report = process_pdf()
    if risk_report:
        logging.info("Risk analysis completed successfully.")
        evaluate_risk(risk_report)
        logging.info("Risk evaluation completed! Check 'output/risk_summary.txt' for detailed insights.")
    else:
        logging.error("Process failed due to errors in text extraction or risk analysis.")
