from ResearchGate.CrawlContext import CrawlContext
from ResearchGate.RGGraphCrawlerBase import RGGraphCrawlerBase
from ResearchGate.RGGraphPersonNode import RGGraphPersonNode
from ResearchGate.RGNodeContainer import RGNodeContainer
import re
import json

class RGGraphPaperNode(RGGraphCrawlerBase):
    def __init__(self) -> None:
        super().__init__()
        self.DOI = ""
        pass

    def Parse(self, context :CrawlContext, s):
        # 提取DOI
        reges = re.compile('doi.org/[0-9.a-zA-Z/"]+>([0-9a-zA-Z./]+)</a>')
        res = reges.search(s)
        self.DOI = res.group(1)

        # 下面截取json串，里面有作者
        pattern = '<script type="application/ld+json">'
        start_pos = s.find(pattern) + len(pattern)
        end_pos = s.find('</script>', start_pos)
        json_str = s[start_pos:end_pos]
        json_result =  json.loads(json_str)
        
        authors_json = json_result['author']
        author_cnt = len(authors_json)
        for k in range(author_cnt):
            # 作者
            author_type = authors_json[k]['@type']
            author_name = authors_json[k]['name']
            author_url = authors_json[k]['url']
            person_node = RGGraphPersonNode()
            person_node.Init(author_type, author_name, author_url)
            context.NodeContainer.AddPerson(person_node)
            pass

        
        pass

    
    
