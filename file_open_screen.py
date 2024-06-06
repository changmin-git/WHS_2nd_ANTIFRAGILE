from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTextEdit

class file_open_screen(QWidget):
    def __init__(self):
        super().__init__()

        self.left_layout = QVBoxLayout()
        self.file_open_area = QTextEdit("")
        self.file_open_area.setReadOnly(True)
        self.left_layout.addWidget(self.file_open_area)

        #self.load_file_button = QPushButton("파일 열기")
        #self.left_layout.addWidget(self.load_file_button)

        self.setLayout(self.left_layout)

    def load_file(self, file_path): 
        try:
            file_list = []
            for path in iso.list_children('/'):
                file_list.append(path)
            
            iso.close()
            
            file_content = '\n'.join(file_list)
            self.file_open_area.setText(file_content)
        
        except Exception as e:
            self.file_open_area.setText(f"Error loading file: {e}")
