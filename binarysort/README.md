Binary Sort

This is an iterative sort that takes a string as an input and returns a sorted version of that string.  It divides the string into length parts and puts each part in a queue and then compares the first elemenet of the first item in the queue to first elment of the first item in the second dataset; uses counters to keep track of data and increments counters until it reaches the end of the dataset and slowly merges the data until their is only one item in the queue (which is the value returned).  Below is an overly simplified drawing.



          abcdef  fghijk    lmnop   aabbccddeefg  kklmmno
            \       /         \         /            \
          abcdeffghijk      aabbccddeefglmnop         \
               >-------------------\-----------------> \
                                    \              abcdeffghijkklmmno
                                     \                  /
                                   aaabbbcccdddeeefffgghijkkllmmmnnoop

