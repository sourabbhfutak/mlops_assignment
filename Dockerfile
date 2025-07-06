# base image
FROM python:3.10-slim

# working directory inside container
WORKDIR /app

# copy files to container
COPY requirements.txt ./

# install dependancies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# port
EXPOSE 8001

# run the app
CMD ["python", "main.py"]