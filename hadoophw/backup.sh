#!/bin/bash
echo "開始備份"
cat /etc/passwd > backup_passwd
sudo cat /etc/shadow > backup_shadow
cat /etc/group > backup_group

echo "建立壓縮檔"
tar zcvf backup.tar.gz backup_passwd backup_shadow backup_group /home

echo "上傳中..."
hdfs dfs -put backup.tar.gz /user/bigred/

echo "備份完成"
echo "============="

echo "請確認是否有 backup.tar.gz 這個檔案"
hdfs dfs -ls /user/bigred/
