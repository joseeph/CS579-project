from StanfordCitationNetwork.DataCleaner import DataCleaner


def NewCleanStep1():
    cleaner = DataCleaner()
    citationfile_path = "./Data/cit-HepTh.txt"
    datefile_path = "./Data/cit-HepTh-dates.txt"
    abstract_parentdir = "./Data/cit-HepTh-abstracts"
    data_path = "./Data/CitationCleaned.dat"
    output_path = "./Data/CitationCleaned.dat"
    cleaner.SetCitationPath(citationfile_path)
    cleaner.SetDatePath(datefile_path)
    cleaner.SetAbstractParentDir(abstract_parentdir)
    cleaner.DoCleanStep1(output_path)

def NewCleanStep2():
    cleaner = DataCleaner()
    citationfile_path = "./Data/cit-HepTh.txt"
    datefile_path = "./Data/cit-HepTh-dates.txt"
    abstract_parentdir = "./Data/cit-HepTh-abstracts"
    data_path = "./Data/CitationCleaned.dat"
    output_path = "./Data/CitationCleaned.dat"
    cleaner.SetCitationPath(citationfile_path)
    cleaner.SetDatePath(datefile_path)
    cleaner.SetAbstractParentDir(abstract_parentdir)
    cleaner.DoCleanStep2(data_path, output_path)


if __name__ == '__main__':
    # build CitationCleaned.dat, but some values are missing
    NewCleanStep1()
    # crawl from arxiv to fill the missing values
    NewCleanStep2()