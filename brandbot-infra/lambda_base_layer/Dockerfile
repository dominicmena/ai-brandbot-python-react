FROM amazonlinux:2

# Install Python 3.9 and dependencies
RUN yum install -y python39 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum install -y gcc && \
    yum install -y python39-devel && \
    yum clean all

# Upgrade pip and install virtualenv
RUN python3.9 -m pip install --upgrade pip && \
    python3.9 -m pip install virtualenv

# Create a virtual environment and activate it
RUN python3.9 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt -t /python

# Install dotenv and other Python packages
RUN pip install python-dotenv
RUN pip install --upgrade typing-extensions
RUN pip install --upgrade

# Install pydantic and other dependencies
RUN python3.9 -m pip install pydantic>=1.8.1

# Install Node.js and npm
RUN curl -sL https://rpm.nodesource.com/setup_16.x | bash - && \
    yum install -y nodejs && \
    yum clean all

# Install the npm version of dotenv
RUN npm install dotenv

# Zip it up for deployment
RUN zip -r /layer.zip /python

ENTRYPOINT ["/bin/bash", "-l"]
