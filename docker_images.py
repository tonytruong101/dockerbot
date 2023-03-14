knowledge_base = {
    "alpine": ['FROM alpine:latest'],
    "alpine/git": ['FROM alpine/git:latest'],
    "archlinux": ['FROM archlinux:latest'],
    "amazon/dynamodb-local": ['FROM amazon/dynamodb-local:latest'],
    "amazonlinux": ['FROM amazonlinux:latest'],
    "apache/cassandra": ['FROM apache/cassandra:latest'],
    "apache/couchdb": ['FROM apache/couchdb:latest'],
    "apache/geode": ['FROM apache/geode:latest'],
    "apache/nifi": ['FROM apache/nifi:latest'],
    "apache/superset": ['FROM apache/superset:latest'],
    "bitnami/kafka": ['FROM bitnami/kafka:latest'],
    "blackbox_exporter": ['FROM prom/blackbox-exporter:latest'],
    "centos": ['FROM centos:latest'],
    "clickhouse/clickhouse-driver": ['FROM clickhouse/clickhouse-driver:latest'],
    "cockpit": ['FROM cockpit:latest'],
    "consul": ['FROM consul:latest'],
    "couchbase": ['FROM couchbase:latest'],
    "couchdb": ['FROM couchdb:latest'],
    "debian": ['FROM debian:latest'],
    "docker": ['FROM docker:latest'],
    "elastic/elasticsearch": ['FROM docker.elastic.co/elasticsearch/elasticsearch:latest'],
    "fedora": ['FROM fedora:latest'],
    "flink": ['FROM apache/flink:latest'],
    "gitlab/gitlab-ce": ['FROM gitlab/gitlab-ce:latest'],
    "golang": ['FROM golang:latest', 'COPY main.go .', 'RUN go build -o main'],
    "grafana/grafana": ['FROM grafana/grafana:latest'],
    "grafana/promtail": ['FROM grafana/promtail:latest'],
    "graylog/graylog": ['FROM graylog/graylog:latest'],
    "hbase": ['FROM hbase:latest'],
    "httpd": ['FROM httpd:latest', 'COPY index.html /usr/local/apache2/htdocs/'],
    "jenkins": ['FROM jenkins/jenkins:latest'],
    "jenkins/jnlp-slave": ['FROM jenkins/jnlp-slave:latest'],
    "kibana": ['FROM docker.elastic.co/kibana/kibana:latest'],
    "kubernetesui/dashboard": ['FROM kubernetesui/dashboard:v2.3.1'],
    "mailhog/mailhog": ['FROM mailhog/mailhog:latest'],
    "microsoft/dotnet": ['FROM mcr.microsoft.com/dotnet/sdk:latest', 'COPY . /app', 'WORKDIR /app', 'RUN dotnet restore', 'RUN dotnet build'],
    "minio": ['FROM minio/minio:latest'],
    "minio/mc": ['FROM minio/mc:latest'],
    "mongo": ['FROM mongo:latest', 'COPY init.js /docker-entrypoint-initdb.d/', 'CMD mongod --bind_ip_all'],
    "mongo-express": ['FROM mongo-express:latest'],
    "mysql": ['FROM mysql:latest', 'ENV MYSQL_ROOT_PASSWORD=password', 'COPY init.sql /docker-entrypoint-initdb.d/'],
    "nginx": ['FROM nginx:latest', 'COPY nginx.conf /etc/nginx/nginx.conf'],
    "nginx-flask": ['FROM nginx:latest', 'RUN apt-get update && apt-get install -y python3-flask'],
    "nginx-php": ['FROM nginx:latest', 'RUN apt-get update && apt-get install -y php-fpm'],
    "nodejs": ['FROM node:latest'],
    "nodejs-express": ['FROM node:latest', 'RUN npm install -g express'],
    "nvidia/cuda": ['FROM nvidia/cuda:latest'],
    "opensuse": ['FROM opensuse:latest'],
    "oraclelinux": ['FROM oraclelinux:latest'],
    "percona/percona-server-mongodb": ['FROM percona/percona-server-mongodb:latest'],
    "php": ['FROM php:latest', 'COPY index.php /var/www/html/'],
    "phpmyadmin": ['FROM phpmyadmin/phpmyadmin:latest'],
    "portainer/portainer-ce": ['FROM portainer/portainer-ce:latest'],
    "postgres": ['FROM postgres:latest', 'ENV POSTGRES_PASSWORD=password', 'COPY init.sql /docker-entrypoint-initdb.d/'],
    "prom/prometheus": ['FROM prom/prometheus:latest'],
    "pypy": ['FROM pypy:latest'],
    "pytorch": ['FROM pytorch/pytorch:latest'],
    "redhat": ['FROM redhat/ubi8:latest '],
    "redhat/ubi8": ['FROM redhat/ubi8:latest '],
    "rabbitmq:3.7-management": ['FROM rabbitmq:3.7-management'],
    "rabbitmq:3.8-management": ['FROM rabbitmq:3.8-management'],
    "redis": ['FROM redis:latest'],
    "ruby": ['FROM ruby'],
    "sonarqube": ['FROM sonarqube:latest'],
    "spark": ['FROM bitnami/spark:latest'],
    "tensorflow": ['FROM tensorflow/tensorflow:latest'],
    "traefik:v2.5": ['FROM traefik:v2.5'],
    "ubuntu": ['FROM ubuntu:latest'],
    "wordpress": ['FROM wordpress:latest'],
    "zookeeper": ['FROM zookeeper:latest'],
    "jesse": ['FROM jesse:latest'],
}
