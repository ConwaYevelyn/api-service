import os
import logging
import json
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Service:
    def __init__(self, config: Dict):
        self.config = config

    def get_config(self) -> Dict:
        return self.config

    def get_data(self, endpoint: str) -> Dict:
        return self.config.get(endpoint)

    def post_data(self, endpoint: str, data: Dict) -> Dict:
        return self.config.get(endpoint, {})

    def put_data(self, endpoint: str, data: Dict) -> Dict:
        return self.post_data(endpoint, data)

    def delete_data(self, endpoint: str) -> Dict:
        return self.post_data(endpoint, {})

    def get_all_data(self, endpoint: str) -> Dict:
        return self.post_data(endpoint, {})

    def update_data(self, endpoint: str, data: Dict) -> Dict:
        return self.put_data(endpoint, data)

    def delete_all_data(self, endpoint: str) -> Dict:
        return self.delete_data(endpoint)

def main():
    config = {
        'endpoint': 'https://example.com/api',
        'username': 'user',
        'password': 'pass'
    }

    service = Service(config)
    logger.info('Service started')

    endpoint = 'users'
    data = {
        'name': 'John Doe',
        'email': 'john@example.com'
    }
    response = service.get_data(endpoint)
    logger.info(response)

    response = service.post_data(endpoint, data)
    logger.info(response)

    response = service.put_data(endpoint, data)
    logger.info(response)

    response = service.delete_data(endpoint)
    logger.info(response)

    response = service.get_all_data(endpoint)
    logger.info(response)

    response = service.update_data(endpoint, data)
    logger.info(response)

    response = service.delete_all_data(endpoint)
    logger.info(response)

if __name__ == '__main__':
    main()