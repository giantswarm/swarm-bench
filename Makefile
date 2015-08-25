
build:
	docker build -t registry.giantswarm.io/giantswarm/swarmbench:latest .

push:
	docker push registry.giantswarm.io/giantswarm/swarmbench:latest

run:
	docker run --rm --name swarmbench registry.giantswarm.io/giantswarm/swarmbench:latest \
