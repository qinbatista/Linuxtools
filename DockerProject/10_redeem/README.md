#### RUN
> 22：ssh，18184：下载工具 80:网站
```
docker run -itv /root/OperationLives:/root/OperationLives -v /root/redeemsystem:/root/redeemsystem -p 9988:9988  qinbatista/operationlivesrequest
```

> build

```
docker build -t qinbatista/redeemsystem .
```

