import os
from azure.ai.inference import ImageEmbeddingsClient
from azure.identity import DefaultAzureCredential
import numpy as np

client = ImageEmbeddingsClient(
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), 
    credential=DefaultAzureCredential(),
    model="Cohere-embed-v3-english"
)

image_input= ImageEmbeddingInput.load(image_file="sample1.png", image_format="png")
response = client.embed(
    input=[ image_input ],
)

for embed in response.data:
    print("Embeding of size:", np.asarray(embed.embedding).shape)

print("Model:", response.model)
print("Usage:", response.usage)
