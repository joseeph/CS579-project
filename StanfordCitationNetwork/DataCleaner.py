from ArxivCrawler.ArxivCrawlerDriver import ArxivCrawlerDriver
from Framework import UtilFuncs
from Framework.CrawlerRunner import CrawlerRunner
from StanfordCitationNetwork.ArxivCitationPaperCrawler import ArxivCitationPaperCrawler
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.HepThAbstractFile import HepThAbstractFile
from StanfordCitationNetwork.HepThCitationFile import HepThCitationFile
from StanfordCitationNetwork.HepThDateFile import HepThDateFile
import StanfordCitationNetwork.CitationUtils as CitationUtils
import os
class DataCleaner:
    def __init__(self) -> None:
        self.CitationPath = ""
        self.DatePath = ""
        self.AbstractParentDir = ""
        pass


    def SetCitationPath(self, path):
        self.CitationPath = path
    
    def SetDatePath(self, path):
        self.DatePath = path

    def SetAbstractParentDir(self, parent_dir):
        self.AbstractParentDir = parent_dir

    def BuildAbstractFilePath(self, id, dt):
        abs_filepath = self.AbstractParentDir + "/" + str(dt.year) + "/" + str(id) + ".abs"
        return abs_filepath
    
    def DoClean(self, output_path):
        date_file = HepThDateFile()
        date_file.Load(self.DatePath)
        citation_file = HepThCitationFile()
        citation_file.Load(self.CitationPath)
        data_container = NodeContainer()

        crawl_paperids = self.__DoClean_Step1(data_container, date_file )
        UtilFuncs.PickleWrite(data_container, output_path)
        self.__DoClean_Step2(data_container, crawl_paperids)
        UtilFuncs.PickleWrite(data_container, output_path)
        self.__DoClean_Step3(data_container, citation_file)
        UtilFuncs.PickleWrite(data_container, output_path)

    
    def __DoClean_Step1(self, data_container:NodeContainer, date_file: HepThDateFile):
        '''
        step 1: create all the paper nodes
        '''
        crawl_paperids = []

        for paper_id, date_str in date_file.PaperDateMap.items():
            # regulate the paper id
            paper_id = CitationUtils.RegulatePaperID(paper_id)
            dt = CitationUtils.DateStrToDate(date_str)

            paper_node = CitationPaperNode()
            paper_node.SetID(paper_id)
            paper_node.SetDate(dt)
            # remove duplicate nodes, use the latest node.
            data_container.RemoveNode(paper_node.GetUID())
            data_container.AddNode(paper_node)
            
            file_path = self.BuildAbstractFilePath(paper_id, dt)
            # check if the file path exist, if it doesn't exist, I need to crawl from arxiv
            if not os.path.exists(file_path):
                crawl_paperid =  str(paper_id)
                if not (crawl_paperid in crawl_paperids):
                    crawl_paperids.append(crawl_paperid)
            else:
                # get tile and authors from abstract file for this paper
                abstract_file = HepThAbstractFile()
                abstract_file.Load(file_path)
                paper_node.SetName(abstract_file.Title)
                for author_name in abstract_file.Authors:
                    paper_node.AddAuthor(author_name)

        return crawl_paperids
    
    

    def __DoClean_Step2(self, data_container :NodeContainer, crawl_paperids):
        '''
        step 2: crawl from arxiv, fill the data
        '''
        driver = ArxivCrawlerDriver()
        runner = CrawlerRunner(driver, "", data_container)
        runner.SetMaxNode(-1)
        for paper_id in crawl_paperids:
            crawler = ArxivCitationPaperCrawler()
            crawler.SetPaperID(paper_id)
            runner.AddDataNodeCrawler(crawler)
        runner.BeginCrawl()

    def __DoClean_Step3(self, data_container: NodeContainer, citation_file :HepThCitationFile):
        '''
        fill the citation information
        '''
        for from_nodeid in citation_file.EdgeMap:
            #from_uid = CitationUtils.BuildCitationPaperUID(from_nodeid)
            node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", from_nodeid)
            if node == None:
                continue
            to_nodeidlist = citation_file.EdgeMap[from_nodeid]
            for to_nodeid in to_nodeidlist:
                node.AddReference(to_nodeid)

    def __DoClean_Step4(self, data_container :NodeContainer, citation_file :HepThCitationFile):
        '''
        1. many edges in the citation file are not included
        2. many information are not included
        
        firstly I need to add new nodes from citation_file
        '''
        tocrawl_paperids = []
        for from_node in citation_file.EdgeMap:
            node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", from_node)
            if node == None:
                tocrawl_paperids.append(from_node)
        
        # now I have node names to crawl


        
        pass

    def DocleanForStep3(self, data_path):
        data_container = UtilFuncs.PickleRead(data_path)
        citation_file = HepThCitationFile()
        citation_file.Load(self.CitationPath)
        self.__DoClean_Step3(data_container, citation_file)
        return data_container


    