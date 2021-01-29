@echo off
set "str=%~nx1"



if exist %str%-rebuild.apk (DEL %str%-rebuild.apk )
if exist %str%0rebuild-Signed.apk (DEL %str%-rebuild-Signed.apk)
call apktool b %str% 

RD %str%-rebuild.apk
CD %str%
CD dist

MOVE %str%.apk  ../../%str%-rebuild.apk

CD ../../

set str2=%str%-rebuild
set str3=%str%-rebuild.apk
jarsigner -verbose -keystore grannysmith.keystore -storepass hello123456 -signedjar %str2%-Signed.apk -digestalg SHA1 -sigalg MD5withRSA %str3% android.keystore

DEL %str%-rebuild.apk
