# Dockerfile

ARG maple_image
FROM ${maple_image}

MAINTAINER adhruv 

ARG maple_parfile
ARG maple_target

COPY ${maple_parfile} ${maple_target}/../flash.par

WORKDIR ${maple_target}/..

ENV maple_procs 1

CMD ["sh", "-c", "export OMPI_MCA_btl_vader_single_copy_mechanism=none && \
                  echo $maple_procs && \
                  mpirun -n $maple_procs ./flash4 && mv *hdf5* IOData/. && mv *.log IOData/."]
