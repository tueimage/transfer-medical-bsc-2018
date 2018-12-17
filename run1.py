from RunTarget import run_target
import sys
arg = sys.argv[1]

model = ["imagenet","kaggleDR"]
data = ['two','three','two_combined']
style = ['FT', 'SVM']

x = int(arg[0])
y = int(arg[1])
z = int(arg[2])
r = int(arg[3])

params = {"Data":'ISIC',
        "data_name":data[y],
        "style":style[z],
        "model":model[x],
        "file_path":r"C:\ISIC",
        "pickle_path":r"C:\pickles\melanoom_color_NotEqual_",
        "model_path":r"C:\models\Epochs_5_kaggleDR.json",
        "RandomSeed":r,
        "doc_path":r"C:\Users\Flori\Documents\GitHub\t",
        'img_size_x':224,
        'img_size_y':224,
        'norm':False,
        'color':True, 
        'pretrain':None, 
        "equal_data":False, 
        "shuffle":True, 
        "epochs":50 , 
        "val_size":100,
        "test_size":200, 
        "Batch_size":16
        }

#"pickle_path":r"C:\pickles\save_melanoom_color_",

run_target(params)