from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
import sys

#   The Quickstarts in this file are for the Computer Vision API for Microsoft
#   Cognitive Services. In this file are Quickstarts for the following tasks:
#     - Describing images
#     - Categorizing images
#     - Tagging images
#     - Detecting faces
#     - Detecting adult or racy content
#     - Detecting the color scheme
#     - Detecting domain-specific content (celebrities/landmarks)
#     - Detecting image types (clip art/line drawing)
#     - Detecting objects
#     - Detecting brands
#     - Recognizing printed and handwritten text with the batch read API
#     - Recognizing printed text with OCR


# Add your Computer Vision subscription key and endpoint to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()



def create_cv_client():
# Instantiate a client with your endpoint and key
# Create a CognitiveServicesCredentials object with your key, and use it with your endpoint to create a Co      >
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    return computervision_client


