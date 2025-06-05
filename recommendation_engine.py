from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    interests = data.get("interests", "").lower()
    skills = data.get("skills", "").lower()
    experience = data.get("experience", "").lower()

    # Basic rule-based logic (can later be replaced with ML model)
    if "ai" in interests or "machine learning" in interests or "python" in skills:
        recommendation = "AI / Machine Learning Internships"
    elif "web" in interests or "html" in skills or "javascript" in skills:
        recommendation = "Web Development Internships"
    elif "android" in interests or "java" in skills:
        recommendation = "Mobile App Development Internships"
    else:
        recommendation = "General Internship Opportunities"

    return jsonify({"recommendation": recommendation})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
