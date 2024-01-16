from sqlalchemy import URL, create_engine, orm
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

url_create = URL.create(
    drivername="mysql+asyncmy",
    username="root",
    password="123456",
    host="127.0.0.1",
    port=3306,
    database="PYTHON",
)
url_create_alenbic = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="123456",
    host="127.0.0.1",
    port=3306,
    database="PYTHON",
)

engine = create_async_engine(url_create, echo=True)
engine_base = create_engine(url_create_alenbic, echo=True)
SessionAlembic = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine_base)
SessionLocal = async_sessionmaker(autoflush=False, bind=engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
