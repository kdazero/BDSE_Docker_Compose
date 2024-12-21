#!/bin/bash
echo "開始還原"

mkdir tmpfile
cd tmpfile

echo "下載備份檔..."
hdfs dfs -get /user/bigred/ zcxf backup.tar.gz

echo "解壓中..."
tar zcxf backup.tar.gz

ecoh "還原中..."
sudo backup_passwd > /etc/passwd
sudo backup_shadow > /etc/shadow
sudo backup_group > /etc/group

home > /home

echo "清理暫存檔..."
rm -rf tmpfile

echo "還原完成"
