import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class ReclameAquiScraper:

    def __init__(self):
        self.page = 1
        self.results_per_page = 90
        self.keyword = ''
        self.type_rank = "best"
        self.http = self._configure_session()
        self.content = None

    def start(self, keyword):
        self.keyword = keyword
        return self.search_companies()

    def _configure_session(self):
        retry_strategy = Retry(total=3, status_forcelist=[403, 429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session

    def search_companies(self):
        url = f"https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/segments/ranking/{self.type_rank}/{self.keyword}/{self.page}/{self.results_per_page}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept": "application/json",
        }
        try:
            response = self.http.get(url, headers=headers)
            if response.status_code == 200:
                self.content = response.json()  # Armazenando a resposta no atributo content
                return self.content
            else:
                print(f"Request failed with status code {response.status_code}")
                print(response.text)
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        
    def get_companies_data(self):
        if self.content:
            companies = self.content.get("companies", [])
            return companies
        else:
            return []


keyword = "bancos-tradicionais-e-digitais"
scraper = ReclameAquiScraper()

scraper.start(keyword=keyword)
companies_data = scraper.get_companies_data()
print(companies_data)