from sqlalchemy import create_engine
from config.config_web import ConfigWeb
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, DECIMAL

Base = declarative_base()

engine = create_engine(ConfigWeb.DATABASE_URI,
                       # echo=True,
                       pool_size=10,
                       pool_recycle=60*30
                       )


DBSession = sessionmaker(bind=engine)


class CaseDetail(Base):
    __tablename__ = 'case_detail'
    id = Column(Integer, primary_key=True)
    is_deleted = Column(Integer, unique=True)
    test_method_name = Column(String(255), unique=True)
    title = Column(String(255))
    module = Column(String(255), unique=True)
    author = Column(String(255), unique=True)
    url = Column(String(255), unique=True)
    update_time = Column(DateTime)
    create_time = Column(DateTime)


class RunDetail(Base):
    __tablename__ = 'run_detail'
    id = Column(Integer, primary_key=True)
    test_method_name = Column(String(255), unique=True)
    title = Column(String(255), unique=True)
    url = Column(String(255), unique=True)
    author = Column(String(255), unique=True)
    module = Column(String(255), unique=True)
    status = Column(String(255), unique=True)
    remark = Column(String(255), unique=True)
    update_time = Column(DateTime)
    elapsed = Column(DECIMAL)


class CaseSuite(Base):
    __tablename__ = 'case_suite'
    id = Column(Integer, primary_key=True)
    suite_id = Column(Integer)
    case_id = Column(Integer)
    update_time = Column(DateTime)


class Suite(Base):
    __tablename__ = 'suite'
    id = Column(Integer, primary_key=True)
    suite_name = Column(String(255), unique=True)
    create_time = Column(DateTime)
    is_monitor = Column(Integer)
    is_deleted = Column(Integer)
    time_interval = Column(Integer)


class Urls(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(255), unique=True)
    belong = Column(String(255), unique=True)
    remark = Column(String(255), unique=True)
    update_time = Column(DateTime)
    is_deleted = Column(Integer)
    is_cover = Column(Integer)
    is_must_cover = Column(Integer)
    count = Column(Integer)


class ApiLog(Base):
    __tablename__ = 'api_log'
    id = Column(Integer, primary_key=True)
    run_id = Column(Integer)
    req_method = Column(String(255), unique=True)
    req_url = Column(String(255), unique=True)
    req_data = Column(String(255), unique=True)
    req_headers = Column(String(255), unique=True)
    res_status = Column(Integer)
    res_content = Column(String(255), unique=True)
    elapsed = Column(DECIMAL)
    update_time = Column(DateTime)
    remark = Column(String(255), unique=True)
    res_headers = Column(String(255), unique=True)


class ReportLog(Base):
    __tablename__ = 'report_log'
    id = Column(Integer, primary_key=True)
    assert_fail = Column(Integer)
    run_error = Column(Integer)
    total = Column(Integer)
    skiped = Column(Integer)
    success = Column(Integer)
    report_url = Column(String(255), unique=True)
    status = Column(String(255), unique=True)
    create_time = Column(DateTime)
    update_time = Column(DateTime)


session = DBSession()


