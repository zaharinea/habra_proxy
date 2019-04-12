[![Build Status](https://travis-ci.com/zaharinea/habra_proxy.svg?token=PnQCGzxy6VzwsgZcmsxs&branch=master)](https://travis-ci.com/zaharinea/habra_proxy)

# Habraproxy
This application proxies incoming requests to the url specified in config.TARGET_URL. The response received from the server is converted to the following form:
* To the words of six letters added the symbol "™";
* URLs in the config.REPLACE_URLS list are replaced with the proxy server URL.

## run habra_proxy
```bash
make dep
make run
```
and open in the browser http://localhost:8000

## run habra_proxy in docker
```bash
make docker-run
```
and open in the browser http://localhost:8000