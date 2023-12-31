Command line utilities
======================

*Note*. For windows use ``py -3 -m ...`` instead of ``python -m ...`` .

mbstat
------

::

   $ python -m microbin.mbstat -h
   usage: microbin.mbstart [-h] [-V] [-s {count,size,bpo}] file

   Analyze MicroBIN file

   positional arguments:
     file                  MicroBIN file to analyze

   options:
     -h, --help            show this help message and exit
     -V, --version         show program's version number and exit
     -s {count,size,bpo}, --sort {count,size,bpo}
                           set field to sort (default: size)

   (c) NekoNekoNyan <me@neko-dev.ru>, 2023

mb2json
-------

::

   $ python -m microbin.mb2json -h
   usage: microbin.mb2json [-h] [-V] [-o OUTPUT] [-m MAGIC] [-c] [-a] file

   Convert MicroBIN file to json

   positional arguments:
     file                  MicroBIN file to convert

   options:
     -h, --help            show this help message and exit
     -V, --version         show program's version number and exit
     -o OUTPUT, --output OUTPUT
                           set output json file (default: standart output)
     -m MAGIC, --magic MAGIC
                           set application magic (default: 0000)
     -c, --compact         create compact json
     -a, --ascii           create json without any non-ascii characters

   (c) NekoNekoNyan <me@neko-dev.ru>, 2023

json2mb
-------

::

   $ python -m microbin.json2mb -h
   usage: microbin.json2mb [-h] [-V] [-i INPUT] [-m MAGIC] [-f {16,32,64}] file

   Convert json to MicroBIN file

   positional arguments:
     file                  output MicroBIN file

   options:
     -h, --help            show this help message and exit
     -V, --version         show program's version number and exit
     -i INPUT, --input INPUT
                           set input json file (default: standart input)
     -m MAGIC, --magic MAGIC
                           set application magic (default: 0000)
     -f {16,32,64}, --float-size {16,32,64}
                           set size of float numbers (in bits; default: 64)

   (c) NekoNekoNyan <me@neko-dev.ru>, 2023
