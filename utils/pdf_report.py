import os
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


class PdfReport:

    @staticmethod
    def generate(test_name: str, steps: list[dict]) -> None:

        report_dir = os.path.join("reports", "pdf")
        os.makedirs(report_dir, exist_ok=True)

        safe_test_name = re.sub(r'[<>:"/\\|?*]', "_", test_name)
        file_path = os.path.join(
            report_dir,
            f"{safe_test_name}.pdf"
        )

        doc = canvas.Canvas(file_path, pagesize=A4)

        page_width, page_height = A4

        # =========================
        # Report Header
        # =========================

        doc.setFont("Helvetica-Bold", 20)
        doc.drawCentredString(
            page_width / 2,
            page_height - 50,
            "Test Execution Report"
        )

        doc.setFont("Helvetica", 12)
        doc.drawString(
            40,
            page_height - 80,
            f"Test: {test_name}"
        )

        current_page = ""
        y = page_height - 120

        # =========================
        # Test Steps
        # =========================

        for step in steps:

            if current_page != step["page"]:
                current_page = step["page"]

                if y != page_height - 120:
                    doc.showPage()

                doc.setFont("Helvetica-Bold", 18)
                doc.drawString(40, page_height - 50, current_page)

                y = page_height - 80

            # New page if required
            if y < 60:
                doc.showPage()
                doc.setFont("Helvetica-Bold", 18)
                doc.drawString(40, page_height - 50, current_page)
                y = page_height - 80

            doc.setFont("Helvetica", 13)
            doc.setFillColorRGB(0, 0, 0)
            doc.drawString(40, y, step["method"])

            # =========================
            # Status
            # =========================

            if step["status"] == "PASS":
                doc.setStrokeColorRGB(0, 0.5, 0)
                doc.setLineWidth(2)

                doc.line(410, y + 7, 416, y + 13)
                doc.line(416, y + 13, 426, y)

                doc.setFillColorRGB(0, 0.5, 0)
                doc.setFont("Helvetica", 12)
                doc.drawString(435, y, "PASS")

            else:
                doc.setStrokeColorRGB(1, 0, 0)
                doc.setLineWidth(2)

                doc.line(410, y + 2, 422, y + 14)
                doc.line(422, y + 2, 410, y + 14)

                doc.setFillColorRGB(1, 0, 0)
                doc.setFont("Helvetica", 12)
                doc.drawString(435, y, "FAIL")

            doc.setFillColorRGB(0, 0, 0)

            # =========================
            # Screenshot
            # =========================

            screenshot = step["screenshot"]

            if os.path.exists(screenshot):

                doc.showPage()

                doc.setFont("Helvetica", 14)
                doc.drawString(
                    40,
                    page_height - 40,
                    f'{current_page} - {step["method"]}'
                )

                doc.setFont("Helvetica", 11)
                doc.drawRightString(
                    page_width - 40,
                    page_height - 42,
                    step["status"]
                )

                image_width = 500
                image_x = (page_width - image_width) / 2

                image = ImageReader(screenshot)
                image_width_original, image_height_original = image.getSize()

                image_height = (
                    image_height_original
                    * image_width
                    / image_width_original
                )

                doc.drawImage(
                    image,
                    image_x,
                    page_height - 70 - image_height,
                    width=image_width,
                    height=image_height,
                    preserveAspectRatio=True,
                    anchor="n"
                )

                y = page_height - 120

            else:
                y -= 25

        doc.save()

        print(f"PDF Report: {file_path}")