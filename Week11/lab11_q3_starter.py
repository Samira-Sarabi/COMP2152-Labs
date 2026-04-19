class Finding:
    def __init__(self, severity, host, description):
        self.severity = severity
        self.host = host
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.host} — {self.description}"


class Report:
    def __init__(self, team_name):
        self.team_name = team_name
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)

    def get_by_severity(self, severity):
        return [f for f in self.findings if f.severity == severity]

    def summary(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self.findings)}")

        high_count = len(self.get_by_severity("HIGH"))
        medium_count = len(self.get_by_severity("MEDIUM"))
        low_count = len(self.get_by_severity("LOW"))

        print(f"  HIGH:   {high_count}")
        print(f"  MEDIUM: {medium_count}")
        print(f"  LOW:    {low_count}")
        print("  ----------------------------------------")

        for finding in self.findings:
            print(f"  {finding}")


# MAIN
if __name__ == "__main__":
    print("=" * 60)
    print("  Q3: VULNERABILITY REPORT")
    print("=" * 60)

    report = Report("CyberHunters")

    print("\n--- Adding Findings ---")
    findings = [
        Finding("HIGH", "ssh.0x10.cloud", "Default credentials admin:admin"),
        Finding("LOW", "blog.0x10.cloud", "No HTTPS (cleartext)"),
        Finding("HIGH", "ftp.0x10.cloud", "Anonymous FTP access"),
        Finding("MEDIUM", "api.0x10.cloud", "Server version exposed in headers"),
        Finding("LOW", "cdn.0x10.cloud", "Missing security headers")
    ]

    for f in findings:
        report.add_finding(f)
        print(f"  Added: {f}")

    print("\n--- Full Report ---")
    report.summary()

    print("\n--- HIGH Severity Only ---")
    for f in report.get_by_severity("HIGH"):
        print(f"  {f}")

    print("=" * 60)