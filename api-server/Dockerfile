FROM alpine:edge
WORKDIR /app
COPY ./src .
RUN apk upgrade && apk add bash curl nodejs=18.12.1-r0 npm=9.1.2-r0
ENV NODE_ENV=production
RUN npm ci 
CMD [ "npm", "run" , "start" ]
EXPOSE 3000