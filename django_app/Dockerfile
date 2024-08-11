FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
  rm -f requirements.txt && \
  useradd -m django && \
  mkdir staticfiles
COPY . .
RUN chown -R django:django .
RUN chown root:root ./dk8sdemo/settings.py
USER django
RUN python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:8000 --noreload