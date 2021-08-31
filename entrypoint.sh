#!/usr/bin/env bash
# export FLASK_APP=todo
# export FLASK_ENV=development
# python main.py db init
# python main.py db migrate
# python main.py db upgrade
python main.py db init
python main.py db migrate
python main.py db upgrade

psql -U postgres -d postgres -f /docker-entrypoint-initdb.d/10-init.sql -h db
# psql+=( --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" )

#         echo
#         for f in /docker-entrypoint-initdb.d/*; do
#             case "$f" in
#                 *.sh)     echo "$0: running $f"; . "$f" ;;
#                 *.sql)    echo "$0: running $f"; "${psql[@]}" < "$f"; echo ;;
#                 *.sql.gz) echo "$0: running $f"; gunzip -c "$f" | "${psql[@]}"; echo ;;
#                 *)        echo "$0: ignoring $f" ;;
#             esac
#             echo
#         done

python main.py