FROM pypy:3
WORKDIR /app
RUN pip install --no-cache-dir numpy

COPY prime_checker.py .
COPY primes.npy .


ENTRYPOINT ["pypy3", "prime_checker.py"]
