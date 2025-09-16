# all : graphics LSTM_DATA report

PYTHON_DIR = ./Python

SRC_REPORT_DIR = ./LateX
REPORT_DIR = ./LateX/target

graphics :
	python3 $(PYTHON_DIR)/Mars_Weather_Graphics.py

LSTM_DATA :
	python3 $(PYTHON_DIR)/LSTM_CSV_MAKER.py

report:
	pdflatex -output-directory=$(REPORT_DIR) $(SRC_REPORT_DIR)/Verin_Clement_Report.tex
	pdflatex -output-directory=$(REPORT_DIR) $(SRC_REPORT_DIR)/Verin_Clement_Report.tex
	mv $(REPORT_DIR)/Verin_Clement_Report.pdf ./
	xdg-open ./Verin_Clement_Report.pdf