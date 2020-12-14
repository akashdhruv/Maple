ARG maple_image
FROM $maple_image

MAINTAINER adhruv 

ARG maple_parfile
ARG solver_parfile

COPY $maple_parfile /home/run/$solver_parfile

WORKDIR /home/run

ENV solver_exe=__none__
CMD ["sh", "-c", "./$solver_exe"]
