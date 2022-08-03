from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
import sqlalchemy_aurora_data_api
from sqlalchemy.orm import sessionmaker
import json


Base = declarative_base()

def get_connection():
    f = open("database_config.json", "r")
    database_config = json.load(f)
    # with open('database_config.json') as f:
        

    cluster_arn = database_config['CLUSTER_ARN']
    secret_arn = database_config['SECRET_ARN']
    db_engine = database_config['ENGINE']
    
    retries = 10
    gap = 5
    from time import sleep
    db_name = 'TestDBalchemy'
    engine = create_engine(f'{db_engine}+auroradataapi://:@/{db_name}',
                        echo=True,
                        connect_args=dict(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn))
    print("SQLAlchemy engine:", engine)
    while retries:
        try:
            connect = engine.connect()
        except Exception as e:
            print(e)
            sleep(gap)
            retries -= 1
            print("Retry again to connect")
        else:
            break
    if not retries:
        print("ERROR ON CONNECT")
        raise
    print("Connected!")
    return connect

alchemy_connection = get_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=alchemy_connection)

