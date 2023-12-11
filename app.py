from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        user_agent = request.form.get("user_agent")
        if url and user_agent:
            headers = {'User-Agent': user_agent}
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    content = response.text
                else:
                    content = f"Failed to fetch {url}. Status code: {response.status_code}"
            except Exception as e:
                content = f"Error while fetching {url}: {str(e)}"
        else:
            content = "Please provide both URL and User-Agent."
    else:
        content = ""

    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)
