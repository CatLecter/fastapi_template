CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS public.users (
    user_id              UUID                        PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name            TEXT                        NOT NULL,
    mobile_phone         VARCHAR(20)                 NOT NULL,
    created_at           TIMESTAMP WITHOUT TIME ZONE NOT NULL    DEFAULT current_timestamp,
    updated_at           TIMESTAMP WITHOUT TIME ZONE NOT NULL    DEFAULT current_timestamp
);

CREATE UNIQUE INDEX idx_user_mobile_phone ON public.users (mobile_phone);

CREATE TABLE IF NOT EXISTS public.tickets (
    ticket_id            UUID                        PRIMARY KEY DEFAULT uuid_generate_v4(),
    buyer_mobile_phone   VARCHAR(20)                 NOT NULL,
    visitor_id           UUID                        NOT NULL,
    FOREIGN KEY (visitor_id)
        REFERENCES public.users (user_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    visitor_mobile_phone VARCHAR(20)                 NOT NULL,
    visitor_full_name    TEXT                        NOT NULL,
    event_name           TEXT                        NOT NULL,
    event_date           TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    sector_number        INTEGER                     NOT NULL,
    row_number           INTEGER                     NOT NULL,
    place_number         INTEGER                     NOT NULL,
    ticket_price         FLOAT(2)                    NOT NULL,
    status               VARCHAR(20)                 NOT NULL,
    created_at           TIMESTAMP WITHOUT TIME ZONE NOT NULL    DEFAULT current_timestamp,
    updated_at           TIMESTAMP WITHOUT TIME ZONE NOT NULL    DEFAULT current_timestamp
);
