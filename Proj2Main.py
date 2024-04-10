

from ArxivCrawler.ArxivCrawlerDriver import ArxivCrawlerDriver
from Framework import UtilFuncs
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
import StanfordCitationNetwork.CitationUtils as CitationUtils
from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.DataNewCleaner import DataNewCleaner
from StanfordCitationNetwork.DataCleaner import DataCleaner
'''
def Test():
    json_str = '{root:[{"id":1}, {"id":2}]}'
    pass

def Main():
    cleaner = CitationDataCleaner()
    src_path = "./Data/dblp.v12.json"
    dst_path = "./Data/CitationClean.dat"
    cleaner.CleanData(src_path, dst_path)

def Main2():
    cleaner = CitationDataCleaner()
    src_path = "./Data/CitationClean.dat"
    dst_path = "./Data/CitationClean2.dat"
    cleaner.CleanStep2(src_path, dst_path)

def MainTest():
    dst_path = "./Data/CitationClean.dat"
    data_container :NodeContainer = CitationUtils.PickleRead(dst_path)

    node_map = data_container.GetAllNodesByType("CitationPaperNode")
    for key in node_map:
        node :CitationPaperNode = node_map[key]
        for ref_id in node.RefIDs:
            papaer_nodeid = CitationUtils.BuildCitationPaperUID(ref_id)
            cit_node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", papaer_nodeid)
            if cit_node != None:
                print(cit_node.PaperName)

        for author_id in node.AuthorIDs:
            author_nodeid = CitationUtils.BuildCitationAuthorNodeUID(author_id)
            author_node :CitationAuthorNode = data_container.FindNodeWithType("CitationAuthorNode", author_nodeid)
            if author_node != None:
                print(author_node.AuthorName)
    
'''

def CleanMain():
    cleaner = DataCleaner()
    citationfile_path = "./Data/cit-HepTh.txt"
    datefile_path = "./Data/cit-HepTh-dates.txt"
    abstract_parentdir = "./Data/cit-HepTh-abstracts"
    output_path = "./Data/CitationCleaned.dat"
    cleaner.SetCitationPath(citationfile_path)
    cleaner.SetDatePath(datefile_path)
    cleaner.SetAbstractParentDir(abstract_parentdir)
    cleaner.DoClean(output_path)

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

def CleanStep3():
    cleaner = DataCleaner()
    citationfile_path = "./Data/cit-HepTh.txt"
    datefile_path = "./Data/cit-HepTh-dates.txt"
    abstract_parentdir = "./Data/cit-HepTh-abstracts"
    output_path = "./Data/CitationCleaned.dat"
    cleaner.SetCitationPath(citationfile_path)
    cleaner.SetDatePath(datefile_path)
    cleaner.SetAbstractParentDir(abstract_parentdir)
    data_container = cleaner.DocleanForStep3(output_path)
    UtilFuncs.PickleWrite(data_container, output_path)
    
def CleanStep4():
    cleaner = DataCleaner()
    citationfile_path = "./Data/cit-HepTh.txt"
    datefile_path = "./Data/cit-HepTh-dates.txt"
    abstract_parentdir = "./Data/cit-HepTh-abstracts"
    data_path = "./Data/CitationCleaned.dat"
    output_path = "./Data/CitationCleaned2.dat"
    cleaner.SetCitationPath(citationfile_path)
    cleaner.SetDatePath(datefile_path)
    cleaner.SetAbstractParentDir(abstract_parentdir)
    data_container = cleaner.DocleanForStep4(data_path, output_path)
    #UtilFuncs.PickleWrite(data_container, output_path)
    pass

def CleanStep5():
    cleaner = DataCleaner()
    citationfile_path = "./Data/cit-HepTh.txt"
    datefile_path = "./Data/cit-HepTh-dates.txt"
    abstract_parentdir = "./Data/cit-HepTh-abstracts"
    data_path = "./Data/CitationCleaned3.dat"
    output_path = "./Data/CitationCleaned3.dat"
    cleaner.SetCitationPath(citationfile_path)
    cleaner.SetDatePath(datefile_path)
    cleaner.SetAbstractParentDir(abstract_parentdir)
    data_container = cleaner.DocleanForStep5(data_path, output_path)


def NewCleanStep1():
    cleaner = DataNewCleaner()
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
    cleaner = DataNewCleaner()
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
    
    NewCleanStep2()
    
    pass