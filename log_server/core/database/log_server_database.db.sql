BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "log_rmi" (
	"id"	TEXT NOT NULL UNIQUE,
	"timestamp"	TEXT NOT NULL,
	"user_ip_address"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"bytes_sent"	INTEGER NOT NULL,
	"bytes_received"	INTEGER NOT NULL,
	"time_spent"	REAL NOT NULL,
	"server_ip_address"	TEXT NOT NULL,
	"server_port"	INTEGER NOT NULL,
	"nameserver"	TEXT NOT NULL,
	"object_name"	TEXT NOT NULL,
	"object_method"	TEXT NOT NULL,
	"response_status"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "log_rest" (
	"id"	TEXT NOT NULL UNIQUE,
	"timestamp"	TEXT NOT NULL,
	"user_ip_address"	TEXT NOT NULL,
	"username"	TEXT NOT NULL,
	"bytes_sent"	INTEGER NOT NULL,
	"bytes_received"	INTEGER NOT NULL,
	"time_spent"	REAL NOT NULL,
	"server_ip_address"	TEXT NOT NULL,
	"server_port"	INTEGER NOT NULL,
	"http_method"	TEXT NOT NULL,
	"url"	TEXT NOT NULL,
	"http_status"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
COMMIT;
