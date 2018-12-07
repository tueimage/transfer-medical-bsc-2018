import pickle
import matplotlib.pyplot as plt
import numpy as np
import random

from AADatasets import import_mnist, import_dogcat, import_melanoom,import_kaggleDR, pre_processing, make_pre_train_classes, get_data, more_data, equal_data_run, val_split
from AAPreTrain import make_model,train_model, config_desktop
from AATransferLearn import get_feature_vector, preform_svm, auc_svm
from AAlogic import test_script, menegola_plane
from LabnotesDoc import doc




# test_script()

params = {'img_size_x':224,'img_size_y':224,'norm':False,'color':True, 'pretrain':None, "equal_data":False, "shuffle": True, "epochs": 50 , "val_size":2000,"test_size":4000, "Batch_size": 16}
file_path = r"D:\kaggleDR"
pickle_path = r"D:\pickles\kaggleDR"
model_path = r"D:\models\Epochs_"
config_desktop()

print('Pickle cant handle 4gb, split it up')

try:
    print("Try to import pickle")
    try:
    	zippy = pickle.load(open( f"{pickle_path}.p", "rb" ))
    except:
    	zippy = pickle.load(open( f"{pickle_path}_part1.p", "rb" ))
    	zippy2 = pickle.load(open( f"{pickle_path}_part2.p", "rb" ))
    	zippy.append(zippy2)

    print("succeed to import pickle")
    zippy = list(zippy)
    random.shuffle(zippy)
    x,y = zip(*zippy)
    x = np.array(x)
    y = np.array(y)
    x_test,y_test,x,y = val_split(x,y, params["test_size"])
    x_val,y_val,x,y = val_split(x,y, params["val_size"])

except:
    print("Failed to import pickle")    
    x,y = import_kaggleDR(file_path, params['img_size_x'],params['img_size_y'], norm = params["norm"], color = params["color"])
    if params["equal_data"] == True:
        x,y = equal_data_run(y,x)
    zip_melanoom = zip(x,y)
    if len(zip_melanoom) > 20000:
    	pickle.dump( zip_melanoom[:int(len(zip_melanoom)/2)], open( f"{pickle_path}_part1.p", "wb" ))
    	pickle.dump( zip_melanoom[int(len(zip_melanoom)/2):], open( f"{pickle_path}_part2.p", "wb" ))
    else:
    	pickle.dump( zip_melanoom, open( f"{pickle_path}.p", "wb" ))
    zippy = list(zip_melanoom)
    random.shuffle(zippy)
    x,y = zip(*zippy)
    x = np.array(x)
    y = np.array(y)
    x_test,y_test,x,y = val_split(x,y, params["test_size"])
    x_val,y_val,x,y = val_split(x,y, params["val_size"])



model = make_model(x, y, w = params['pretrain'])
H, score, model = train_model(model,x,y,x_val,y_val,x_test,y_test, params["epochs"], params["Batch_size"])

results = {'score':score,"acc_epoch":H.history['acc'],"val_acc_epoch":H.history['val_acc'],"loss_epoch":H.history['loss'],"vall_loss_epoch":H.history['val_loss']}

doc(params,results,H)

#save model to JSON
model_json = model.to_json()
with open(f"{model_path}{params['epochs']}_{file_path[3:]}.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights(f"{model_path}{params['epochs']}_{file_path[3:]}_Weights.h5")
print("Saved model to disk")


### KaggleDR ###

# import_kaggleDR(path, img_size_x, img_size_y, norm, color = False, limit = None)
# x,y 