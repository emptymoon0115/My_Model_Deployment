from typing import Text
import numpy as np
import tensorflow as tf
import midi_statistics
import utils
import os
from gensim.models import Word2Vec

def bell_prediction(text):
    
    syll_model_path = './enc_models/syllEncoding_20190419.bin'
    word_model_path = './enc_models/wordLevelEncoder_20190419.bin'

    syllModel = Word2Vec.load(syll_model_path)
    wordModel = Word2Vec.load(word_model_path)



        
    #text=[x for x in input("공백 구분해서 text 입력: ").split()]
    text2=[x for x in text.split()]
    #iprint(text)
    lyrics=[[x,x] for x in text2]
    #print(lyrics)
    #length_song = len(lyrics)
    #print(length_song)

    
   # lyrics = [['E','Everywhere'],['very','Everywhere'],['where','Everywhere'],['I','I'],['look','look'],
    #        ['I','I'],['found','found'],['you','you'],['look','looking'],['king','looking'],['back','back']]

    
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



    with tf.Session(graph=tf.Graph()) as sess:
        tf.saved_model.loader.load(sess, [], model_path)
        graph = tf.get_default_graph()
        keep_prob = graph.get_tensor_by_name("model/keep_prob:0")
        input_metadata = graph.get_tensor_by_name("model/input_metadata:0")
        input_songdata = graph.get_tensor_by_name("model/input_data:0")
        output_midi = graph.get_tensor_by_name("output_midi:0")
        feed_dict = {}
        feed_dict[keep_prob.name] = 1.0
        condition = []
        feed_dict[input_metadata.name] = condition
        feed_dict[input_songdata.name] = np.random.uniform(size=(1, 20, 3))
        condition.append(np.split(np.asarray(flattened_cond), 20))
        feed_dict[input_metadata.name] = condition

        generated_features = sess.run(output_midi, feed_dict)
        sample = [x[0, :] for x in generated_features]
        sample = midi_statistics.tune_song(utils.discretize(sample))
        midi_pattern = utils.create_midi_pattern_from_discretized_data(sample[0:length_song])
        destination = "test_success.mid"
        #midi_pattern.write(destination)


        print('done')

        #return midi_pattern.write(destination)

        #return model.predict(x_test)
        #return print("FINISH")
        return midi_pattern.write(destination)
        # 필요한거
        # return midi ---> 악보변환, 음악재생  --> 최종으로 안되면 그냥 mid파일 다운



# bell_prediction("lyrics 넣기")  # 이거먼저
#text="hi my friend"
#bell_prediction(text)  