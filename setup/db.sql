create database mypydns;
grant all on mypydns.* to mypydns@localhost identified by 'mypydns';

use mypydns;

create table client_hosts(
    host_id int unsigned not null primary key auto_increment,
    host_ip varchar(20) not null unique,
    host_name varchar(250)
);

create table dns_requests(
    req_id int unsigned not null primary key auto_increment,
    host_id int unsigned not null,
    request_query varchar(250),
    query_type varchar(50),
    request_time datetime
);

create table redirects(
    rule_id int unsigned not null primary key auto_increment,
    redirect_ip varchar(200),
    client_host_specs varchar(250),
    query_domain varchar(250),
    query_type varchar(20), /* A, AAAA, MX, SOA etc */
    enabled bool default 1
);

