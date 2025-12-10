CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(email, password)
);

CREATE TABLE transaction (
    id SERiAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES user(id),
    created_at TIMESTAMP DEFAULT NOW(),
    amount DECIMAL(10, 2) NOT NULL,
    description TEXT,
    transaction_date DATE NOT NULL
);

CREATE TABLE budget (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES user(id),
    category VARCHAR(255),
    month DATE NOT NULL UNIQUE,
    limit INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),

);

