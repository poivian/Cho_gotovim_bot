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
                insert into or replace users (tg_id, username, firstname, lastname) values (%s,%s,%s,%s);
                """, (tg_id, username, firstname, lastname))
            await conn.commit() 

async def add_stat_user(tg_id:str, stat_name:str):
    """добавление статистики"""
    async with await psycopg.AsyncConnection.connect(conninfo=getenv('DATABASE_CONNECTION_STRING')) as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                update users set {stat_name} = {stat_name} + 1 where tg_id = %(tg_id)s;
                """, {'tg_id': tg_id})
            await conn.commit() 


async def get_recepts(words:str) :
    """получение списка рецептов"""
    ids = await relevant_recepts(words=words)
    return await get_recepts_from_db(ids=ids, select='id, title, category')