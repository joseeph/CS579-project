import StanfordCitationNetwork.CitationUtils as CitationUtils
class HepThCitationFile:
    def __init__(self) -> None:
        self.EdgeMap = {}
        pass

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
            from_nodeid = split_parts[0]
            to_nodeid = split_parts[1]
            from_nodeid = CitationUtils.RegulatePaperID(from_nodeid)
            to_nodeid = CitationUtils.RegulatePaperID(to_nodeid)
            

            edge_list = []
            if from_nodeid in self.EdgeMap:
                edge_list = self.EdgeMap[from_nodeid]
            else:
                self.EdgeMap[from_nodeid] = edge_list
            edge_list.append(to_nodeid)
        f.close()
        