# Support-Engineer-Challenge

Nel folder excercises ci sono i 3 file di script per la risoluzione dei 3 esercizi di scripting.

L'excercise1.sh è stato svolto tramite script python.
E' sufficente lanciarlo passandogli come parametri la stringa da cercare nei files, la stringa che dovrà sostituire la stringa cercata ed il path dove cercare:
esempio:
python3 StringScanner.py stringa1 stringa2 path

L'excercise2.sh è uno script in Bash per la ricerca dei script restituendo il conteggio di quanti ne vengono trovati nelle varie sotto directories.

L'excercise3.sh è uno script che fa il backup in formato tar di una directory e trasferisce il file in un altro server via ssh:
tar -cJpf /tmp/backup/backup.tar.xz /home/stefano/*
scp /tmp/backup/backup.tar.xz stefano@192.168.1.15:/tmp/backup

Ovviamente poi è stato configurato nel crontab il lancio di tale script a mezzanotte ogni sabato:
0 0 * * 6 /home/stefano/excercises/excercise3.sh


Nel folder wordpress invece ci sono tutti i file di configurazione per il deploy rapido tramite Ansible di Wordpress su un altro server linux.

