ARG maple_image
FROM $maple_image

MAINTAINER adhruv

ARG maple_user
ARG maple_group

RUN addgroup --gid $maple_group user
RUN adduser --disabled-password --gecos '' --uid $maple_user --gid $maple_group user

USER user 
