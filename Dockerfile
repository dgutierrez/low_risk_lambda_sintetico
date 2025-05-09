FROM public.ecr.aws/lambda/python:3.11

COPY app /var/task/

RUN pip install --upgrade pip

RUN pip install -r /var/task/requirements.txt

CMD [ "lambda_function.lambda_handler" ]