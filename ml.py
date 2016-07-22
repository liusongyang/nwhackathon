#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import json
import pandas as pd
import numpy as np

ml = Flask(__name__)

points = [
    {
        'time': 1,
        'temp': 60,
        'done': False
    },
    {
        'id': 2,
        'temp': 50,
        'done': False
    }
]

@ml.route('/hello')
def hello():
    return "Hello, World!"


@ml.route('/todo/api/ml', methods=['POST'])
def doML():
    
    inpt=u"[{\"flag\": \"False\", \"time\": 0,\"temp\":\"60\"},{\"flag\": \"False\", \"time\": 1,\"temp\":\"62\"}]"
    
    #read data 
    data_jason=json.loads(inpt)
    #convert it to Jason
    data=pd.DataFrame(data_jason)
    
    one_column = data.iloc[:,1].apply(lambda x: float(x)) #Temparature col
    
    outliers_MAD = one_column[mad_based_outlier(one_column)]
    
    #data.loc[:,"flag"] = None 
    data["flag"].iloc[outliers_MAD.index] = 1
    
    #convert data to Jason
    data_jason_flagged = df_to_json(data)
    
    #return jason file
    return data_jason_flagged
    
def mad_based_outlier(points, thresh=3.5):
    if len(points.shape) == 1:
        points = points[:,None]
    print points
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh

def df_to_json(y):
    j = "["
    for i in xrange(len(y)):
        line=y.loc[i,:]
        #item={"flag": line[0],"time": line[1],"temp":line[2]}
        item='{\"'+str(y.columns[0])+'\": ' +str(line[0])+', \"'+str(y.columns[1])+'\": '+ str(line[1])+', \"'+str(y.columns[2])+'\": '+str(line[2])+'}'
        #j.append(item)
        if i == 0:
            j=j+item
        else:
            j = j + ", " + item
                
    j=j+']'
    return j

	
if __name__ == '__main__':
    ml.run(debug=True)
