from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
import networkx as nx
import pandas as pd

from Framework import UtilFuncs




class CoauthorNetworkBuilder:
    def __init__(self) -> None:
        pass

    def BuildCoauthorDataFrame(self, data_container :NodeContainer, output_path):
        paper_map = data_container.GetAllNodesByType("CitationPaperNode")

        graph_dict = {}

        from_year = 1993
        to_year = 2003
        # from 1993 to 2003
        for cur_year in range(from_year, to_year + 1):
            coauthor_graph = nx.DiGraph()
            paper_name_dict = {}
            paper_node :CitationPaperNode = None
            for paper_id in paper_map:
                # add this paper's ID
                paper_node = paper_map[paper_id]
                if paper_node.Dt.year <= cur_year:
                    first_author = paper_node.AuthorNames[0]
                    coauthor_graph.add_node(first_author)
                    if first_author in paper_name_dict:
                        paper_name_dict[first_author]['paper'].append(paper_node.Name)
                    else:
                        paper_name_dict[first_author] = {'paper': [paper_node.Name], 'author':'first'}
                    if len(paper_node.AuthorNames)>1:
                        for coauthor_name in paper_node.AuthorNames[1:]:
                            # citation_paper :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", citation_paperid)
                            # if citation_paper.Dt.year <= cur_year:
                            coauthor_graph.add_node(coauthor_name)
                            coauthor_graph.add_edge(coauthor_name, first_author)
                            if coauthor_name in paper_name_dict:
                                paper_name_dict[coauthor_name]['paper'].append(paper_node.Name)
                            else:
                                paper_name_dict[coauthor_name] = {'paper': [paper_node.Name], 'author':'second'}
            nx.set_node_attributes(coauthor_graph, paper_name_dict)
            graph_dict[cur_year] = coauthor_graph
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
        paper_name_list = []
        authorship= []
        betweenness_centrality_list = []
        for cur_year in range(from_year, to_year + 1):
            cur_graph :nx.DiGraph = graph_dict[cur_year]
            in_degree_cen = in_degree_centrality_map[cur_year]
            out_degree_cen = out_degree_centrality_map[cur_year]

            for node_id, attr in cur_graph.nodes(data=True):
                # node id
                nodeid_list.append(node_id)
                year_list.append(cur_year)
                in_degree_centrality = in_degree_cen[node_id]
                out_degree_centrality = out_degree_cen[node_id]
                in_degreecen_list.append(in_degree_centrality)
                out_degreecen_list.append(out_degree_centrality)
                print(attr)
                paper_name_list.append(attr['paper'])
                authorship.append(attr['author'])
            
        df['NodeID'] = nodeid_list
        df['Year'] = year_list
        df['InDegreeCentrality'] = in_degreecen_list
        df['OutDegreeCentrality'] = out_degreecen_list
        df['paper'] = paper_name_list
        df['authorship'] = authorship
        
        UtilFuncs.PickleWrite(df, output_path)
        

        #pd.DataFrame()
        pass 