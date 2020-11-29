''' reverse the bits of the given number
input | output
1100  | 0011
1011  | 1101

'''

def reverse_bits(x):
  output = 0
  while(x != 0):
    output = output << 1 # left shift the output by 1
    if(x & 1 == 1):
      output = output | 1 # or with 1
    x = x >> 1 # right shift the number by 1
  return output
  
  
TIME COMPLEXITY = O(N) => This depends on the number of bits
SPACE COMPLEXITY = O(1) => since only output variable is taken so the space complexity is constant
