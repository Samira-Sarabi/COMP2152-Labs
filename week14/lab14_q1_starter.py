import urllib.request
import json


def make_request(url):
    """
    Fetch a URL and return status, headers, and body as a dictionary.
    """
    try:
        response = urllib.request.urlopen(url)
        body = response.read().decode("utf-8")
        status = response.status
        headers = dict(response.headers)

        return {
            "status": status,
            "headers": headers,
            "body": body
        }
    except Exception as e:
        return {
            "status": None,
            "headers": {},
            "body": "",
            "error": str(e)
        }


def parse_json(body):
    """
    Convert a JSON string into a Python dictionary.
    """
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def check_api_info(response):
    """
    Check headers for exposed server version, technology, and CORS issues.
    """
    findings = []
    headers = response.get("headers", {})

    if "Server" in headers:
        findings.append(f"Server header exposed: {headers['Server']}")

    if "X-Powered-By" in headers:
        findings.append(f"Technology exposed via X-Powered-By: {headers['X-Powered-By']}")

    if "Access-Control-Allow-Origin" in headers:
        cors_value = headers["Access-Control-Allow-Origin"]
        if cors_value == "*":
            findings.append("CORS issue: Access-Control-Allow-Origin is set to *")
        else:
            findings.append(f"CORS configured: {cors_value}")
    else:
        findings.append("No CORS header found")

    if not findings:
        findings.append("No obvious API security issues found")

    return findings


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/1"

    response = make_request(url)

    print("=== RESPONSE ===")
    print("Status:", response["status"])
    print("Headers:", response["headers"])
    print("Body:", response["body"])

    parsed = parse_json(response["body"])
    print("\n=== PARSED JSON ===")
    print(parsed)

    findings = check_api_info(response)
    print("\n=== SECURITY FINDINGS ===")
    for finding in findings:
        print("-", finding)