FROM python:alpine
LABEL name="gt-planner-backend"

# install pip packages
RUN pip install fastapi uvicorn graphviz

# set working directory
WORKDIR /app

# run server
CMD ["python", "main.py"]
