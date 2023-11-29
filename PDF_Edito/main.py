import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QAction, \
    QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor, QPixmap
from PyQt5.QtCore import Qt
from fpdf import FPDF
import fitz

class PDFEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a central widget to hold the main content
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        save_menu = self.menuBar().addMenu("File")
        save_as_pdf_action = QAction("Save as PDF", self)
        save_as_pdf_action.triggered.connect(self.save_as_pdf)
        save_menu.addAction(save_as_pdf_action)

        # Create a "Open PDF" menu item
        open_menu = self.menuBar().addMenu("File")
        open_pdf_action = QAction("Open PDF", self)
        open_pdf_action.triggered.connect(self.open_pdf)
        open_menu.addAction(open_pdf_action)

        # Create a layout for the central widget
        layout = QVBoxLayout()

        # Create a QTextEdit widget for text editing
        self.text_editor = QTextEdit(self)
        layout.addWidget(self.text_editor)

        # Create buttons for text formatting
        bold_btn = QPushButton("Bold", self)
        bold_btn.clicked.connect(self.set_text_bold)
        layout.addWidget(bold_btn)

        italic_btn = QPushButton("Italic", self)
        italic_btn.clicked.connect(self.set_text_italic)
        layout.addWidget(italic_btn)

        color_btn = QPushButton("Color", self)
        color_btn.clicked.connect(self.set_text_color)
        layout.addWidget(color_btn)

        # Create a button to insert images
        insert_image_btn = QPushButton("Insert Image", self)
        insert_image_btn.clicked.connect(self.insert_image)
        layout.addWidget(insert_image_btn)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Create a QGraphicsView for displaying images
        self.image_view = QGraphicsView(self)
        self.image_scene = QGraphicsScene(self)
        self.image_view.setScene(self.image_scene)
        layout.addWidget(self.image_view)

        # Set window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("PDF Text and Image Editor")
        self.show()

    def open_pdf(self):
        # Open a file dialog to select an existing PDF
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        pdf_file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf);;All Files (*)",
                                                       options=options)

        if pdf_file_path:
            # Clear the text editor and image view
            self.text_editor.clear()
            self.image_scene.clear()

            # Load and display the selected PDF
            pdf_document = fitz.open(pdf_file_path)
            for page_number in range(pdf_document.page_count):
                page = pdf_document.load_page(page_number)
                # image = page.get_pixmap()
                # image_item = QGraphicsPixmapItem(QPixmap.fromImage(image.to_image()))
                # self.image_scene.addItem(image_item)

                # Extract text from the PDF and add it to the text editor
                page_text = page.get_text()
                self.text_editor.append(page_text)


    def set_text_bold(self):
        # Toggle bold formatting for selected text
        format_bold = QTextCharFormat()
        format_bold.setFontWeight(75)  # 75 represents bold
        cursor = self.text_editor.textCursor()
        cursor.mergeCharFormat(format_bold)

    def set_text_italic(self):
        # Toggle italic formatting for selected text
        format_italic = QTextCharFormat()
        format_italic.setFontItalic(True)
        cursor = self.text_editor.textCursor()
        cursor.mergeCharFormat(format_italic)

    def set_text_color(self):
        # Change text color for selected text
        color = QColor.getColor()
        if color.isValid():
            format_color = QTextCharFormat()
            format_color.setForeground(color)
            cursor = self.text_editor.textCursor()
            cursor.mergeCharFormat(format_color)

    def insert_image(self):
        # Open a file dialog to select an image
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        image_path, _ = QFileDialog.getOpenFileName(self, "Insert Image", "",
                                                    "Image Files (*.png *.jpg *.jpeg *.gif *.bmp);;All Files (*)",
                                                    options=options)

        if image_path:
            # Create a QGraphicsPixmapItem to display the image
            pixmap = QPixmap(image_path)
            item = QGraphicsPixmapItem(pixmap)
            self.image_scene.addItem(item)

    def save_as_pdf(self):
        # Open a file dialog to choose the save location and file name
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        pdf_file_path, _ = QFileDialog.getSaveFileName(self, "Save as PDF", "", "PDF Files (*.pdf);;All Files (*)",
                                                       options=options)

        if pdf_file_path:
            # Create a PDF document
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Extract the text content from the text editor
            text_content = self.text_editor.toPlainText()

            # Add the text content to the PDF
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text_content)

            # Save the PDF to the specified file path
            pdf.output(pdf_file_path)


def main():
    app = QApplication(sys.argv)
    editor = PDFEditorApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
