from os import getenv
import psycopg
from utils.recept_search import relevant_recepts


async def get_recepts_from_db(ids:list, select:str='*') -> list[dict]:
    """получение рецептов из базы"""
    async with await psycopg.AsyncConnection.connect(conninfo=getenv('DATABASE_CONNECTION_STRING')) as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                select {select} from recepts where id in ({','.join(ids)});
                """)
            values = await cur.fetchall()
            column = [desc[0] for desc in cur.description]
            return [dict(zip(column, row)) for row in values]


async def add_new_user(tg_id:str, username:str, firstname:str, lastname:str) :
    """сохранение нового пользователя"""
    async with await psycopg.AsyncConnection.connect(conninfo=getenv('DATABASE_CONNECTION_STRING')) as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                insert into users (tg_id, username, firstname, lastname) values (%s,%s,%s,%s);
                """, (tg_id, username, firstname, lastname))
            await conn.commit() 


async def get_recepts(words:str) :
    """получение списка рецептов"""
    ids = await relevant_recepts(words=words)
    return await get_recepts_from_db(ids=ids, select='id, title, category')