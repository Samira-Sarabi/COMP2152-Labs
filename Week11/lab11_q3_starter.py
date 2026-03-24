class Finding:
    def __init__(self, severity, target, description):
        self.severity = severity
        self.target = target
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.target} — {self.description}"


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
        print(f"  HIGH:   {len(self.get_by_severity('HIGH'))}")
        print(f"  MEDIUM: {len(self.get_by_severity('MEDIUM'))}")
        print(f"  LOW:    {len(self.get_by_severity('LOW'))}")
        print("  ----------------------------------------")
        for finding in self.findings:
            print(f"  {finding}")


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
        Finding("LOW", "cdn.0x10.cloud", "Missing security headers"),
    ]

    for finding in findings:
        report.add_finding(finding)
        print(f"  Added: {finding}")

    print("\n--- Full Report ---")
    report.summary()

    print("\n--- HIGH Severity Only ---")
    for finding in report.get_by_severity("HIGH"):
        print(f"  {finding}")

    print("\n" + "=" * 60)