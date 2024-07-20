# Zero Shot Text Classification

This is the source code for my Huggingface Space deployment. You can checkout the deployed application on [Huggingface Spaces](https://huggingface.co/spaces/arnabdhar/Zero-Shot-Classification-DeBERTa-Quantized). The task of Zero Shot Classification is a Natutal Language Processing technique where a model can __classify text into categories it has not seen during training__. This is acheived by training a model like DeBERTa on a variety of NLP tasks allowing the model to generalize and predict the most relevant class for a given text input based on the context provided by candidate labels.

I have used a [DeBERTa](https://arxiv.org/pdf/2006.03654) model architecture that excels at Zero Shot Tasks very well. I have quantized a finetuned model, [sileod/deberta-v3-base-tasksource-nli](https://huggingface.co/sileod/deberta-v3-base-tasksource-nli) provided by [Damien Sileo](https://huggingface.co/sileod) to further improve the inference latency. The model has been quantized using Huggingface Optimum for ONNX. You can see the [quantize.ipynb](./quantize.ipynb) for the source code for quantization.

## Running the Application

To run the application, I highly recommend using Docker but there are also other ways to get started. But first you have to clone the repository onto your local machine.

```bash
$ git clone https://github.com/arnabd64/Zero-Shot-Text-Classification.git
$ cd Zero-Shot-Text-Classification
```

### Using Docker

1. Build the Docker Image:

```bash
$ docker build -t zero-shot-text-classification:latest .
```

2. Run the following docker command:

```bash
$ docker run -itd \
-p 8000:8000  \
-e HF_MODEL=pitangent-ds/deberta-v3-nli-onnx-quantized \
-e PORT=8000 \
-e WORKERS=2 \
zero-shot-text-classification:latest
```

After running the docker container wait for a few minutes for the model to download and load into the memory.

### Using Docker Compose (Recommended)


```bash
$ docker compose up -d --build
```
After running the docker compose wait for a few minutes for the model to download and load into the memory.

### Using python

__Note:__ Use python 3.11 or later (Python 3.10 should work but I have not yet tested it)

1. Create a virtual environment and install dependencies

```bash
# create a virtual environment
$ python -m venv .venv

# activate the environment
$ .venv/bin/activate # on linux and macOS
$ .venv/Scripts/Activate.ps1 # on Windows

# install dependencies
$ pip install -e .
```

2. Set the following Environment Variables

```bash
HF_MODEL=pitangent-ds/deberta-v3-nli-onnx-quantized
PORT=8000
WORKERS=2
```

3. Run the application

```bash
$ python main.py
```