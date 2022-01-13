{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red23\green23\blue23;\red218\green218\blue218;}
{\*\expandedcolortbl;;\cssrgb\c11765\c11765\c11765;\cssrgb\c88235\c88235\c88235\c50196;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
from http.server import HTTPServer, SimpleHTTPRequestHandler\
\
\
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):\
    """Entrypoint for python server"""\
    server_address = ("0.0.0.0", 8000)\
    httpd = server_class(server_address, handler_class)\
    print("launching server...")\
    httpd.serve_forever()\cf2 \cb1 \
\
\
\cf2 \cb3 if __name__ == "__main__":\
    run()}