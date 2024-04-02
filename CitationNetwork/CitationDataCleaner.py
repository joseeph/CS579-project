import json_stream

from CitationNetwork.CitationAuthorNode import CitationAuthorNode
from CitationNetwork.CitationPaperNode import CitationPaperNode
from Framework.NodeContainer import NodeContainer
import CitationNetwork.CitationUtils as CitationUtils

class CitationDataCleaner:
    def __init__(self) -> None:
        pass

    def CleanData(self, src_path, dst_path):
        node_container = NodeContainer()
        f = open(src_path, 'r', encoding="utf-8")
        data = json_stream.load(f)
        
        save_frequency = 200000
        #root = data['root']
        process_num = 0
        for dat in data:
            # read the whole block
            dat = dat.persistent()

            id = 0
            authors = []
            refs = []
            title = ""
            year = 0
            n_citation = 0
            doc_type = ""
            doi = ''

            for k, v in dat.items():
                if k == 'id':
                    id = v
                elif k == 'authors':
                    authors = v
                elif k == 'title':
                    title = v
                elif k == 'year':
                    year = v
                elif k == 'n_citation':
                    n_citation = v
                elif k == 'doc_type':
                    doc_type = v
                elif k == 'doi':
                    doi = v
                elif k == 'references':
                    refs = v
            
            paper_node = CitationPaperNode()
            paper_node.SetID(id)
            paper_node.SetPaperName(title)
            paper_node.SetDOI(doi)
            paper_node.SetDocType(doc_type)
            paper_node.SetYear(year)
            paper_node.SetCitationNum(n_citation)
            # walk all references
            for cur_ref in refs:
                paper_node.AddReference(cur_ref)
            # walk all authors
            for cur_author in authors:
                author_name = ""
                author_org = ""
                author_id = 0
                for author_k, author_v in cur_author.items():
                    if author_k == 'name':
                        author_name = author_v
                    if author_k == 'org':
                        author_org = author_v
                    if author_k == 'id':
                        author_id = author_v
                    
                authornode_uid = CitationUtils.BuildCitationAuthorNodeUID(author_id)
                author_node = node_container.FindNodeWithType("CitationAuthorNode", authornode_uid)
                if author_node == None:
                    author_node = CitationAuthorNode()
                    author_node.SetAuthorID(author_id)
                    author_node.SetAuthorName(author_name)
                    author_node.SetOrganization(author_org)
                    node_container.AddNode(author_node)

                # here the raw author id is added
                paper_node.AddAuthor(author_id)
            node_container.AddNode(paper_node)
            process_num += 1
            if (process_num % save_frequency) == 0:
                CitationUtils.PickleWrite(node_container, dst_path)
        # save the result
        CitationUtils.PickleWrite(node_container, dst_path)
            