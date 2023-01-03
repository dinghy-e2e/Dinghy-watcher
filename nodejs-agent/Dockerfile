FROM alpine:edge
WORKDIR /app
RUN apk update && apk upgrade && apk add nodejs npm
# COPY ./package.json ./
# COPY ./package-lock.json ./
COPY . .
RUN npm i 
CMD node main.js