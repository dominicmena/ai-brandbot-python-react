FROM amazonlinux:2

# Install Python and dependencies
RUN yum install -y python37 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum install -y gcc && \
    yum install -y python3-devel && \
    yum clean all

# Upgrade pip and install virtualenv
RUN python3.7 -m pip install --upgrade pip && \
    python3.7 -m pip install virtualenv

# Create a virtual environment and activate it
RUN python3.7 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt -t /python

# Install dotenv
RUN pip install python-dotenv

# Zip it up for deployment
RUN zip -r /layer.zip /python

ENTRYPOINT ["/bin/bash", "-l"]
