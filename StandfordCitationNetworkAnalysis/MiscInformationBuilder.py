from Framework import UtilFuncs
from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
import pandas as pd

class MiscInformationBuilder:
    def __init__(self) -> None:
        pass

    def BuildMiscInfoDF(self, data_container :NodeContainer, output_path):
        from_year = 1992
        to_year = 2003
        all_nodemap = data_container.GetAllNodesByType("CitationPaperNode")
        nodeid_list = []
        year_list = []
        # 距离发表距今几年
        yearstonow_list = []
        # 引用了其他文章的数量
        referencenum_list = []
        # 作者数
        authornum_list = []
        for year in range(from_year, to_year + 1):
            
            for node_id in all_nodemap:
                cur_node :CitationPaperNode = all_nodemap[node_id]
                if cur_node.Dt.year <= year:
                    nodeid_list.append(node_id)
                    year_list.append(year)
                    author_num = len(cur_node.AuthorNames)
                    authornum_list.append(author_num)
                    ref_num = len(cur_node.ReferenceIDs)
                    referencenum_list.append(ref_num)
                    yearstonow = year - cur_node.Dt.year
                    yearstonow_list.append(yearstonow)
        df = pd.DataFrame()
        df['NodeID'] = nodeid_list
        df['Year'] = year_list
        df['YearsToNow'] = yearstonow_list
        df['ReferenceNum'] = referencenum_list
        df['AuthorNum'] = authornum_list  

        UtilFuncs.PickleWrite(df, output_path)
        