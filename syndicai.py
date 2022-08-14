# -*- coding: utf-8 -*-
"""syndicai

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vzs5PaV7xijxVyYkOVPG0P2FZxoikNRx
"""

import torch
from PIL import Image 


class PythonPredictor:

    def __init__(self, config):
        """ Download pretrained model. """
        #self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).autoshape()
        self.model = torch.jit.load('model_scripted_defect.pt').autoshape()

    def predict(self, payload):
        """ Run a model based on url input. """

        # Inference
        img = url_to_img(payload["url"])
        outputs = self.model(img)
        _, preds = torch.max(outputs, 1)
        pred = preds.cpu()
        
        return pred  #img_to_bytes(box_img)

