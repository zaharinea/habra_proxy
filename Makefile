APP_PORT = "8000"
APP_HOST = "0.0.0.0"
APP_NAME = "habra_proxy"
APP_IMAGE = "habra_proxy"

NETWORK="habra_proxy"


dep:
	python3.6 -m venv .venv && \
        source .venv/bin/activate && \
        pip install -r requirements.txt && \
        deactivate

run:
	.venv/bin/python app.py

test:
	pytest -v --cov-report term --cov=proxy tests/

docker-remove-network:
	docker network remove ${NETWORK} || true

docker-create-network: docker-remove-network
	docker network create ${NETWORK} || true


docker-build:
	docker build -t "${APP_IMAGE}" .


docker-remove:
	docker rm -f ${APP_NAME}  || true

docker-run: docker-create-network docker-build docker-remove
	docker run -d \
		--net ${NETWORK} \
		--name ${APP_NAME} \
		-p ${APP_PORT}:${APP_PORT} \
		-e HOST=${APP_HOST} \
		-e PORT=${APP_PORT} \
		${APP_IMAGE}
