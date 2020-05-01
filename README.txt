>>>How to run the files ?

1) Make sure the system has all the necessary requirements as mentioned in the requirements.txt
2) Copy all the files into one directory.
3) Open the Data_preprocessing.ipynb notebook and run the the entire notebook to generate the datasets
4) Run the Other_models.ipynb for creating Baseline, MLP, SVM, DT, RF and KNN models
5) Run the BiLSTM.ipynb for creating the BiLSTM model.


>>>File Structure :

Current Directory contains : 

baseline.py - contains the baseline model
evaluate.py - contains helper functions for calculating evalution metrics and plotting confusion metrics
Data_preprocessing.ipynb - data preprocessing notebook
BiLSTM_model.ipynb - notebook containing implementation of BiLSTM model
Other_models.ipynb - notebook containing implementation of traditional machine learning algorithms including baseline 
Report.pdf - Report File for the project
requirements.txt - requirements for the project environment
README.txt 

datasets directory contains : 

Train.csv - original dataset from kaggle
Mapping.csv - origingal mapping file from Kaggle
balanced_data.csv - dataset used for training models in this project
balanced_mapping.csv - mapping for the balanced_data.csv


>>>Steps to replicate environment : 

1) Make sure GPU, Visual Studio and anaconda are installed
2) Open anaconda prompt and execute this command to create a new environment: 

	conda create --name emoji_prediction_env tensorflow-gpu anaconda

3) Execute this command to enter the newly created environment : 
	
	conda activate emoji_prediction_env

4) Install gensim library for word2vec embeddings using one of the two options:

	conda install gensim 

OR
	pip isntall gensim

NOTE: If have trouble running the model with GPU Run below two command
		conda install -c anaconda cudnn
		conda install -c anaconda cudatoolkit
5) All the necesary libraries are now installed and open jupyter notebook to run all the files!
