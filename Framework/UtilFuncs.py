import pickle

def PickleWrite(obj, dst_path):
    print("save:" + dst_path)
    file = open(dst_path, 'wb')
    pickle.dump(obj, file)
    file.close()

def PickleRead(dst_path):
    print("load:" + dst_path)
    file = open(dst_path, 'rb')
    obj = pickle.load(file)
    file.close()
    return obj