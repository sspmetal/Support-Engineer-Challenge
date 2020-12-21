#! /bin/bash
#
tar -cJpf /tmp/backup/backup.tar.xz /home/stefano/*
scp /tmp/backup/backup.tar.xz stefano@192.168.1.15:/tmp/backup
