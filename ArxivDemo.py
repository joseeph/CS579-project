import arxiv
import requests

def Main():
    client = arxiv.Client()
    search = arxiv.Search(
        query = 'au:"Yan Yang"',
        max_results = 10,
        sort_by = arxiv.SortCriterion.SubmittedDate
        )
    results = client.results(search)
    for r in results:
        print(r.title)
    

def Main2():
    author_name = "Yan Yang"
    papers = arxiv.query(query=f"au:{author_name}", max_results=5)
    print(papers)

def Main3():
    result = requests.get('http://export.arxiv.org/api/query?search_query=au:"Yan Yang"&start=0&max_results=20')
    s = result.content
    print(s)
    pass

if __name__ == '__main__':
    Main()
    