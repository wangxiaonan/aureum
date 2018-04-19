# coding:utf-8


from aureum.config import logutil
from aureum.dao.rule_dao import ruledao
logger = logutil.getLogger("riskrule")

class RiskRule(object):
    pass

    def sel_byrulename(self,rule_name):
        logger.info("sel_byrulename:%s" % rule_name)
        return ruledao.selbyrule(rule_name)

    def del_byruleid(self, rule_id):
        logger.info("del_byruleid:%s" % rule_id)
        return ruledao.delbyid(rule_id)


riskrule = RiskRule()


