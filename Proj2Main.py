from CitationNetwork.CitationDataCleaner import CitationDataCleaner
import CitationNetwork.CitationUtils as CitationUtils
import pickle
def Test():
    json_str = '{root:[{"id":1}, {"id":2}]}'
    pass

def Main():
    cleaner = CitationDataCleaner()
    src_path = "./Data/dblp.v12.json"
    dst_path = "./Data/CitationClean.dat"
    cleaner.CleanData(src_path, dst_path)

def Main2():
    dst_path = "./Data/CitationClean.dat"
    data_container = CitationUtils.PickleRead(dst_path)
    pass

if __name__ == "__main__":
    Main()

    
    pass