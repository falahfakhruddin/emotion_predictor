from flask import Flask, render_template, request
from importlib import import_module

import tensorflow as tf
import pickle
import os
import numpy



def init_tokenizer():
    # Load Tokenizer
    tokenizer_path = 'tokenizer.pickle'
    with open(tokenizer_path, 'rb') as handle:
        tokenizer_rerun = pickle.load(handle)
    return tokenizer_rerun


def init_model():
    # Load Model checkpoint
    model_path = 'my_model.h5'
    return tf.keras.models.load_model(model_path)
    
def init_response():

    joy = ["If you happy and you know it clap your hand! *clap* *clap* *clap*", 
           "Good thing that I wear sunglasses. Because you look so bright! B)",
           "So happy for you! Don't forget to spread your happiness to others!"]
    
    sadness = ["It may sound even sadder, but an act of fake smiling can actually lift the mood.",
               "Every cloud has a silver lining. It is not a easy to be patient, but try it and good things will eventually come.",
               "It's always darkest before the dawn. I know it is hard, but try your best."]
    
    anger = ["Sometimes anger is an effective solution. But most of the time, it isn't. Calm down, take a deep breath.",
    "If you are standing now, sit down for a while. If you are still angry after that, lay down for a while, take a deep breath.",
    "Forgive, when someone/something makes a mistake. Like we want to be forgiven when we make a mistake."]
    
    love = ["Uuuu looks like someone is in love <3",
    "Are you having a fever? Your face is all red *smirk :)",
    "No wonder you are giggling all day!"]
    
    fear = ["I can hear how scared you are. Try to reach someone close to you.",
    "It is normal to be afraid, try to reach someone close to you.",
    "It sounds hard. Try to reach someone close to you. Or try to do something else to free your mind from what bothers you."]
    
    emotional_response = {"joy" : joy, "sadness":sadness, "anger": anger, "love": love, "fear": fear}
    
    return emotional_response
    

    


def register_blueprints(app):
    module_name = 'api'
    module = import_module('app.{}.routes'.format(module_name))
    app.register_blueprint(module.blueprint)

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'test_flask', 'templates')

app = Flask(__name__, template_folder=template_dir)
tokenizer = init_tokenizer()
model = init_model()
response_dict = init_response()

from app.api import routes
from app.views import views


