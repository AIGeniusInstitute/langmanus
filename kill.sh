#!/usr/bin/env bash
ps -ef|grep 'uv run server.py'|awk '{print $2}'|xargs kill -9
lsof -t -i :8000 | xargs kill -9