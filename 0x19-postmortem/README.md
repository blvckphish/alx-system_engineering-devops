# POSTMORTEM

We experienced a inconsistency in my company's API infrastructure. The APIs were hosted across multiple servers with a load balancer at the frontend. The load balancer was using the round robin algorithm so the servers were getting queried equally. The data being returned by the API was inconsistent, each server went out of sync with the others. User's created accounts but could not login and even when they did after many attempt, the backend could not authenticate their JWT tokens.

## Timeline (West African Time)

- 11:19 pm: Deployment done
- 11:30 pm: Bug noticed
- 01:13 am: Bug patched
- 02:11 pm: Bug fixed, users 100% online

## Root Cause

At 11:19 WAT, a new version of the API was pushed to production, this was the first time that the API was being hosted on multiple servers, so a central database was put on it's own server and the API
