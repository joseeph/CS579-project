from Framework.NodeContainer import NodeContainer
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode
import networkx as nx
import pandas as pd

from Framework import UtilFuncs
import numpy as np



class CoauthorNetworkBuilder:
    def __init__(self) -> None:
        pass

    def find_max_cen(self, group):
        max_cen = group['DegreeCentrality'].max()
        max_score = group['ClosenessCentrality'].max()
        selected_rows =  group[(group['DegreeCentrality'] == max_cen) & (group['ClosenessCentrality'] == max_score)]
        return selected_rows.assign(
        Degree_Centrality_sum=group['DegreeCentrality'].sum(),
        Closeness_Centrality_sum=group['ClosenessCentrality'].sum())

    def BuildCoauthorDataFrame(self, data_container :NodeContainer, output_path):
        paper_map = data_container.GetAllNodesByType("CitationPaperNode")

        graph_dict = {}

        from_year = 1992
        to_year = 2003
        # from 1993 to 2003
        for cur_year in range(from_year, to_year + 1):
            # the coauthor grpah is directional graph
            coauthor_graph = nx.DiGraph()
            paper_name_dict = {}
            paper_node :CitationPaperNode = None
            for paper_id in paper_map:
                # add this paper's ID
                paper_node = paper_map[paper_id]
                if paper_node.Dt.year <= cur_year:
                    # first author
                    first_author = paper_node.AuthorNames[0]
                    coauthor_graph.add_node(first_author)
                    if first_author in paper_name_dict:
                        paper_name_dict[first_author]['paper'].append(paper_node.Name)
                    else:
                        paper_name_dict[first_author] = {'paper': [paper_node.Name], 'author':'first', 'paper_id':paper_id}
                    if len(paper_node.AuthorNames)>1:
                        for coauthor_name in paper_node.AuthorNames[1:]:
                            # citation_paper :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", citation_paperid)
                            # if citation_paper.Dt.year <= cur_year:
                            coauthor_graph.add_node(coauthor_name)
                            coauthor_graph.add_edge(coauthor_name, first_author)
                            if coauthor_name in paper_name_dict:
                                paper_name_dict[coauthor_name]['paper'].append(paper_node.Name)
                            else:
                                paper_name_dict[coauthor_name] = {'paper': [paper_node.Name], 'author':'second', 'paper_id':paper_id}
            nx.set_node_attributes(coauthor_graph, paper_name_dict)
            graph_dict[cur_year] = coauthor_graph
        # degree centrality
        degree_centrality_map = {}
        closeness_centrality_map = {}
        for cur_year in range(from_year, to_year + 1):
            graph = graph_dict[cur_year]
            degree_map = nx.degree_centrality(graph)
            close_degree_map = nx.closeness_centrality(graph)
            degree_centrality_map[cur_year] = degree_map
            closeness_centrality_map[cur_year] = close_degree_map

        # betweenness centrality
        
        # betweenness_centrality_map = {}
        # for cur_year in range(from_year, to_year + 1):
        #     graph = graph_dict[cur_year]
        #     betweenness_map = nx.betweenness_centrality(graph)
        #     betweenness_centrality_map[cur_year] = betweenness_map
        

        df = pd.DataFrame()
        # nodeid_list = []
        paperid_list = []
        year_list = []
        max_degreecen_list = []
        max_closecen_list = []
        sum_degreecen_list = []
        sum_closecen_list = []

        # degreecen_list = []
        # closeness_list = []
        # paper_name_list = []
        # authorship= []

        paper_id_list = []
        for cur_year in range(from_year, to_year + 1):
            
            curyear_degreecen_map = degree_centrality_map[cur_year]
            curyear_closenesscen_map = closeness_centrality_map[cur_year]
            for paper_id in paper_map:
                paper_node :CitationPaperNode = paper_map[paper_id]
                paperid_list.append(paper_id)
                year_list.append(cur_year)
                # the degree centralities of all authors
                authors_degree_cenlist = []
                # the closeness centralities of all authors
                authors_closeness_cenlist = []
                for author_name in paper_node.AuthorNames:
                    # degree centrality
                    degree_centrality = curyear_degreecen_map[author_name]
                    # closeness centrality
                    closeness_centrality = curyear_closenesscen_map[author_name]
                    authors_degree_cenlist.append(degree_centrality)
                    authors_closeness_cenlist.append(closeness_centrality)
                # now find the max degree centrality 
                max_degree_cen = np.max(authors_degree_cenlist)
                # find the max closeness centrality
                max_close_cen = np.max(authors_closeness_cenlist)
                # sum the degree centrality
                sum_degree_cen = np.sum(authors_degree_cenlist)
                # sum the closenes c entrality
                sum_close_cen = np.sum(authors_closeness_cenlist)
                max_degreecen_list.append(max_degree_cen)
                max_closecen_list.append(max_close_cen)
                sum_degreecen_list.append(sum_degree_cen)
                sum_closecen_list.append(sum_close_cen)
                
                    




        # for cur_year in range(from_year, to_year + 1):
        #     cur_graph :nx.DiGraph = graph_dict[cur_year]
        #     degree_centrality_map = degree_centrality_map[cur_year]
        #     closeness_centrality_map = closeness_centrality_map[cur_year]
        #     for node_id, attr in cur_graph.nodes(data=True):
        #         # node id
        #         nodeid_list.append(node_id)
        #         year_list.append(cur_year)
        #         degree_centrality = degree_centrality_map[node_id]
        #         close_centrality = closeness_centrality_map[node_id]
        #         degreecen_list.append(degree_centrality)
        #         closeness_list.append(close_centrality)
        #         print(attr)
        #         paper_name_list.append(attr['paper'])
        #         authorship.append(attr['author'])
        #         paper_id_list.append(attr['paper_id'])
            
        df['NodeID'] = paper_id_list

        df['Year'] = year_list
        df['AuthorDegreeCentrality_Max'] = max_degreecen_list
        df['AuthorClosenessCentrality_Max'] = max_closecen_list
        df['AuthorDegreeCentrality_Sum'] = sum_degreecen_list
        df['AuthorClosenessCentrality_Sum'] = sum_closecen_list

        
        # grouped = df.groupby(['NodeID', 'Year'])
        # # Apply the function to each group
        # highest_df = grouped.apply(self.find_max_cen)

        # # Reset index to obtain a flat DataFrame
        # highest_df = highest_df.reset_index(drop=True)

        UtilFuncs.PickleWrite(df, output_path)

        #pd.DataFrame()
        pass 