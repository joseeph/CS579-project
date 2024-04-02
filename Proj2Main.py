from CitationNetwork.CitationAuthorNode import CitationAuthorNode
from CitationNetwork.CitationDataCleaner import CitationDataCleaner
from CitationNetwork.CitationPaperNode import CitationPaperNode
import CitationNetwork.CitationUtils as CitationUtils
from Framework.NodeContainer import NodeContainer
import pickle
def Test():
    json_str = '{root:[{"id":1}, {"id":2}]}'
    pass

def Main():
    cleaner = CitationDataCleaner()
    src_path = "./Data/dblp.v12.json"
    dst_path = "./Data/CitationClean.dat"
    cleaner.CleanData(src_path, dst_path)

def Main2():
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
    

    pass

if __name__ == "__main__":
    Main2()

    
    pass