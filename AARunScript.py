import pickle
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import tensorflow as tf
from AADatasets import import_mnist, import_dogcat, import_melanoom,import_kaggleDR, pre_processing, make_pre_train_classes, get_data, more_data, equal_data_run, val_split
from AAPreTrain import make_model,train_model, config_desktop
from AATransferLearn import get_feature_vector, preform_svm, auc_svm
from AAlogic import test_script, menegola_plane
from LabnotesDoc import doc


# params = {"Data":'kaggleDR','img_size_x':224,'img_size_y':224,'norm':False,'color':True, 'pretrain':None, "equal_data":False, "shuffle": True, "epochs": 50 , "val_size":3000,"test_size":5000, "Batch_size": 32} #epochs val X1000 bacth to 32
# file_path = r"C:\kaggleDR"
# pickle_path = r"C:\pickles\kaggleDR"
# model_path = r"C:\models\Epochs_"
# doc_path =  r"C:\Users\Flori\Documents\GitHub\t"
config_desktop()
# # params = { "Data":'cat_dogmini','img_size_x':224,'img_size_y':224,'norm':False,'color':True, 'pretrain':None, "equal_data":False, "shuffle": True, "epochs": 2 , "val_size":50,"test_size":50, "Batch_size": 1}
# # ## intergreren van data naam en path name   

# # file_path = r"C:\Users\s147057\Documents\BEP\pet set"
# # pickle_path = r"C:\Users\s147057\Documents\BEP\Pickle"
# # model_path = r"C:\Users\s147057\Documents\BEP\models"
# # doc_path =  r"C:\Users\s147057\Documents\GitHub\t"

# # laptop = False


# try:
#     print("Try to import pickle")
#     try:
#     	zippy = pickle.load(open( f"{pickle_path}.p", "rb" ))
#     except:
#     	zippy = pickle.load(open( f"{pickle_path}_part1.p", "rb" ))
#     	zippy2 = pickle.load(open( f"{pickle_path}_part2.p", "rb" ))
#     	zippy.append(zippy2)

#     print("succeed to import pickle")
#     zippy = list(zippy)
#     random.shuffle(zippy)
#     x,y = zip(*zippy)
#     x = np.array(x)
#     y = np.array(y)
#     x_test,y_test,x,y = val_split(x,y, params["test_size"])
#     x_val,y_val,x,y = val_split(x,y, params["val_size"])

# except:
#     print("Failed to import pickle")    
#     x,y = import_kaggleDR(file_path, params['img_size_x'],params['img_size_y'], norm = params["norm"], color = params["color"])
#     # x,y = import_dogcat(file_path,params['img_size_x'],params['img_size_y'], norm = params["norm"], color = params["color"])
#     if params["equal_data"] == True:
#         x,y = equal_data_run(y,x)

    
    
#     x2 = list(x)
#     y2 = list(y)
#     zip_melanoom1 = zip(x2[int(len(y)/2):],y2[int(len(y)/2):])
#     zip_melanoom2 = zip(x2[:int(len(y)/2)],y2[:int(len(y)/2)])
#     pickle.dump( zip_melanoom1, open( f"{pickle_path}_part1.p", "wb" ))
#     pickle.dump( zip_melanoom2, open( f"{pickle_path}_part2.p", "wb" ))
#     zip_melanoom = zip(x2,y2)

#     zippy = list(zip_melanoom)
#     random.shuffle(zippy)
#     x,y = zip(*zippy)
#     x = np.array(x)
#     y = np.array(y)
#     x_test,y_test,x,y = val_split(x,y, params["test_size"])
#     x_val,y_val,x,y = val_split(x,y, params["val_size"])
# print(y)
# # if laptop == True:
# #     x = x[:20]
# #     y = y[:20]


# model = make_model(x, y, w = params['pretrain'])

# if params['pretrain'] == None:
#     H, score, model = train_model(model,x,y,x_val,y_val,x_test,y_test, params["epochs"], params["Batch_size"])

# results = {'score':score,"acc_epoch":H.history['acc'],"val_acc_epoch":H.history['val_acc'],"loss_epoch":H.history['loss'],"vall_loss_epoch":H.history['val_loss']}

# doc(params,results,H,doc_path)

# #save model to JSON
# model_json = model.to_json()
# with open(f"{model_path}{params['epochs']}_{params['Data']}.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# model.save_weights(f"{model_path}{params['epochs']}_{params['Data']}_Weights.h5")
# print("Saved model to disk")


### KaggleDR ###

# import_kaggleDR(path, img_size_x, img_size_y, norm, color = False, limit = None)
# x,y 


#Load model
with open(r"C:\models\Epochs_50_kaggleDR.json", 'r') as json_file:
    loaded_model_json = json_file.read()
json_file.close()
loaded_model = tf.keras.models.model_from_json(loaded_model_json)
#Load weights into new model
loaded_model.load_weights(r"C:\models\Epochs_50_kaggleDR_Weights.h5")
print("Loaded model from disk")



params = {"Data":'ISIC','img_size_x':224,'img_size_y':224,'norm':False,'color':True, 'pretrain':None, "equal_data":False, "shuffle": True, "epochs": 50 , "val_size":300,"test_size":400, "Batch_size": 16}
file_path = r"C:\ISIC"
pickle_path = r"C:\pickles\save_melanoom_color_"
model_path = r"C:\models\Epochs_"
doc_path =  r"C:\Users\Flori\Documents\GitHub\t"

count=0
super_script = True
if super_script == True:
    for style in ["FT"]:
        for data_name in ['three']: #'two',,'two_combined']:  "imagenet", 'two' ,,'two_combined'
            try:
                print("Try to import pickle")
                zippy = pickle.load(open( f"{pickle_path}{data_name}.p", "rb" ))
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

            for method in ["kaggleDR"]: #"imagenet",
                config_desktop()
                count +=1
                if count ==0: ## if you want to cancel numbers
                    continue
                if method == "imagenet":
                    model = make_model(x, y, w = 'imagenet')
                elif method == "kaggleDR":
                    model = loaded_model
                    for layer in model.layers[:-5]:
                        layer.trainable = False
                    fine_tune = tf.keras.layers.Dense(y.shape[1], activation='sigmoid')(model.output)
                    model  = tf.keras.models.Model(inputs=model.input, outputs=fine_tune)
                    opt = tf.keras.optimizers.SGD(lr=0.001, momentum=0.01, decay=0.0, nesterov=True)
                    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

                if style == 'FT':
                    H, score, model = train_model(model,x,y,x_val,y_val,x_test,y_test, params["epochs"], params["Batch_size"])
                    results = {'score':score,"acc_epoch":H.history['acc'],"val_acc_epoch":H.history['val_acc'],"loss_epoch":H.history['loss'],"vall_loss_epoch":H.history['val_loss'],'data_name':data_name,'method':method,'style':style}

                elif style =='SVM':
                    predictions = get_feature_vector(model, x, layer = 'fc2')
                    predictions_test = get_feature_vector(model, x_test, layer = 'fc2')
                    score = auc_svm(predictions,y,predictions_test,y_test, plot = False)
                    results = {'score':score,'data_name':data_name,'method':method,'style':style}
                    H=None
                    print(params)
                    print(results)
                    print(H)
                doc(params,results,H,doc_path)
                print(method)
                print(style)
                print(data_name)




            
