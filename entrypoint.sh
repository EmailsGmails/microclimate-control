#!/bin/sh
echo "ENTRYPOINTING"
if [ "$DATABASE_TYPE" = "postgres" ]
then
    echo "Waiting for postgres..."
#    psql -lqt | cut -d \| -f 1 | grep -qw $DB_NAME

    while ! nc -z $DATABASE_HOST $DATABASE_PORT ; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"