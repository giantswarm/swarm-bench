import requests
import argparse
import time
import sys
import logging
import random
import string

"""
Giant Swarm API benchmark

"""

args = None
timings = []

def main():
    global args
    parser = argparse.ArgumentParser(description="Run a Giant Swarm API benchmark")
    parser.add_argument("-u", "--username", dest="username",
        help="The user name to act with")
    parser.add_argument("-t", "--token", dest="token",
        help="The auth token to act with")
    parser.add_argument("-r", "--repetitions", dest="repetitions", default=3,
        help="Number of times to call each method (default: 3)", type=int)
    parser.add_argument("--api-endpoint", dest="api_endpoint",
        help="Optional API endpoint", default="https://api.giantswarm.io/v1")
    parser.add_argument("--cluster-id", dest="cluster_id", default="alpha.private.giantswarm.io",
        help="Optional cluster ID (default: 'alpha.private.giantswarm.io')")
    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

    print("duration,label,request_id,route,statuscode")

    for n in range(args.repetitions):
        call_ping()
        call_me()
        orgs = call_memberships()
        for org in orgs:
            call_org(org)
            envs = call_environments(org)
            for env in envs:
                services = call_services(org, env["name"])
                for service in services:
                    if "service" in service:
                        call_service_status(org, env["name"], service["service"])

def generate_request_id(size=8):
    chars = string.ascii_lowercase + string.digits
    return "swarmbench-" + ''.join(random.choice(chars) for _ in range(size))

def get_request(uri, label):
    global args
    url = args.api_endpoint + uri
    request_id = generate_request_id()
    headers = {
        "User-Agent": "swarmbench",
        "Authorization": "giantswarm " + args.token,
        "X-Request-ID": request_id
    }
    if args.cluster_id:
        headers["X-Giant-Swarm-ClusterID"] = args.cluster_id
    start = time.time()
    r = requests.get(url, headers=headers, timeout=120)
    duration = time.time() - start
    datarow = {
        "label": label,
        "route": uri,
        "duration": duration,
        "status_code": r.status_code,
        "request_id": request_id
    }
    timings.append(datarow)
    print(",".join([str(datarow[x]) for x in sorted(datarow.keys())]))
    if r.status_code != 200:
        sys.stderr.write("ERROR: %s failed with status code %s\n" % (url, r.status_code))
    return r


def call_ping():
    r = get_request("/ping", "Ping")

def call_me():
    r = get_request("/user/me", "Me")

def call_memberships():
    r = get_request("/user/me/memberships", "Memberships")
    return r.json()["data"]

def call_org(org):
    r = get_request("/org/%s" % org, "Org")

def call_environments(org):
    r = get_request("/org/%s/env/" % org, "ListEnvironments")
    envs = r.json()["data"]["environments"]
    if envs is None:
        return []
    else:
        return envs

def call_services(org, env):
    r = get_request("/org/%s/env/%s/service/" % (org, env), "ListServices")
    data = r.json()
    if "data" in data:
        return data["data"]

def call_service_status(org, env, service):
    r = get_request("/org/%s/env/%s/service/%s/status" % (org, env, service), "ServiceStatus")


if __name__ == "__main__":
    main()
