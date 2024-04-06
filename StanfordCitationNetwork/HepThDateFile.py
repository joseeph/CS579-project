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
            date_str = split_parts[1]

            self.PaperDateMap[paper_id] = date_str
        f.close()
        