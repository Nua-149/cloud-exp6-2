
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>Cloud Experiment 6.2</title></head>
      <body style="font-family: Arial; text-align: center; margin-top: 80px;">
        <h1>Azure Container Apps</h1>
        <h2>Experiment 6.2 Successful!</h2>
        <p>My containerized web application is running.</p>
        <p>Deployed using GitHub Actions CI/CD.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)