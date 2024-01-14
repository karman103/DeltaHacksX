import streamlit as st
from PIL import Image
from fastai.vision.all import load_learner
from datetime import datetime
from ultralytics import YOLO
import sys
import re
import os

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

resnet50_Model = load_learner(f'../result-resnet50.pkl')
nonLivingObjects = [
    1,2,3,4,5,6,7,8,9,10,
    11,12,13,24,25,26,27,28,29,30,
    31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50,
    51,52,53,54,55,56,57,58,59,60,
    61,62,63,64,65,66,67,68,69,70,
    71,72,73,74,75,76,77,78,79
]

st.set_page_config(layout="wide", page_title="Waste Classifier")

st.write("## Waste Classifier Prototype")


def truncate(num):
    return re.sub(r'^(\d+\.\d{,3})\d*$', r'\1', str(num))
  

def predictWaste(filename):
    response = []
    img = Image.open(filename)
    YOLOv8_model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
    results = YOLOv8_model(img)
    for result in results:
        detection_count = result.boxes.shape[0]
        for i in range(detection_count):
            cls = int(result.boxes.cls[i].item())
            name = result.names[cls]
            confidence = truncate(float(result.boxes.conf[i].item()))
            bounding_box = result.boxes.xyxy[i].cpu().numpy()
            
            if cls not in nonLivingObjects:
                continue
            
            newFile = f"{filename.split('.')[0]}-{len(response)}.{filename.split('.')[-1]}"
            img.crop(bounding_box).save(newFile)
            
            prediction = resnet50_Model.predict(newFile)
            num = int(prediction[1].numpy().tolist())
            prob = truncate(float(prediction[2].numpy()[num]))
            print(f'Classified as {prediction[0]}, Class number {num} with probability {prob}')
            response.append(
                {
                    'object_name': name,
                    'object_confidence': confidence,
                    'waste_predicted': prediction[0], 
                    'waste_probability': prob
                }
            )
            os.remove(newFile)
    return response


def process_image(upload):
    ts = datetime.timestamp(datetime.now())
    orignal_image = Image.open(upload)
    image_name = f'{ts}-{upload.name}'
    orignal_image.save(image_name)
    col2.image(orignal_image)

    response = ''
    for i in predictWaste(image_name):
        response += f'Classified as {i["object_name"].upper()}, (Confidence - {i["object_confidence"]}) | Categorized as {i["waste_predicted"].upper()}, (Confidence - {i["waste_probability"]})'
        response += '\n'

    col2.write(f"{response}")
    os.remove(image_name)

col1, col2 = st.columns(2)
picture = col1.camera_input("Take a picture!")

if picture:
    process_image(upload=picture)

st.write('''
The aim is to build a model for waste classification that identifies among the different classes:\n
- cardboards
- compost
- glass
- metal
- paper
- plastic
- trash
'''
)
