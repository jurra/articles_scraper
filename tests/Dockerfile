# syntax=docker/dockerfile:1

# FROM node:current AS builder
# WORKDIR /build
# COPY gridsome-website ./
# RUN npm install && gridsome build

FROM nginx:stable
WORKDIR /blog
COPY  /dist /usr/share/nginx/html/
EXPOSE 80