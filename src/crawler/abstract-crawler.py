from abc import ABC, abstractmethod

from loguru import logger

from src.tools.redis import RedisClient
from config_logger import configure_logger

configure_logger()


class AbstractCrawler(ABC):

    def __init__(self):
        self.redis = RedisClient.get()
        pass

    @abstractmethod
    def execute_main(self):
        pass

    @abstractmethod
    def execute_before(self):
        pass

    @abstractmethod
    def execute_after(self):
        pass

    def get_step(self, key):
        return self.redis.get(key)

    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
        except:
            logger.error(f"Não foi possível salvar os dados: {e}")
            
        pass