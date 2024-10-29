from os import getenv
from logging import getLogger
import aiohttp


HEADERS = {
        'accept': 'application/json',
        }
log = getLogger(__name__)

async def relevant_recepts(words:str) -> list:
    """получение списка ID релевантных рецептов"""
    async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.post(url=getenv('URL_EMBEDDING'), 
                                    json={"text": words}) as response:

                if response.status == 200:  
                    ids =  await response.json()   
                    return ids.get('ids')
                else:
                    error_response = await response.json()
                    log.error(f'Ошибка ембеддинга:{ response.status} {error_response}')
                    return []
