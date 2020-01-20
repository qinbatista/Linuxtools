#### RUN
> 22：ssh，18184：下载工具 80:网站
```
docker run -itv /root/download:/root/download -p 10022:22 -p 10080:80 -p 18184:18184  qinbatista/debian_synology
```
