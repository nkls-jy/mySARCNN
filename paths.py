import os 

train_dir = "/home/niklas/Documents/SLC_train_tiles"
#train_dir = "/home/niklas/Documents/GRD_train_tiles"
#train_dir = "/home/niklas/Documents/traindata_big_cleaned"
valid_dir = ""
test_dir = "/home/niklas/Documents/dataForDL_Filtering/SLC_post"
#test_dir = "/home/niklas/Documents/SLC_test_tiles"
#test_dir = "/home/niklas/Documents/GRD_test_tiles"

# create testfiles
list_testfiles = [os.path.join(test_dir, f) for f in os.listdir(test_dir) if os.path.isfile(os.path.join(test_dir, f)) and f.endswith(".tif")]

