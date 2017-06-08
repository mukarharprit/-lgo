
INF = 1e999

def min_argmin(array):
    
    mn = min(array)
    return (mn, array.index(mn))

def huffman(probs):
   
    nodes = [[x] for x in range(len(probs))]
    merged_probs = probs[:]
    while len(nodes) > 1:
        
        (mn, idx) = min_argmin(merged_probs)
        merged_probs[idx] = INF
        (mn2, idx2) = min_argmin(merged_probs)
       
        merged_probs[idx] = mn + mn2;
        del merged_probs[idx2]
        nodes[idx] = [nodes[idx], nodes[idx2]]
        del nodes[idx2]

    def huffman_helper(cur_code, nodes, codes):
        if len(nodes) == 1:
            symbol = nodes[0]
            codes[symbol] = cur_code
        else:
            huffman_helper(cur_code + '0', nodes[0], codes)
            huffman_helper(cur_code + '1', nodes[1], codes)
    codes = ['' for x in range(len(probs))]
    huffman_helper('', nodes[0], codes)
    return codes
    
def symbol_code_expected_length(probs, codes):
    return sum(x*len(y) for (x,y) in zip(probs, codes))

def Hbits(probs):
    
    from math import log
    return sum(-x*log(x, 2) for x in probs if x !=0)

def main():
    import sys
    file = open('huffman.txt')
    lines = file.readlines()
   # data = map(int,lines)
    
    probs = map(float, lines)
    Z = sum(probs)
    probs = [x/Z for x in probs]
    codes = huffman(probs)
    Lbar = symbol_code_expected_length(probs, codes)
    
    for cc in codes:
        print cc,len(cc)
   
    

if __name__ == "__main__":
    main()


