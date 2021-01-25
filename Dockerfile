ARG maple_image
FROM $maple_image

MAINTAINER adhruv 

ARG maple_parfile

COPY parfiles/$maple_parfile /home/run/flash.par

WORKDIR /home/run

CMD ["sh", "-c", "./flash4 && mv *hdf5* IOData/."]
