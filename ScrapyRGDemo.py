from scrapy.http import Request, FormRequest
from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
import requests

class MySpider(InitSpider):
    name = 'researchgatespider'
    allowed_domains = ['researchgate.net']
    login_page = 'https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration'   # replace the valid URL 

    def init_request(self):
        #This function is called before crawling starts.
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        print(response)
        return FormRequest.from_response(response,
                formdata={'name': 'userrname', 'password': 'password'},
                callback=self.isValid_login)

    def isValid_login(self, response):
        if "XXXXXXX - term to check" in response.body:
            self.log("Successfully logged in")
            self.initialized()
        else:
            self.log("Wrong credentials")


    def parse_item(self, response):
        # write XPATH / any type of extraction here.
        pass
        
if __name__ == "__main__":
    session = requests.session()
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        "Cookie" : "did=AlSrf7jsbqPgGMeErCzigI2ewtbToaGSWqriPcM2CnkZ8YK77k41ykEDYkTKS0ai; ptc=RG1.2233128135087022392.1705920529; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; _cc_id=f5c6022b62b7069487c65bddb34ce96; pbjs-unifiedid=%7B%22TDID%22%3A%22dedfbfa3-ac9e-445f-a089-3829fed1740c%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-12-22T11%3A42%3A16%22%7D; pbjs-unifiedid_last=Mon%2C%2022%20Jan%202024%2011%3A42%3A16%20GMT; __gads=ID=15ca77dfa1f70596:T=1705920532:RT=1705928758:S=ALNI_MYeK-4FadKMwGAG58wQIu0UMXpzow; __gpi=UID=00000ced86eb1502:T=1705920532:RT=1705928758:S=ALNI_May382jzZY8FHRlFFiLwm3iqZWSKw; sid=VcbExlXddjdOLO9KXeGavQAOnS18wae3CkN1xOkGYmHAEozm3e9LZ17QS34v037EOe4Y1RAle8Ua0zMKJBBfmvBrRtckDD03267QPfHI0ynMWFBoLG4u2bnexAQxd0Vr; __cf_bm=wblUEIZEVrfC0Yobixm3BQddSE2zxJw6oIt1svRFAis-1706676496-1-AVV4mNS4LyC5BwI0T0iLaTs7bTMrZa+FrC4fP+eZZNR3rkHLUXbE4zTyxqgg59QM7P2yLZEqVc6a2U1Rx8IJA4M=; __cfruid=938938004a2e29ed8af6b5e95b3d907bff8f626d-1706676496; _cfuvid=7.qAvM2xmqZsiTQ0v.egG1xwTxt8Zhfkq6zbR4zFBE4-1706676496832-0-604800000; _gid=GA1.2.1491776271.1706676499; _ga_4P31SJ70EJ=GS1.1.1706676498.3.0.1706676498.0.0.0; cf_clearance=Osamy0C5yirPeRfDAodiO4ZKQPwiUQ_D3VTOw3GD2qc-1706676501-1-AZZM4sTidqxsDxWtNW3oC2EKXTM95JElpLYbmFIj+9cqI8z64z4QOBCPC0NEPVCrk42yd92tLZmIpyiQ50gheVg=; _ga=GA1.2.352408958.1705920529"
    }

    #url = "https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration"
    url = "https://www.researchgate.net/profile/Arlen-Moller"
    longinpage  = session.get( url,
                               headers=headers)
    print(longinpage)
    
