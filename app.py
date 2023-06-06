from flask import Flask, jsonify
from cli import print_cv
from retrive_data import Read_CV_Data

app = Flask(__name__)

app.cli.add_command(print_cv)

cv_data = Read_CV_Data.get_instance().retrive_data()

@app.route("/personal", methods=["GET"])
def get_personal():
    if "general_information" in cv_data:
        return jsonify(cv_data["general_information"])
    else:
        error_message = {"error": "General information not found"}
        return jsonify(error_message), 404

@app.route("/experience", methods=["GET"])
def get_experience():
    if "experience" in cv_data:
        return jsonify(cv_data["experience"])
    else:
        error_message = {"error": "Experience not found"}
        return jsonify(error_message), 404

@app.route("/education", methods=["GET"])
def get_education():
    if "education" in cv_data:
        return jsonify(cv_data["education"])
    else:
        error_message = {"error": "Educationn not found"}
        return jsonify(error_message), 404

if __name__ == "__main__":
    app.run()
