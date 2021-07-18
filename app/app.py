import os
import pandas as pd
import d6tstack

db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_pass = os.getenv('POSTGRES_PASSWORD')
db_host = 'db'
db_port = '5432'
db_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

def reformatCRMcsv(filepath):
    if 'CRM Reviews.csv' in filepath or 'CRM Events.csv' in filepath:
        fin = open(filepath, "rt", encoding = 'latin')
        data = fin.read()
        data = data.replace('\r\n', '').replace('\r', '').replace('\n', '')
        data = data.replace('2011-0', '\r\n2011-0').replace('2011-1', '\r\n2011-1')
        data = data.replace('2012-0', '\r\n2012-0').replace('2012-1', '\r\n2012-1')
        data = data.replace('2013-0', '\r\n2013-0').replace('2013-1', '\r\n2013-1')
        data = data.replace('2014-0', '\r\n2014-0').replace('2014-1', '\r\n2014-1')
        data = data.replace('2015-0', '\r\n2015-0').replace('2015-1', '\r\n2015-1')
        data = data.replace('2016-0', '\r\n2016-0').replace('2016-1', '\r\n2016-1')
        data = data.replace('2017-0', '\r\n2017-0').replace('2017-1', '\r\n2017-1')
        data = data.replace('2018-0', '\r\n2018-0').replace('2018-1', '\r\n2018-1')
        data = data.replace('2019-0', '\r\n2019-0').replace('2019-1', '\r\n2019-1')
        data = data.replace(',\r\n', ',')
        fin.close()
        fin = open(filepath, "wt", encoding = 'latin')
        fin.write(data)
        fin.close()

if __name__ == '__main__':
    print('Application started')
    arr = os.listdir('/home/lpetrocelli-retail-banking-demo-data')
    for x in arr:
        print('start '+x)
        reformatCRMcsv('/home/lpetrocelli-retail-banking-demo-data/'+x)
        df = pd.read_csv('/home/lpetrocelli-retail-banking-demo-data/'+x, skipinitialspace = True, quotechar = '"', encoding = 'latin', dtype='unicode')
        df.columns = [c.lower() for c in df.columns]
        df.to_csv('/home/'+x, sep='|', encoding='latin', index=False)
        
        df = pd.read_csv('/home/'+x, sep = '|', skipinitialspace = True, quotechar = '"', encoding = 'latin', dtype='unicode')
        d6tstack.utils.pd_to_psql(df, db_string, x.replace('.csv','').replace(' ',''), sep = '|')
        print('end '+x.replace('.csv','').replace(' ',''))