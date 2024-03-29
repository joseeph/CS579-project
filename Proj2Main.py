from CitationNetwork.CitationDataCleaner import CitationDataCleaner

def Test():
    json_str = '{root:[{"id":1}, {"id":2}]}'
    pass

if __name__ == "__main__":
    cleaner = CitationDataCleaner()
    src_path = "./Data/dblp.v12.json"
    dst_path = "./Data/CitationClean.xml"
    cleaner.CleanData(src_path, dst_path)

    pass