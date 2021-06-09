import numpy as np
import tensorflow as tf
import midi_statistics
import utils
import os
from gensim.models import Word2Vec


syll_model_path = './enc_models/syllEncoding_20190419.bin'
word_model_path = './enc_models/wordLevelEncoder_20190419.bin'

syllModel = Word2Vec.load(syll_model_path)
wordModel = Word2Vec.load(word_model_path)




lyrics = [['E','Everywhere'],['very','Everywhere'],['where','Everywhere'],['I','I'],['look','look'],
         ['I','I'],['found','found'],['you','you'],['look','looking'],['king','looking'],['back','back']]


length_song = len(lyrics)
cond = []

for i in range(20):
    if i < length_song:
        syll2Vec = syllModel.wv[lyrics[i][0]]
        word2Vec = wordModel.wv[lyrics[i][1]]
        cond.append(np.concatenate((syll2Vec,word2Vec)))
    else:
        cond.append(np.concatenate((syll2Vec,word2Vec)))


flattened_cond = []
for x in cond:
    for y in x:
        flattened_cond.append(y)


model_path = './saved_gan_models/saved_model_best_overall_mmd'
# model_path = './saved_gan_models/saved_model_end_of_training'

x_list = []
y_list = []

print(length_song)
