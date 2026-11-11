"""Compose validator service: connect to Postgres, store one check, print the result."""

import os
import sys

import psycopg2

from duty_validator import validate_duty


def main():
    conn = psycopg2.connect(
        host=os.environ["DATABASE_HOST"],
        port=os.environ.get("DATABASE_PORT", "5432"),
        dbname=os.environ["DATABASE_NAME"],
        user=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
    )
    print("Database connection: SUCCESS")

    ok, reason = validate_duty(10, 60, 10)
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS duty_checks (
                    id SERIAL PRIMARY KEY,
                    hours_today DOUBLE PRECISION,
                    hours_last_7_days DOUBLE PRECISION,
                    rest_hours DOUBLE PRECISION,
                    accepted BOOLEAN,
                    reason TEXT
                )
                """
            )
            cur.execute(
                """
                INSERT INTO duty_checks
                    (hours_today, hours_last_7_days, rest_hours, accepted, reason)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (10, 60, 10, ok, reason),
            )
            cur.execute("SELECT COUNT(*) FROM duty_checks")
            count = cur.fetchone()[0]
    conn.close()
    print(f"Validator result: accepted={ok} reason={reason}")
    print(f"Rows stored in duty_checks: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
