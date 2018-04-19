# coding:utf-8
from sqlalchemy import Column, String, create_engine
from aureum.config import logutil
from sqlalchemy.orm import create_session
logger = logutil.getLogger("dbconfig")

class DBConfig (object):
    pass
    drip_session = None

    DB_STORM_SLAVE_URI = 'mysql+mysqlconnector://root:123456@127.0.0.1:3306/drip?charset=utf8'

    """获取数据session"""

    @property
    def session(self):
        if self.drip_session is None:
            logger.info("初始化数据库...")
            try:
                engine = create_engine(self.DB_STORM_SLAVE_URI,echo=False)
            except Exception as e :
                logger.info("数据初始化异常: %s" % e)
            self.drip_session = create_session(bind=engine)
        return self.drip_session;


db = DBConfig()