FROM python:3.9.12 
# start by pulling the python image

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]

# docker image build -t flask-portfilio .

# docker run -p 80:80 --name flask-portfilio flask-portfilio

# docker start flask-portfilio

# docker stop flask-portfilio