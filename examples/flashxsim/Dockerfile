ARG maple_image
FROM $maple_image

MAINTAINER adhruv 

ARG maple_parfile
ARG maple_target

COPY $maple_parfile $maple_target/../flash.par

WORKDIR $maple_target/..

CMD ["sh", "-c", "mpirun -n 5 ./flash4 && mv *hdf5* IOData/. && mv *.log IOData/."]
