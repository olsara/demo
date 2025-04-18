# Describe the image and what's observed in it

# Import necessary libraries
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Connect to API through subscription key and endpoint
subscription_key = "your_real_key_here"
endpoint = "https://your-resource-name.cognitiveservices.azure.com/"

# Authenticate
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Get image
local_image = open("images/street.jpeg", "rb")

# Call API
description_result = computervision_client.describe_image_in_stream(local_image)

# Return the result
print("Description of local image: ")
if (len(description_result.captions) == 0):
    print("No description detected.")
else:
    for caption in description_result.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()