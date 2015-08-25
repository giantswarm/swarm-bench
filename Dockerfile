FROM giantswarm/python
WORKDIR /
ADD requirements.txt /
RUN pip install -r ./requirements.txt
ADD benchmark.py /
ENTRYPOINT ["python", "-u", "benchmark.py"]
