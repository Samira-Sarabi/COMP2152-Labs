class Finding:
    severity_order = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}

    def __init__(self, title, severity):
        self.title = title
        self.severity = severity.upper()

    def __eq__(self, other):
        if not isinstance(other, Finding):
            return False
        return self.title == other.title and self.severity == other.severity

    def __lt__(self, other):
        return self.severity_order[self.severity] < self.severity_order[other.severity]

    def __repr__(self):
        return f"Finding('{self.title}', '{self.severity}')"


class Report:
    def __init__(self, findings=None):
        if findings is None:
            self.findings = []
        else:
            self.findings = findings

    def __len__(self):
        return len(self.findings)

    def __add__(self, other):
        return Report(self.findings + other.findings)

    def __repr__(self):
        return f"Report({self.findings})"


if __name__ == "__main__":
    f1 = Finding("Open SSH Port", "HIGH")
    f2 = Finding("Open SSH Port", "HIGH")
    f3 = Finding("Missing Security Header", "LOW")
    f4 = Finding("Weak TLS", "MEDIUM")

    print("=== Equality Check ===")
    print(f1 == f2)

    print("\n=== Sorting Findings LOW -> HIGH ===")
    findings = [f1, f3, f4]
    print(sorted(findings))

    print("\n=== Report Length ===")
    report1 = Report([f1, f3])
    report2 = Report([f4])
    print(len(report1))
    print(len(report2))

    print("\n=== Merged Reports ===")
    merged_report = report1 + report2
    print(merged_report)
    print("Total findings in merged report:", len(merged_report))