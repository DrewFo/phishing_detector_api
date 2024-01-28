from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

###### FOR THE CLASSIFIER ######
from simpletransformers.classification import ClassificationModel

# Access our trained model
model = ClassificationModel("distilbert", 'gpmodel', use_cuda=False)

# to avoid deadlocks during concurrency
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def is_phishing(input_email):
    class_list = [False, True]
    predictions, _ = model.predict([input_email])

    return(class_list[predictions[0]])

################################

app = FastAPI()

class Item(BaseModel):
    email: str

@app.post('/api/post/')
async def post_handling(item: Item):
    
    return {True if is_phishing(item.email) else False}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
