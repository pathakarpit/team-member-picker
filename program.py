import pandas as pd
import random

#generating keys function
def cre_keys(datel,timel):
    keysl=[]
    for i in range(len(datel)):
        keysl.append((datel[i]*10000+timel[i]))
    return keysl
        
#crteating dictionary function        
def cre_dict(namel,keysl):
    dictionary={}
    for i in range(len(namel)):
        dictionary[keysl[i]] = namel[i]
    return dictionary

#instant draw function
def instant_draw(flag,slot,keysl,activel):
    draw=[]
    if flag:        #activity factor exist
        active=[]
        notactive=[]
        #making two diff list for active and non active members
        for i in range(len(keysl)):
            if activel[i]==1:
                active.append(keysl[i])
            if activel[i]==0:
                notactive.append(keysl[i])
        #sorting both the notactive list                
        notactive.sort()
        if len(active)<slot:
            draw=draw+active
            draw=draw+notactive[:(slot-len(draw))]
        else:
            draw = random.sample(active,k=slot)
        return draw
            
        
    else:       #activity factor dont exist
    #sorting the list
        keysl.sort()
        draw = random.sample(keysl,k=slot)
        return draw
            

#importing datasets
def imp_data():
    list_all= pd.read_csv('Name.csv')
    name = list_all.iloc[:,0].values
    date=list_all.iloc[:,1].values
    time=list_all.iloc[:,2].values
    active=list_all.iloc[:,3].values
    return name,date,time,active

#making dictionary
def make_dict(date,time,name):
    keys=cre_keys(date,time)
    Dict=cre_dict(name,keys)
    return keys,Dict

