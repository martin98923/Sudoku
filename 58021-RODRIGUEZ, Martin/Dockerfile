
FROM python:3

RUN git clone https://github.com/martin98923/Sudoku.git

WORKDIR /Sudoku/58021-RODRIGUEZ, Martin

RUN pip freeze > requirements.txt

RUN pip install requests

RUN pip install -r requirements.txt

CMD ["python", "./test_sudoku.py"] 