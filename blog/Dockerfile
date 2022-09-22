FROM python:3

RUN pip install Flask

COPY app.py .

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000"]
