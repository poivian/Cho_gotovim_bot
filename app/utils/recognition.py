from os import getenv
from logging import getLogger
from io import BytesIO

import aiohttp

HEADERS = {
        'accept': 'application/json',
        # 'Content-Type': 'multipart/form-data'
        }
PARAMS = {
        'encode': 'true',
        'task': 'transcribe',
        'language': 'ru',
        'vad_filter': 'false',
        'word_timestamps': 'false',
        'output': 'txt'
}
log = getLogger(__name__)

async def recognition_audio(audio_file:BytesIO) -> str:
    """отправка аудио на распознание"""
    async with aiohttp.ClientSession(headers=HEADERS) as session:

            form_data = aiohttp.FormData()
            form_data.add_field('audio_file', audio_file, filename='voice.ogg', content_type='audio/ogg')
            for k,v in PARAMS.items():
                form_data.add_field(k, v)

            async with session.post(url=getenv('URL_WHISPER'), data=form_data) as response:

                if response.status == 200:
                    return await response.text()
                else:
                    error_response = await response.text()
                    log.error(f'Ошибка при загрузке файла:{ response.status} {error_response}')
