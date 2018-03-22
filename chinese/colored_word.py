from termcolor import colored
all_file=open('all_del_person_info.txt','r').read()
f=open('ntotal.txt','r',encoding='utf-16').readlines()
idioms=[]
for text in f:
    text=text.split()
    idioms.append(text[1])
idioms=idioms[1:]
for idiom in idioms:
    all_file=all_file.replace(idiom,colored(idiom, 'grey', attrs=['reverse']))

print(all_file)