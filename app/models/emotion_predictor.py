import pandas as pd
import numpy as np
import tensorflow as tf

from app import tokenizer, model, response_dict


def predictor(sentence):
    sample_series = pd.Series(sentence)
    sample_tkn = tokenizer.texts_to_sequences(sample_series)
    sample_pad = tf.keras.preprocessing.sequence.pad_sequences(sample_tkn, maxlen=120, padding="post",
                                                               truncating="post")

    sample_pred = (model.predict(sample_pad) > 0.5).astype("int32")

    # To Label Encoding
    sample_pred = np.argmax(sample_pred, axis=-1)
    prediction_sample = pd.DataFrame(data=sample_pred, columns=['prediction'])
    prediction_sample['emotion'] = prediction_sample.prediction.replace(
        {0: 'joy', 1: 'anger', 2: 'love', 3: 'sadness', 4: 'fear'})

    predicted_emo = prediction_sample.emotion[0]

    return predicted_emo

def response(predicted_emo, index):
    reply = response_dict[predicted_emo][index]
    return reply