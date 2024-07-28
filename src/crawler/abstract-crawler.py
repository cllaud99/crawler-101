from abc import ABC, abstractmethod
from loguru import logger
from src.tools.redis import RedisClient
from config_logger import configure_logger

configure_logger()

class AbstractCrawler(ABC):

    def __init__(self):
        self.redis = RedisClient.get()

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
        try:
            steps = self.redis.get(key)
            if steps is None:
                logger.warning(f"Chave '{key}' não encontrada no Redis.")
        except Exception as e:
            logger.error(f"Não foi possível coletar os dados do Redis: {e}")
            steps = None
        return steps

    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
            logger.info("Dados salvos com sucesso")
        except Exception as e:
            logger.error(f"Não foi possível salvar os dados: {e}")