#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

FROM python:3.6.8

# Install git, process tools
RUN apt-get update && apt-get -y install git procps python3-pip sqlite3

RUN mkdir /workspace
WORKDIR /workspace

# Install Python dependencies from requirements.txt if it exists
COPY requirements*.txt /workspace/
RUN if [ -f "requirements-dev.txt" ]; then pip install -r requirements-dev.txt; fi
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi && rm requirements*.txt

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Set the default shell to bash instead of sh and python to use unicode
ENV SHELL=/bin/bash \
  LC_ALL=C.UTF-8 \
  LANG=C.UTF-8
