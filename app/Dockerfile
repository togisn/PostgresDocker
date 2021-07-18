FROM python:latest
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh
COPY app.py app.py

RUN wget https://github.com/togisn/fileshare/raw/main/lpetrocelli-retail-banking-demo-data.zip.001 -P /home
RUN wget https://github.com/togisn/fileshare/raw/main/lpetrocelli-retail-banking-demo-data.zip.002 -P /home

RUN cat /home/lpetrocelli-retail-banking-demo-data.zip* > /home/lpetrocelli-retail-banking-demo-data.zip
RUN unzip /home/lpetrocelli-retail-banking-demo-data.zip -d /home
RUN rm -rf /home/lpetrocelli-retail-banking-demo-data.zip.002
RUN rm -rf /home/lpetrocelli-retail-banking-demo-data.zip.001
RUN rm -rf /home/lpetrocelli-retail-banking-demo-data.zip
