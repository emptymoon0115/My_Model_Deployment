#lyrics = [['E','Everywhere'],['very','Everywhere'],['where','Everywhere'],['I','I'],['look','look'],
        #['I','I'],['found','found'],['you','you'],['look','looking'],['king','looking'],['back','back']]


#length_song = len(lyrics)


text="hello my friend"
#text=[x for x in input("공백 구분해서 text 입력: ").split()]
text2=[x for x in text.split()]

#iprint(text)
lyrics=[[x,x] for x in text2]
print(lyrics)
length_song = len(lyrics)
print(length_song)


