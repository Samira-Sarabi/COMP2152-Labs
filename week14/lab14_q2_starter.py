import urllib.request

REQUIRED_HEADERS = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]


def check_headers(url):
    """
    Check one URL for required security headers.
    Return a dictionary with header names and whether they are present or missing.
    """
    results = {}

    try:
        response = urllib.request.urlopen(url)
        headers = dict(response.headers)

        for header in REQUIRED_HEADERS:
            if header in headers:
                results[header] = ("Present", headers[header])
            else:
                results[header] = ("Missing", None)

    except Exception as e:
        print(f"Error checking {url}: {e}")

    return results


def generate_report(url, results):
    """
    Print a report showing which headers are present or missing.
    """
    print(f"\nChecking URL: {url}")

    explanations = {
        "X-Frame-Options": "Protects against clickjacking attacks.",
        "Content-Security-Policy": "Helps prevent XSS and content injection.",
        "X-Content-Type-Options": "Prevents MIME-type sniffing.",
        "Strict-Transport-Security": "Forces HTTPS connections."
    }

    for header, (status, value) in results.items():
        if status == "Present":
            print(f"✓ {header}: {value}")
        else:
            print(f"✗ {header}: Missing — {explanations[header]}")


if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://www.google.com"
    ]

    for url in urls:
        results = check_headers(url)
        generate_report(url, results)