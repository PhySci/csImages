FROM python:3.10.0

RUN pip install --upgrade pip

COPY nst /app

WORKDIR /app
RUN pip install -r requirements.txt && \
    python prepare_img.py

ENV STREAMLIT_SERVER_PORT=8000

CMD ["streamlit", "run", "app.py"]