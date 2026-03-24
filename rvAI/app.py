# from flask import Flask, request, redirect, render_template

# app = Flask(__name__)

# PROMPT_URL_MAP = {
#     "hospital": "https://prakruthihospital.com",
#     "manufacture": "https://nexus-analysis.com/",
#     "builders": "https://builderexhibitions.in/",
#     "realestate": "https://ssmdevelopers.in/",
#     "pharma industry": "https://srkcleanrooms.in/",
# }

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/process", methods=["POST"])
# def process():
#     user_prompt = request.form.get("prompt", "").strip().lower()
#     for key, url in PROMPT_URL_MAP.items():
#         if key in user_prompt:
#             return redirect(url)
#     return render_template("index.html", error=f"No match found for: {user_prompt}")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

PROMPT_URL_MAP = {
    "hospital": "https://prakruthihospital.com",
    "manufacture": "https://nexus-analysis.com/",
    "builders": "https://builderexhibitions.in/",
    "realestate": "https://ssmdevelopers.in/",
    "pharma industry": "https://srkcleanrooms.in/",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_prompt = request.form.get("prompt", "").strip().lower()
    for key, url in PROMPT_URL_MAP.items():
        if key in user_prompt:
            return redirect(url)
    # If no match, just refresh back to home page
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

