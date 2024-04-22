from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
import networkx as nx
import pandas as pd

from Framework import UtilFuncs


class CitationNetworkBuilder:
    def __init__(self) -> None:
        pass

    def BuildCitationDataFrame(self, data_container :NodeContainer, output_path):
        paper_map = data_container.GetAllNodesByType("CitationPaperNode")

        graph_dict = {}

        from_year = 1993
        to_year = 2003
        # from 1993 to 2003
        for cur_year in range(from_year, to_year + 1):
            citation_graph = nx.DiGraph()

            paper_node :CitationPaperNode = None
            for paper_id in paper_map:
                # add this paper's ID
                paper_node = paper_map[paper_id]
                if paper_node.Dt.year <= cur_year:
                    citation_graph.add_node(paper_node.ID)
                    for citation_paperid in paper_node.ReferenceIDs:
                        citation_paper :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", citation_paperid)
                        if citation_paper.Dt.year <= cur_year:
                            citation_graph.add_node(citation_paperid)
                            citation_graph.add_edge(paper_node.ID, citation_paperid)
            graph_dict[cur_year] = citation_graph
        # degree centrality
        in_degree_centrality_map = {}
        out_degree_centrality_map = {}
        for cur_year in range(from_year, to_year + 1):
            graph = graph_dict[cur_year]
            in_degree_map = nx.in_degree_centrality(graph)
            out_degree_map = nx.out_degree_centrality(graph)
            in_degree_centrality_map[cur_year] = in_degree_map
            out_degree_centrality_map[cur_year] = out_degree_map

        # betweenness centrality
        
        # betweenness_centrality_map = {}
        # for cur_year in range(from_year, to_year + 1):
        #     graph = graph_dict[cur_year]
        #     betweenness_map = nx.betweenness_centrality(graph)
        #     betweenness_centrality_map[cur_year] = betweenness_map
        

        df = pd.DataFrame()
        nodeid_list = []
        year_list = []
        in_degreecen_list = []
        out_degreecen_list = []
        betweenness_centrality_list = []
        for cur_year in range(from_year, to_year + 1):
            cur_graph :nx.DiGraph = graph_dict[cur_year]
            in_degree_cen = in_degree_centrality_map[cur_year]
            out_degree_cen = out_degree_centrality_map[cur_year]

            for node_id in cur_graph.nodes:
                # node id
                nodeid_list.append(node_id)
                year_list.append(cur_year)
                in_degree_centrality = in_degree_cen[node_id]
                out_degree_centrality = out_degree_cen[node_id]
                in_degreecen_list.append(in_degree_centrality)
                out_degreecen_list.append(out_degree_centrality)
                
            
        df['NodeID'] = nodeid_list
        df['Year'] = year_list
        df['InDegreeCentrality'] = in_degreecen_list
        df['OutDegreeCentrality'] = out_degreecen_list
        
        UtilFuncs.PickleWrite(df, output_path)
        

        #pd.DataFrame()
        pass


        
        

        

        
