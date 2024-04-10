from ArxivCrawler.ArxivCrawlerDriver import ArxivCrawlerDriver
from Framework.CrawlerRunner import CrawlerRunner
from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.ArxivCitationPaperCrawler import ArxivCitationPaperCrawler
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
from StanfordCitationNetwork.HepThAbstractFile import HepThAbstractFile
from StanfordCitationNetwork.HepThCitationFile import HepThCitationFile
from StanfordCitationNetwork.HepThDateFile import HepThDateFile
from Framework import UtilFuncs
import os

class DataNewCleaner:
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
    
    

    def DoCleanStep1(self, output_path):
        
        date_file = HepThDateFile()
        date_file.Load(self.DatePath)
        citation_file = HepThCitationFile()
        citation_file.Load(self.CitationPath)
        data_container = NodeContainer()
        self.__DoClean_Step1(data_container, citation_file, date_file, output_path)

    def DoCleanStep2(self, data_path, output_path):
        citation_file = HepThCitationFile()
        citation_file.Load(self.CitationPath)
        data_container :NodeContainer = UtilFuncs.PickleRead(data_path)
        self.__Doclean_Step2(data_container, citation_file, output_path)

    def __DoClean_Step1(self, data_container :NodeContainer, citation_file :HepThCitationFile, date_file :HepThDateFile, output_path ):
        
        from_paperids = []
        # add 'from' nodes, we have reference information for these nodes
        for from_paperid in citation_file.EdgeMap:
            from_paperids.append(from_paperid)

            to_paperids = citation_file.EdgeMap[from_paperid]
            paper_node = CitationPaperNode()
            paper_node.SetID(from_paperid)
            # fill the paper node if possible
            self.ProcessPaperID(paper_node, date_file)
            data_container.AddNode(paper_node)
            # citations
            for to_paperid in to_paperids:
                paper_node.AddReference(to_paperid)
        
        # add 'to' nodes, we don't have reference information for these nodes
        data_map = data_container.GetAllNodesByType("CitationPaperNode")
        for frompaper_id in from_paperids:
            cur_papernode :CitationPaperNode = data_map[frompaper_id]
            refid_list = cur_papernode.GetReferences()
            for ref_id in refid_list:
                ref_node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", ref_id)
                if ref_node == None:
                    ref_node = CitationPaperNode()
                    ref_node.SetID(ref_id)
                    # fill the paper node if possible
                    self.ProcessPaperID(ref_node, date_file)
                    data_container.AddNode(ref_node)
        UtilFuncs.PickleWrite(data_container, output_path)


    def __Doclean_Step2(self, data_container :NodeContainer, citation_file :HepThCitationFile, output_path):
        crawlfrom_paperids = []
        crawlto_paperids = []
        for from_paperid in citation_file.EdgeMap:
            from_node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", from_paperid)
            # we don't have information of this paper, then crawl it
            if len(from_node.AuthorNames) == 0:
                crawlfrom_paperids.append(from_paperid)
            to_ids = from_node.GetReferences()
            for to_id in to_ids:
                to_node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", to_id)
                if len(to_node.AuthorNames) == 0:
                    if to_id not in crawlto_paperids:
                        crawlto_paperids.append(to_id)
        # concat to arrays
        tocrawl_paperids = [] + crawlfrom_paperids
        for to_id in crawlto_paperids:
            if to_id not in tocrawl_paperids:
                tocrawl_paperids.append(to_id)
        # now we have paper ids to crawl
        driver = ArxivCrawlerDriver()
        runner = CrawlerRunner(driver, output_path, data_container)
        runner.SetMaxNode(-1)
        runner.SetSaveOnFinish(True)
        runner.SetSaveFrequency(50)
        for paper_id in tocrawl_paperids:
            crawler = ArxivCitationPaperCrawler()
            crawler.SetCrawlOrderByPhFirst(False)
            crawler.SetPaperID(paper_id)
            runner.AddDataNodeCrawler(crawler)
        runner.BeginCrawl()
        

            
            
    def ProcessPaperID(self, paper_node :CitationPaperNode, date_file :HepThDateFile):
        paper_id = paper_node.GetUID()
        dt = date_file.GetPaperDate(paper_id)
        if dt != None:
            abs_filepath = self.BuildAbstractFilePath(paper_id, dt)
            if os.path.exists(abs_filepath):
                abs_file = HepThAbstractFile()
                abs_file.Load(abs_filepath)
                paper_node.SetDate(dt)
                paper_node.SetName(abs_file.Title)
                for author_name in abs_file.Authors:
                    paper_node.AddAuthor(author_name)
                return True
        return False
            


    def BuildAbstractFilePath(self, id, dt):
        abs_filepath = self.AbstractParentDir + "/" + str(dt.year) + "/" + str(id) + ".abs"
        return abs_filepath