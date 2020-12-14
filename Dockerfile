ARG flash_image=akashdhruv/flash:latest

FROM $flash_image

COPY flash.par /home/run/.

WORKDIR /home/run

CMD ["./flash4"]
