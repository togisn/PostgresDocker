FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY data/LuxuryLoanPortfolio.zip LuxuryLoanPortfolio.zip
RUN unzip LuxuryLoanPortfolio.zip
COPY pages/* pages/
COPY app.py app.py
CMD ["python", "-u", "app.py"]