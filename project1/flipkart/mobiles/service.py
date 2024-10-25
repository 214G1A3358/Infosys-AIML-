#serive.py
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
endpoint="https://lang-instance1.cognitiveservices.azure.com/"
key="6a9f60d0e4044e569667f904036f53e5"
cred=AzureKeyCredential(key)
client=TextAnalyticsClient(endpoint=endpoint,credential=cred)