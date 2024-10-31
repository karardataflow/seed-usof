import sys
import plotly.express as px
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

# إنشاء بيانات الرسم باستخدام Plotly
df = px.data.iris()  # بيانات عينة لرسم بياني
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# تحويل الرسم إلى HTML
plot_html = fig.to_html(include_plotlyjs='cdn', full_html=False)

# إعداد واجهة PyQt6 لعرض الرسم
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Plotly with PyQt6")

# إعداد QWebEngineView لعرض HTML الخاص بالرسم
web_view = QWebEngineView()
web_view.setHtml(plot_html)

# إعداد التخطيط لعرض QWebEngineView
central_widget = QWidget()
layout = QVBoxLayout(central_widget)
layout.addWidget(web_view)

window.setCentralWidget(central_widget)
window.resize(800, 600)
window.show()
sys.exit(app.exec())
