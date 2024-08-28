FROM python:3.10

EXPOSE 9000

COPY main.py .
COPY requirements.txt .
# COPY setup.sh /usr/share/backend/

# preparing enviromnent
RUN pip install -r requirements.txt

# running app

ENTRYPOINT python main.py
