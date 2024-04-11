

from ArxivCrawler.ArxivCrawlerDriver import ArxivCrawlerDriver
from Framework import UtilFuncs
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
import StanfordCitationNetwork.CitationUtils as CitationUtils
from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.DataCleaner import DataCleaner

def CrawlerTest():
    driver = ArxivCrawlerDriver()
    #result = driver.Get("query_idlist", "hep-ph/119902209")
    #result = driver.Get("query_idlist", "hep-th/9203001")
    #result = driver.Get("query_idlist", "9210235")
    result = driver.Get("query_idlist", "hep-ph/9210235")

    #result = driver.Get("query_papername", "9210235")
    
    paper_infolist = []
    for paper_info in result:
        paper_infolist.append(paper_info)
    return paper_infolist

def LoadData():
    data_container :NodeContainer = UtilFuncs.PickleRead("./Data/CitationCleaned.dat")
    SummaryDataContainer(data_container)
    

def SummaryDataContainer(data_container):
    paper_nodemap = data_container.GetAllNodesByType("CitationPaperNode")
    total_num = len(paper_nodemap)
    hasref_num = 0
    valid_num = 0
    for key in paper_nodemap:
        paper_node :CitationPaperNode = paper_nodemap[key]
        ref_num = len(paper_node.ReferenceIDs)
        if ref_num > 0:
            hasref_num += 1
        author_num = len(paper_node.AuthorNames)
        if author_num > 0:
            valid_num += 1
    print( "hasref_num / total_num:"+ str(hasref_num) + "/" + str(total_num))
    print( "valid_num / total_num:" + str(valid_num) + "/" + str(total_num))


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

if __name__ == "__main__":
    
    LoadData()
    
    pass