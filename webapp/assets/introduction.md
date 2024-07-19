# Zero Shot Text Classification

_Zero-shot text classification_ is a natural language processing technique where a model can __classify text into categories it has not seen during training__. This method leverages pre-trained language models, such as the [BART](https://huggingface.co/facebook/bart-base) model or the [DeBERTa](https://huggingface.co/microsoft/deberta-v3-base) model, to perform classification tasks without needing additional labeled data for the new categories. The models are typically trained on a variety of tasks, allowing them to generalize and predict the most relevant class for a given text input based on the context provided by candidate labels. This approach is particularly useful when labeled data is scarce or unavailable for certain categories, making it a cost-effective and time-saving solution for various applications