ARG maple_image
FROM $maple_image

MAINTAINER adhruv 

#ARG USER_ID
#ARG GROUP_ID

#RUN addgroup --gid $GROUP_ID user
#RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

#USER user

ARG maple_parfile
COPY $maple_parfile /home/run/flash.par

WORKDIR /home/run

CMD ["sh", "-c", "./flash4 && mv *hdf5* IOData/. && mv *.log IOData/."]
