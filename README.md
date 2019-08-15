# Discord bot for the VUT FIT discord server

## About

This bot manages the verification process, karma and a bunch of simple commands
on our VUT FIT discord server. Since most of the features are custom-made I
wouldn't recommend using it for different servers.

## Installing and running the bot

Prerequisites:
* Mysql #TODO
* Python3.6+

Start by cloning the repo:
```
git clone https://github.com/toaster192/rubbergod.git
cd rubbergod
```

## Local setup (not recommended)

Install the required python modules (`venv` / `--user` flag recommended):
```
pip3 install -r requirements.txt
```

Run the bot (might want to use `nohup` or something):
```
python3 rubbergod.py
```

#### Required/recommended packages (apt)

```
python3.7
python3.7-dev
python3-pip
mysql-server #TODO
libmysqlclient-dev
```

## Docker compose setup

Install `docker-compose` for your system (will vary from system to system)
and run `docker` (`systemctl start docker.service`)

```
docker-compose down && docker-compose up --build
```

## Authors

* [Matthew](https://github.com/matejsoroka)
* [Toaster](https://github.com/toaster192)
* [Fpmk](https://github.com/TheGreatfpmK)
* [Radluy](https://github.com/Radluy)
* [Urumasi](https://github.com/Urumasi)
* [Leo](https://github.com/ondryaso)

**Pull requests, issues or tips for new features are very much welcome!**

## License

This project is licensed under the GNU GPL v.3 License.
