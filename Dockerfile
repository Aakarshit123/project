FROM redhat/ubi8
RUN yum install python3 -y
RUN pip3 install flask

COPY api.py /api.py

CMD ["python3","/api.py"]
