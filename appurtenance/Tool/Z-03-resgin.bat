@echo off
set "str=%~nx1"
set "str1=%~n1"
RD %str%-rebuild-Signed.apk
jarsigner -verbose -keystore grannysmith.keystore -storepass hello123456 -signedjar %str1%-Signed.apk -digestalg SHA1 -sigalg MD5withRSA %str% android.keystore