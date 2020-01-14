CREATE USER reader WITH PASSWORD 'reader';

CREATE USER writer WITH PASSWORD 'writer';

\c db

CREATE TABLE events(
            timestamp DATE,
            type VARCHAR(255),
            payload VARCHAR(2000));

GRANT UPDATE, INSERT ON events TO writer;
GRANT SELECT ON events TO reader;

