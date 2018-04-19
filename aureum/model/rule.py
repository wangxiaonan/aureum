# coding:utf-8
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, String
class Rule(Base):

    def __init__(self,id,uuid="",create_time="",update_time="",rule_name=""):
        self.id = id
        self.uuid = uuid
        self.create_time = create_time
        self.update_time = update_time
        self.rule_name = rule_name
    # 表的名字:
    __tablename__ = 'rule'
    id = Column(String(20), primary_key=True)
    uuid = Column(String(32))
    create_time =Column(String(32))
    update_time =Column(String(32))
    rule_name =Column(String(32))


    def getDict(self, obj):
        data = {}
        if (isinstance(obj,Rule)):
            data['id'] = obj.id
            data['create_time'] = str(obj.create_time)
            data['update_time'] = str(obj.update_time)
            data['rule_name'] = obj.rule_name

        return data




