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

```
$cat deploy/nginx.template.conf \
 | sed "s/HOST/<ACTUAL_HOST>/g" \
 | sed "s/SITE_NAME/<ACTUAL_SITE_NAME>/g" \
 | sudo tee /etc/nginx/sites-available/<ACTUAL_SITE_NAME>
$sudo ln -s /etc/nginx/sites-available/<ACTUAL_SITE_NAME> \
 /etc/nginx/sites-enabled/<ACTUAL_SITE_NAME>
```

## Systemd service
- see gunicorn-systemd.template.service
- replace SITE_NAME with Url or hostname

```
$cat deploy/gunicorn-systemd.template.service \
 | sed "s/SITE_NAME/<ACTUAL_SITE_NAME>/g" \
 | sudo tee /etc/systemd/system/gunicorn-<ACTUAL_SITE_NAME>.service
```

## Enable new configurations
To update the nginx run:
```
$sudo systemctl daemon-reload
$sudo systemctl reload nginx
```

To enable the gunicorn service run:
```
$sudo systemctl enable gunicorn-<ACTUAL_SITE_NAME>.service
$sudo systemctl start gunicorn-<ACTUAL_SITE_NAME>.service
```
