run-staging:
	docker-compose -f docker-compose-staging.yml --env-file .env.staging up -d --build --force-recreate
	docker exec -it api bash -c "cd /app && uv run alembic upgrade head"

stop-staging:
	docker-compose -f docker-compose-staging.yml down --remove-orphans

migrations:
	docker exec -it api bash -c "cd /app && uv run alembic upgrade head"

