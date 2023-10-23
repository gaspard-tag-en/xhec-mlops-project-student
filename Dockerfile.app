FROM python:3.11.2
WORKDIR /app_home
COPY requirements.txt /app_home/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app_home/requirements.txt
COPY src/web_service /app_home/src/web_service
WORKDIR /app_home/src/web_service  # Correction du chemin du répertoire de travail
EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
