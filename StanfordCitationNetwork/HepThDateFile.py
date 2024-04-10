import Framework.UtilFuncs as UtilFuncs
import StanfordCitationNetwork.CitationUtils as CitationUtils

class HepThDateFile:
    def __init__(self) -> None:
        self.PaperDateMap = {}
        

    def Load(self, path):
        f = open(path, 'r')
        lines = f.readlines()
        cur_line :str = ""
        for cur_line in lines:
            cur_line = cur_line.strip()
            if cur_line[0] == '#':
                #comments
                continue
            split_parts = cur_line.split('\t')
            paper_id = split_parts[0]
            paper_id = CitationUtils.RegulatePaperID(paper_id)
            date_str = split_parts[1]
            dt = CitationUtils.DateStrToDate(date_str)
            self.PaperDateMap[paper_id] = dt

        f.close()

    def ContainsPaper(self, paper_id):
        return paper_id in self.PaperDateMap
    
    def GetPaperDate(self, paper_id):
        dt = self.PaperDateMap.get(paper_id)
        return dt
        
    