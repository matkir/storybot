import os
from flask import Flask, jsonify
from storyteller import Storyteller

app = Flask(__name__)
storyteller = Storyteller("storyteller.db", str(os.environ["OPENAI_API_KEY"]))


@app.route("/stories", methods=["GET"])
def get_stories():
    stories = storyteller.get_stories()
    return jsonify(stories)


if __name__ == "__main__":
    app.run(debug=True)
