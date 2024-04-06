import pickle
import random

from Framework.GraphDataNodeBase import GraphDataNodeBase
from Framework.NodeContainer import NodeContainer
from datetime import datetime

def BuildCitationAuthorNodeUID(id):
    return "CitationAuthor_" + str(id)

def BuildCitationPaperUID(id):
    return "CitationPaper_" + str(id)

def RegulatePaperID( paper_id ):
    if len(paper_id) < 7:
        # fill in front of the id with 0s
        paper_id = FillNodeName(paper_id, 7, '0')
    if len(paper_id) > 7:
        # keep the last 7 digits
        paper_id = paper_id[len(paper_id) - 7:]
    return paper_id

def FillNodeName(node_name, target_len, fill_with):
    fill_len = target_len - len(node_name)
    # fill character in front of node name
    new_nodename = fill_with * fill_len + node_name
    return new_nodename

def DateStrToDate(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt