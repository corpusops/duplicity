# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf8 -*-
#
# Copyright 2019 Nils Tekampe <nils@tekampe.org>,
# Kenneth Loafman <kenneth@loafman.com> and Aaron Whitehouse <code@whitehouse.kiwi.nz>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

FROM ubuntu:20.04

# Set locale to prevent UTF-8 errors
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set to non-interactive so no tzdata prompt
ARG DEBIAN_FRONTEND=noninteractive

# Installing some pre-requisites and some
# packages needed for testing duplicity
RUN apt-get update \
    && apt-get install -y \
            2to3 \
            build-essential \
            git \
            intltool \
            lftp \
            librsync-dev \
            libffi-dev \
            libssl-dev \
            openssl \
            par2 \
            python3-pip \
            python3-dev \
            python3-future \
            python3-pip \
            python3 \
            rdiff \
            tzdata  # required for testing/unit/test_statistics.py

# The following packages are not necessary for testing but make life easier or support debugging
RUN apt-get install -y \
            ftp \
            iputils-ping \
            mc \
            nano \
            net-tools \
            rsync \
    && rm -rf /var/lib/apt/lists/*

# Installing requirements w/pip
COPY requirements.txt /tmp
RUN pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt

# Delete root's password so we can do 'su -'
RUN passwd --delete root

# Install test user and swap to it
RUN groupadd test && useradd -m -g test test
USER test

# Setting a working directory to home
WORKDIR /home/test

# Copy a SSH key to the users folder that is used for some test cases
USER root
COPY testing/docker/id_rsa /home/test/.ssh/
COPY testing/docker/id_rsa.pub /home/test/.ssh/
RUN chown -R test:test /home/test/.ssh
RUN chmod 400 /home/test/.ssh/id_rsa

USER test

# Set final workdir to duplicity
WORKDIR /home/test/duplicity
