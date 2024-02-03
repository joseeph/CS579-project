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
    result = requests.get('http://export.arxiv.org/api/query?search_query=au:"Yan Yang"&start=0&max_results=20')
    s = result.content
    print(s)
    pass

def Main3(title):
    client = arxiv.Client()
    search = arxiv.Search(
        query = 'ti:"' + title + '"',
        max_results = 10,
        sort_by = arxiv.SortCriterion.SubmittedDate
        )
    results = client.results(search)
    for r in results:
        print(r.title)

def Main4():
    
    client = arxiv.Client()
    search = arxiv.Search(
        query = 'au:"Yan Yang"',
        max_results = 10,
        sort_by = arxiv.SortCriterion.SubmittedDate
        )
    results = client.results(search)
    for r in results:
        print(r)

def Main5():
    client = arxiv.Client()
    search = arxiv.Search(
        id_list = ['2401.16862v1'],
    )
    results = client.results(search)
    for r in results:
        print(r)


if __name__ == '__main__':
    title = "Variance-Reduced Gradient Estimation via Noise-Reuse in Online Evolution Strategie"
    #title = "Deep Unsupervised Learning using Nonequilibrium Thermodynamics"
    #Main3(title)
    Main5()
    