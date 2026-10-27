"""Northwind portal demo health service."""
from flask import Flask, jsonify

app = Flask("northwind-portal-demo")


@app.get("/healthz")
def healthz():
    return jsonify(status="ok", service="northwind-portal-demo", company="Northwind")


@app.get("/")
def index():
    return jsonify(
        message="Northwind Portal Demo App",
        docs="See deploy/ and docs/ in this repository",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
