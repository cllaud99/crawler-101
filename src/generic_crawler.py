import json

from crawler.abstract_crawler import AbstractCrawler


class GenericCrawler(AbstractCrawler):

    data_frame = None

    def __init__(self, type):
        super().__init__()
        self.type = type
        self.steps = json.loads(self.get_step(self.type))

        if self.steps is None:
            raise('Crawler Não Configurado')

    def start(self):
        self.execute_before()
        self.execute_main()
        self.execute_after()
        self.save_data(self.data_frame)
    
    def execute_before(self):
        pass
    
    def execute_main(self):
        pass

    def execute_after(self):
        pass

    def extraction(self):
        pass