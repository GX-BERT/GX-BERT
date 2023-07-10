# GX-BERT

<img alt="Keras" src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white"/>
<img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" />
<img alt="NumPy" src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"/>

# Repository Description
- In Workflow_TPU, you can find two example notebooks of GX-BERT on the CTB dataset using TPU:
  - GIT_GX-BERT_CTB_TPU_TRAIN.ipynb shows you how to train, evaluate, save, and load GX-BERT on our CTB (seq_len = 65k, labels = median mRNA levels). Moreover, it shows how to save the attention tracks and gradient x input into organized directories. It will be useful to upload your tracks to the UCSC Genome Browser.
  - GIT_GX-BERT_CTB_TPU_MA_ML.ipynb shows you how to load a model and plot the average attention matrix and the UMAP of the heads' CLS token.
- In GX-BERT_attention_track_example, you can find the attention tracks and gradient x input of the model used in the paper (you can load the same model from Saved_Models/GX-BERT_CTB_65k as shown in notebooks GIT_GX-BERT_CTB_TPU_TRAIN.ipynb and GIT_GX-BERT_CTB_TPU_MA_ML.ipynb). In particular, we uploaded the tracks of the gene (gene_id ENSG00000132549, gene_name VPS13B) used for the UCSC Genome Browser plot shown in the paper. In the same directory, you can find a script that creates a text file that can be used to upload hundreds of attention tracks in a few seconds to the UCSC Genome Browser (url.py), as well as the result of that script (GX-BERT_url.txt). In practice, you need to run the script to create a file with a raw link per line, and each raw link points to an attention track file generated as shown in notebook GIT_GX-BERT_CTB_TPU_TRAIN.ipynb. You can just copy and past the generated text in the input box of the UCSC Genome Browser input form "Paste URLs or data" that can be found on the page https://genome.ucsc.edu/cgi-bin/hgCustom that can be found following the steps: My Data > Custom Tracks > add custom tracks.
- In Classes/GX_BERT.ipynb, you can find the class that manages GX-BERT and Transformer models.
- In Classes/DataManager.ipynb, you can find the class that manages Xpresso's data.
- In Hyperparameters, you can find the best hyperparameters found for each dataset.

# Credits

The data relating to the promoters, half-life features and median gene expression levels are available thanks to the following publication:
 - Agarwal V, Shendure J. [Predicting mRNA abundance directly from genomic sequence using deep convolutional neural networks](https://www.cell.com/cell-reports/pdf/S2211-1247(20)30616-1.pdf). 2020. Cell Reports 31 (7), 107663
