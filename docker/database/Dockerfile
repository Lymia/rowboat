FROM postgres:9.6.3
RUN useradd -u 1006 -ms /bin/bash rowboat
ENV POSTGRES_USER rowboat
COPY postgres-healthcheck.sh /usr/local/bin/
COPY initdb.sh /docker-entrypoint-initdb.d/
HEALTHCHECK CMD ["postgres-healthcheck.sh"]
