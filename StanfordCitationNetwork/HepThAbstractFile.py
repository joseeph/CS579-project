class HepThAbstractFile:
    def __init__(self) -> None:
        self.Title = ""
        self.Authors = []
        pass

    def IsAuthorLine(self, line):
        index = line.find("Author")
        return index == 0

    def IsTitleLine(self, line):
        index = line.find("Title")
        return index == 0
        

    def ProcessForAuthor(self, line:str):
        authors = []
        idx = line.find(":")
        author_part = line[idx + 1:]
        splited_authors = author_part.split(",")
        if len(splited_authors) == 1:
            tosplit_authors = splited_authors[0]
            split_by_and_authors = tosplit_authors.split(' and ')
            cur_author :str = ""
            for cur_author in split_by_and_authors:
                cur_author = cur_author.strip()
                authors.append(cur_author)
        else:
            cur_author :str = ""
            for cur_author in splited_authors:
                cur_author = cur_author.strip()
                authors.append(cur_author)
        return authors
        
        
    def ProcessForTitle(self, line):
        idx = line.find(":")
        title_part = line[idx + 1 :]
        title = title_part.strip()
        return title
        
        
    def Load(self, path):
        f = open(path, 'r')
        lines = f.readlines()
        cur_line :str = ""
        found_author = False
        found_title = False
        for cur_line in lines:
            cur_line = cur_line.strip()
            if self.IsAuthorLine(cur_line):
                self.Authors = self.ProcessForAuthor(cur_line)
                found_author = True
            
            if self.IsTitleLine(cur_line):
                self.Title = self.ProcessForTitle(cur_line)
                found_title = True
                
            if found_author and found_title:
                break
        f.close()
            