from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (needed for frontend)

# Simple rule-based FAQ chatbot
FAQ_RESPONSES = {
    "how to apply": "You can apply through our internship portal at example.com/apply.",
    "deadline": "Application deadlines are usually posted on our website.",
    "about organization": "We are a tech-driven company offering AI-based internships.",
    "eligibility": "All undergraduate and postgraduate students are eligible to apply.",
    "contact": "You can contact us at contact@example.com."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response = "I'm not sure about that. Please check the FAQ section on our website."

    for key in FAQ_RESPONSES:
        if key in user_message:
            response = FAQ_RESPONSES[key]
            break

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
