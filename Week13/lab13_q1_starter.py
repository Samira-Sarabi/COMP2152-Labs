import csv


def load_findings(filename):
    """
    Read the CSV file and return a list of dictionaries.
    """
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def count_by_field(findings, field):
    """
    Count occurrences of each unique value in a given field.
    """
    counts = {}
    for finding in findings:
        value = finding[field]
        counts[value] = counts.get(value, 0) + 1
    return counts


def filter_findings(findings, field, value):
    """
    Return findings where finding[field] == value.
    """
    return [finding for finding in findings if finding[field] == value]


def top_subdomains(findings, n):
    """
    Return the top n most targeted subdomains as a list of tuples.
    """
    counts = count_by_field(findings, "subdomain")
    sorted_subdomains = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_subdomains[:n]

if __name__ == "__main__":
    # Create sample CSV
    with open("findings.csv", "w", newline="", encoding="utf-8") as f:
        f.write("subdomain,type,severity,date\n")
        f.write("ssh.0x10.cloud,default_creds,HIGH,2026-04-01\n")
        f.write("api.0x10.cloud,xss,MEDIUM,2026-04-01\n")
        f.write("app.0x10.cloud,sqli,HIGH,2026-04-02\n")
        f.write("ssh.0x10.cloud,headers,LOW,2026-04-02\n")
        f.write("api.0x10.cloud,xss,HIGH,2026-04-03\n")

    filename = "findings.csv"
    findings = load_findings(filename)

    print("=== Severity Counts ===")
    print(count_by_field(findings, "severity"))

    print("\n=== Type Counts ===")
    print(count_by_field(findings, "type"))

    print("\n=== HIGH Findings ===")
    high_findings = filter_findings(findings, "severity", "HIGH")
    for finding in high_findings:
        print(finding)

    print("\n=== Top 3 Subdomains ===")
    print(top_subdomains(findings, 3))