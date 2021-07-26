from app import app
from app.models.emotion_predictor import predictor, response, emotion_color
import numpy as np
from flask import request, render_template


@app.route("/",methods=['POST'])
def predict_emo():
    sentence = [x for x in request.form.values()][0]
    opening = "your emotion dominated by..."
    prediction = predictor(sentence)
    index = np.random.randint(0,3)
    reply = response(prediction,index)
    color_config = emotion_color(prediction)
    return render_template('index.html', sentence_text=sentence, opening_text=opening, prediction_text= prediction, reply_text = reply, color_config = color_config )

