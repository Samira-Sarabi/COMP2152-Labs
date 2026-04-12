def bar_chart(data, title, max_width=30):
    """
    Draw a horizontal ASCII bar chart using █ characters.
    data should be a list of tuples: [(label, count), ...]
    """
    print(f"\n=== {title} ===")

    if not data:
        print("No data available.")
        return

    max_value = max(count for _, count in data)

    for label, count in data:
        if max_value == 0:
            bar_length = 0
        else:
            bar_length = int((count / max_value) * max_width)

        bar = "█" * bar_length
        print(f"{label:15} | {bar} ({count})")


def severity_summary(findings):
    """
    Count findings by severity and return ordered list:
    HIGH first, then MEDIUM, then LOW
    """
    counts = {}
    for finding in findings:
        severity = finding["severity"]
        counts[severity] = counts.get(severity, 0) + 1

    order = ["HIGH", "MEDIUM", "LOW"]
    return [(severity, counts[severity]) for severity in order if severity in counts]


def timeline(findings):
    """
    Count findings by date and return sorted list by date.
    """
    counts = {}
    for finding in findings:
        date = finding["date"]
        counts[date] = counts.get(date, 0) + 1

    return sorted(counts.items())


if __name__ == "__main__":
    sample_findings = [
        {"date": "2026-04-01", "severity": "HIGH", "type": "xss"},
        {"date": "2026-04-01", "severity": "MEDIUM", "type": "cors"},
        {"date": "2026-04-02", "severity": "HIGH", "type": "sqli"},
        {"date": "2026-04-02", "severity": "LOW", "type": "headers"},
        {"date": "2026-04-03", "severity": "HIGH", "type": "xss"},
        {"date": "2026-04-03", "severity": "MEDIUM", "type": "headers"},
    ]

    # Severity breakdown
    severity_data = severity_summary(sample_findings)
    bar_chart(severity_data, "Severity Breakdown")

    # Findings by date
    timeline_data = timeline(sample_findings)
    bar_chart(timeline_data, "Findings by Date")

    # Vulnerability types
    type_counts = {}
    for finding in sample_findings:
        vuln_type = finding["type"]
        type_counts[vuln_type] = type_counts.get(vuln_type, 0) + 1

    type_data = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
    bar_chart(type_data, "Vulnerability Types")