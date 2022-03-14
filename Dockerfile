FROM python:3

# The WORKDIR command is used to define the working directory of a Docker Container.
# Any RUN , CMD , ADD , COPY , or ENTRYPOINT command will be executed in the specified working directory.
WORKDIR /usr/src/app

# This command install all the libs on the requirements.txt insede the container
COPY requirements.txt ./
RUN sudo -H pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

COPY . .

ENTRYPOINT ["streamlit", "run"]

# inside the container we have the path: /usr/src/app/src/index.py
CMD [ "./src/index.py" ]

