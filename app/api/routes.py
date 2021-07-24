from app import app
from app.models.emotion_predictor import predictor, response
import numpy as np
from flask import request, render_template


@app.route("/",methods=['POST'])
def predict_emo():
    sentence = [x for x in request.form.values()][0]
    opening = "you are feeling...."
    prediction = predictor(sentence)
    index = np.random.randint(0,3)
    reply = response(prediction,index)
    return render_template('index.html', sentence_text=sentence, opening_text=opening, prediction_text= prediction, reply_text = reply)

