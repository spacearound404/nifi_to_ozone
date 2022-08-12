# Nifi to Apache Ozone
Integration any version of NiFi to Ozone. There is script `task.py`, witch upload some data to Ozone with S3 protocol.
## Docker
Start NiFi:
```bash
docker-compose up -d
```

Start Apache Ozone:
```bash
cd ozone
docker-compose up -d
```