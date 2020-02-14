#### RUN
> 22：ssh，18184：下载工具 80:网站
```
docker run -itdv /root/download:/root/download -v /root/deliveried:/root/deliveried -p 10022:22 -p 18184:18184  qinbatista/download
```
