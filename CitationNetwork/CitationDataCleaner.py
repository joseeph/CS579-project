import json_stream

from CitationNetwork.CitationAuthorNode import CitationAuthorNode
from CitationNetwork.CitationPaperNode import CitationPaperNode
from Framework.NodeContainer import NodeContainer
import CitationNetwork.CitationUtils as CitationUtils
import copy

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
            fos = []

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
                elif k == 'fos':
                    fos = v
            
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

            # walk all fos
            for cur_fos in fos:
                fos_name = ""
                fos_w = 0
                for k, v in cur_fos.items():
                    if k == 'name':
                        fos_name = v
                    elif k == 'w':
                        fos_w = v
                paper_node.AddFOS(fos_name, fos_w)


            node_container.AddNode(paper_node)
            process_num += 1
            if (process_num % save_frequency) == 0:
                CitationUtils.PickleWrite(node_container, dst_path)
        # save the result
        CitationUtils.PickleWrite(node_container, dst_path)
    
    def ProcessAddPaperNode(self, data_container :NodeContainer, new_container :NodeContainer, node:CitationPaperNode):
        new_node = copy.copy(node)
        is_exist = new_container.InNodeExistByUID(new_node.GetUID())
        if is_exist:
            return
        # add the new node
        new_container.AddNode(new_node)
        
        # add authors 
        for cur_authorid in node.AuthorIDs:
            author_uid = CitationUtils.BuildCitationAuthorNodeUID(cur_authorid)
            author_node :CitationAuthorNode = data_container.FindNodeWithType("CitationAuthorNode", author_uid)
            if author_node != None:
                if not new_container.InNodeExistByUID(author_uid):
                    new_container.AddNode(copy.copy(author_node))
        
    def CleanStep2(self, src_path, dst_path):
        data_container : NodeContainer = CitationUtils.PickleRead(src_path)
        new_datacontainer :NodeContainer = NodeContainer()
        node_map = data_container.GetAllNodesByType("CitationPaperNode")
        cs_fos = 'Computer science'
        toadd_refpapers = []
        for k in node_map:
            node :CitationPaperNode = node_map[k]
            
            # if the field has computer scienece, then add it to new container
            if node.IsInFOS(cs_fos):
                # add this node to new container
                self.ProcessAddPaperNode(data_container, new_datacontainer, node)
                
                # walk all the references, if it is not a computer sceience paper, then add it to the queue
                for ref_id in node.RefIDs:
                    ref_paper_uid = CitationUtils.BuildCitationPaperUID(ref_id)
                    ref_paper_node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", ref_paper_uid)
                    if ref_paper_node != None:
                        if not ref_paper_node.IsInFOS(cs_fos):
                            # it is not a cs paper
                            if not (ref_id in toadd_refpapers):
                                # and it is no in the queue, then add it to the queue
                                toadd_refpapers.append(ref_id)
        # at last, add the referenced papers not in cs scope
        for ref_id in toadd_refpapers:
            ref_paper_uid = CitationUtils.BuildCitationPaperUID(ref_id)
            ref_papernode = data_container.FindNodeWithType("CitationPaperNode", ref_paper_uid)
            self.ProcessAddPaperNode(data_container, new_datacontainer, ref_papernode)
        
        # save the result
        CitationUtils.PickleWrite(new_datacontainer, dst_path)
    
    
                


                
            

            