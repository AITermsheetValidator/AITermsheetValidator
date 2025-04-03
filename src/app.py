from main import process_pdf, evaluate_risk
import logging
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define paths
DATA_DIR = "data"
OUTPUT_DIR = "output"

PDF_PATH = os.path.join(DATA_DIR, "TERM_SHEET_EQUITY.pdf")
TEXT_FILE_PATH = os.path.join(DATA_DIR, "termsheet.txt")
OUTPUT_JSON_PATH = os.path.join(OUTPUT_DIR, "results.json")
OUTPUT_SUMMARY_PATH = os.path.join(OUTPUT_DIR, "risk_summary.txt")

@app.route('/analyze_termsheet', methods=['POST'])
def analyze_termsheet():
    logging.info("Starting Term Sheet Validation Process...")

    try:
        risk_report = process_pdf(PDF_PATH)
        if not risk_report:
            logging.error("Process failed due to errors in text extraction or risk analysis.")
            return jsonify({"error": "Text extraction or risk analysis failed"}), 500

        logging.info("Risk analysis completed successfully.")
        risk_summary = evaluate_risk(risk_report)

        logging.info("Risk evaluation completed! Check 'output/risk_summary.txt' for detailed insights.")
        
        return jsonify({"message": "Analysis complete", "risk_summary": risk_summary}), 200

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == "__main__":
    print("Flask server is starting on http://localhost:5000...")
    app.run(debug=True)
