#!/bin/sh

clean(){
  nerdctl rm -f $(nerdctl ps -aq)
}
build(){
  cd ./python
  nerdctl build -t server .
  cd ..
  cd ./nodejs-agent
  nerdctl build -t agent .
  cd ..
}
run(){
  nerdctl run -d --network temp -v ${PWD:2}/python/credentials:/root/.aws/credentials -p 3000:3000 --name server server
  nerdctl run -d --network temp --name agent agent
  nerdctl ps -a

}

case $1 in
  b)
    build
  ;;
  r)
    run
  ;;
  c)
    clean
  ;;
  cr)
    clean
    run
  ;;
  cbr)
    clean
    build
    run
  ;;
esac