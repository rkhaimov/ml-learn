import base64
import json

import cv2
import requests


def image_to_string(image):
    url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyACaXt7I0ZBVtKaqTEo4-F9FEdULP-5nCg'

    post_fields = {"requests": [{"image": {"content": base64.b64encode(cv2.imencode('.png', image)[1]).decode()},
                                 "features": [{"type": "DOCUMENT_TEXT_DETECTION"}]}]}

    response = requests.post(url, json=post_fields, headers={'referer': 'https://brandfolder.com/'})

    result = json.loads(response.text)

    return result['responses'][0]['fullTextAnnotation']['text']
