CREATE TABLE users (
    modified_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    user_id SERIAL NOT NULL, 
    name VARCHAR NOT NULL, 
    email VARCHAR NOT NULL, 
    signup_date DATE, 
    total_experiments INTEGER, 
    avg_experiments FLOAT, 
    common_compound VARCHAR, 
    PRIMARY KEY (user_id), 
    UNIQUE (name), 
    UNIQUE (email)
);

CREATE TABLE compound (
    modified_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    compound_id SERIAL NOT NULL, 
    compound_name VARCHAR NOT NULL, 
    compound_structure VARCHAR NOT NULL, 
    PRIMARY KEY (compound_id), 
    UNIQUE (compound_name), 
    UNIQUE (compound_structure)
);

CREATE TABLE experiment (
    modified_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    experiment_id SERIAL NOT NULL, 
    experiment_run_time INTEGER NOT NULL, 
    user_id INTEGER, 
    PRIMARY KEY (experiment_id), 
    FOREIGN KEY(user_id) REFERENCES users (user_id)
);

CREATE TABLE experimentcompound (
    modified_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    experiment_id INTEGER NOT NULL, 
    compound_id INTEGER NOT NULL, 
    PRIMARY KEY (experiment_id, compound_id), 
    FOREIGN KEY(experiment_id) REFERENCES experiment (experiment_id), 
    FOREIGN KEY(compound_id) REFERENCES compound (compound_id)
);
