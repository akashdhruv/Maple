# Dockerfile

# Get maple_image
#
ARG maple_image
FROM ${maple_image}


# Uncomment this to build a container without root access
# TODO figure out a better way to do this
#
ARG maple_user
ARG maple_group
RUN addgroup --gid ${maple_group} user
RUN adduser --disabled-password --gecos '' --uid ${maple_user} --gid ${maple_group} user
USER user


# Uncomment this to install essential packages without accessing bash environment
# TODO: remove this or find a better way to deal with this
#
#RUN apt-get update -y && apt-get install -y apt-utils && apt-get upgrade -y && \
#    apt-get install -y build-essential && export DEBIAN_FRONTEND=noninteractive && \
#    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && apt-get install -y tzdata && \
#    apt-get install -y openmpi-bin libopenmpi-dev tzdata
