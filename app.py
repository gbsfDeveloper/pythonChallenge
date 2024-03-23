from flask import Flask, jsonify, request
from game import DiceGame
app = Flask(__name__)

@app.route("/")
def dice_probabilities():
    try:
        diceSize = request.headers.get('k')
        diceGame = DiceGame(diceSize, "Bob")
        probabilities, hasDiceSize = diceGame.getProbabilitiesData()
        objectKey = "probability" if hasDiceSize else "probabilities"
        return jsonify({"error": False, objectKey: probabilities})
    except Exception as error:
        return jsonify({"error": True, "message": str(error)})

if __name__ == '__main__':
    app.run()