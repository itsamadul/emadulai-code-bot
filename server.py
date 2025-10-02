from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Directly add your OpenAI API Key here
openai.api_key = "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"

@app.route("/generate_code", methods=["GET"])
def generate_code():
    prompt = request.args.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided."})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        code_text = response['choices'][0]['message']['content']
        return jsonify({"code": code_text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
