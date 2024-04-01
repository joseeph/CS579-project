import pickle

def BuildCitationAuthorNodeUID(id):
    return "CitationAuthor_" + str(id)

def BuildCitationPaperUID(id):
    return "CitationPaper_" + str(id)


def PickleWrite(obj, dst_path):
    file = open(dst_path, 'wb')
    pickle.dump(obj, file)
    file.close()

def PickleRead(dst_path):
    file = open(dst_path, 'rb')
    obj = pickle.load(file)
    file.close()
    return obj