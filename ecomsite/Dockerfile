FROM python:latest
WORKDIR /app
COPY requirments.txt requirments.txt
RUN pip3 install --no-cache-dir -r requirments.txt
EXPOSE 8000
COPY . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]