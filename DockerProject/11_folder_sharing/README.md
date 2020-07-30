#### RUN
> 22：ssh，18184：下载工具 80:网站
```
docker run -itv /root/download:/root/download_folder  -p 9998:9998  qinbatista/redeemsystem
```

> build

```
docker build -t qinbatista/FTPCreater .
```

