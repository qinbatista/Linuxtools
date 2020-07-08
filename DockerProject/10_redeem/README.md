#### RUN
> 22：ssh，18184：下载工具 80:网站
```
docker run -itv /root/OperationLives:/root/OperationLives -v /root/redeemsystem:/root/redeemsystem -p 9989:9989  qinbatista/redeemsystem
```

> build

```
docker build -t qinbatista/redeemsystem .
```

