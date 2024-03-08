# Evaluation

Across the different VLM architectures being developed, there are a variety of setups needed to run the models and evaluate them. Thankfully, many methods allow the model to be run interactively through a REST API. The current repository contains code to abstract the particularities of each setup away: the model is run on a server, and a test runner instance connects to the server to perform model evaluation.