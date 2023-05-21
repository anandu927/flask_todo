FROM python:3.9

# Create a non-root user
RUN useradd -ms /bin/bash myuser
USER myuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Unit Testing
RUN ["python", "-m","pytest"]

EXPOSE 5000

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
