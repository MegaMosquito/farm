FROM debian:bookworm

# Initialize apt
RUN apt update && apt install -y --no-install-recommends gnupg

# Install requirements and clean up
RUN apt update && apt install -y --no-install-recommends \
  python3-dev \
  python3-pip \
  python3-requests \
  python3-flask \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/cache/apt/archives/* \
  && rm -rf /var/lib/apt/lists/*

# Copy over my source code
RUN mkdir -p  /farm
COPY . /farm/
WORKDIR /farm

# Start the daemon
CMD [ "python3", "farm.py" ]

