ARG maple_image
FROM $maple_image

MAINTAINER adhruv 

ARG maple_parfile
COPY $maple_parfile /home/run/flash.par

WORKDIR /home/run

ENV maple_exe flash4
CMD ["sh", "-c", "./$maple_exe"]
