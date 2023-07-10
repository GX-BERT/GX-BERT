#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import os
import sys
import pandas as pd

rawlink = "https://raw.githubusercontent.com/GX-BERT/GX-BERT/main/GX-BERT_attention_track_example/GX-BERT_CTB_65k_median/"
folder = "GX-BERT_CTB_65k_median/"
with open(f'GX-BERT_url.txt', 'w') as w_writer:
    genes=os.listdir(folder)
    for elem in genes:
        files=os.listdir(f"{folder}/{elem}/")
        for file in files:
            w_writer.write(f"{rawlink}{elem}/{file}\n")
        
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%