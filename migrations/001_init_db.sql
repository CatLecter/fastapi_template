create EXTENSION IF NOT EXISTS "uuid-ossp";

create table if not exists public.data (
    data_uuid uuid primary key default uuid_generate_v4(), a int2, b int2, c int2, d int2, e int2, f int2, ts bigint not null
);
