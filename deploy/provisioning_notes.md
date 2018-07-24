Provisioning
============

## Required packages:
- nginx
- python 3.6
- virtualenv
- pip
- git

```
$sudo apt update
$sudo apt install nginx git python3.6 python3.6-venv
```

## Nginx virtual host config
- see nginx.template.conf
- replace SITE_NAME with Url or hostname
- replace HOST with Url or IP

## Systemd service
- see gunicorn-systemd.template.service
- replace SITE_NAME with Url or hostname
- replace HOST with Url or IP

