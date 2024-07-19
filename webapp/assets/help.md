# Help Page

This is a guide on how to use this application accoring to your needs. There are two ways you can access the application, first by the __WebUI__ and second using the __API__. 

## WebUI

The web UI is built using [Gradio](https://gradio.app/). You have to first input the sentence that you want to clasify in the _Input Text_ box and then add the labels in the _Candidate Labels_ box. The labels should be comma separated, example: __positive, negative, neutral__. Once both the text boxes are filled, press the __Submit__ button to start the inference.

## API

Along with the web UI there is also an API that can be accessed by sending a `POST` request to `/predict` endpoint with the following JSON in the request body:

```json
{
  "text": "Text to classify",
  "labels": ["label-1", "label-2", "label-3"]
}
```

The sample response should be:

```json
{
    "labels": ["label-1", "label-2", "label-3"],
    "scores": [0.75, 0.1, 0.15]
}
```