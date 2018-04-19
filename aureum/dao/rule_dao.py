# coding:utf-8

from aureum.config import logutil
from aureum.config.db import db
from aureum.model.rule import Rule
logger = logutil.getLogger("ruledao")

class RuleDao(object):


    def selbyrule(self,rule_name):
        logger.info("selbyrule %s" %id)
        data = []
        try:
            x = db.session.query(Rule).filter(Rule.rule_name==rule_name).all()
            if len(x) > 0:
                for obj in x:
                    data.append(obj.getDict(obj))
        except Exception as err:
            print(err)
        return data

    def delbyid(self, id):
        logger.info("selbyrule %s" % id)
        try:
            db.session.begin()
            rule = db.session.query(Rule).filter(Rule.id == id).first()
            db.session.delete(rule)
            db.session.commit()
        except Exception as err:
            print(err)

ruledao = RuleDao()