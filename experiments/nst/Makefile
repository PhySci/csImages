build:
	docker build -t nst:0.1 .

run :
	docker run --rm -it -p 8055:8000 --name nst nst:0.1

push:
	docker tag nst:0.1 cr.yandex/crpkujl9qm6sjqiu6a5l/img:0.1
	docker push cr.yandex/crpkujl9qm6sjqiu6a5l/img:0.1

	docker tag nst:0.1 physci/imagen:0.1
	docker push physci/imagen:0.1