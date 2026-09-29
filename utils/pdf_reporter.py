from pathlib import Path

from utils.pdf_report import PdfReport


def pytest_runtest_makereport(item, call):
    if call.when != "call":
        return

    if not hasattr(item, "report_steps"):
        return

    steps = item.report_steps

    if steps:
        PdfReport.generate(
            item.name,
            steps
        )