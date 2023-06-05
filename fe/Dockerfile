FROM node:16.13.1
USER root

RUN mkdir react

WORKDIR /root/react/

RUN apt-get update
COPY . .

RUN apt-get install -y vim less

CMD ["npm", "start"]
