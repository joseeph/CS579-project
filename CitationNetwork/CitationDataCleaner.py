import json_stream
class CitationDataCleaner:
    def __init__(self) -> None:
        pass

    def CleanData(self, src_path, dst_path):
        f = open(src_path, 'r', encoding="utf-8")
        data = json_stream.load(f)
        #root = data['root']
        for dat in data:
            id = dat['id']
            authors = dat['authors']
            title = dat['title']
            year = dat['year']
            doc_type = dat['doc_type']

        pass