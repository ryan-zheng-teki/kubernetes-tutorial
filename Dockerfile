FROM python:3.8.2
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install --upgrade pip
ADD /app/app.py app.py
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]