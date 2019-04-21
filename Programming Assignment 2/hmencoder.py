# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:56:08 2019

@author: jainr
"""

import heapq
import os
import sys

class HeapNode:
    
    def __init__(self, character, frequency):
        self.left = None
        self.right = None
        self.character = character
        self.frequency = frequency

    def __cmp__(self, other):
        if(other == None):
            return -1
        if(not isinstance(other, HeapNode)):
            return -1
        return self.freq > other.freq
    
    def __lt__(self, other):
        if(self.frequency == other.frequency):
            self_min=self.character[0]
            other_min=other.character[0]
            for i in range(len(self.character)):
                if self.character[i]<self_min:
                    self_min= self.character[i]
            for i in range(len(other.character)):
                if other.character[i]<other_min:
                    other_min= other.character[i]
            return self_min < other_min
        return self.frequency < other.frequency
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.frequency == other.frequency


    
class HuffmanCode:
    
    def __init__(self,text):
        self.text = text
        self.min_heap = []
        self.codes = {}
        self.reverse_mapping = {}
        self.total_bits = 0
        
    
    def frequency_dict(self, text):
        freq_dict = {}
        for character in text:
            if character in freq_dict:
                freq_dict[character] += 1
            else:
                freq_dict[character] = 1
        print(freq_dict)
        return freq_dict
    
    def heap_create(self, frequency_dict):
        for character in frequency_dict:
            character_node = HeapNode(character, frequency_dict[character])
            heapq.heappush(self.min_heap, character_node)
            
    def codes_builder(self, root, current_code):
        if root == None:
            return
        if len(root.character)==1:
            self.codes[root.character] = current_code
            self.reverse_mapping[current_code] = root.character
            return
        self.codes_builder(root.right, current_code+"1")
        self.codes_builder(root.left, current_code+"0")
        

    
    def encode(self):
        
        freq_dict = self.frequency_dict(text)
        self.heap_create(freq_dict)
        
        
        #Merging all the nodes to form the final tree
        while(len(self.min_heap)> 1):
            
            left = heapq.heappop(self.min_heap)
            right = heapq.heappop(self.min_heap)
            
            if( left.character > right.character ):
                left, right = right, left
            
            mergeNode = HeapNode(left.character+right.character, left.frequency+right.frequency)
            mergeNode.left = left
            mergeNode.right = right
            
            heapq.heappush(self.min_heap, mergeNode)
         
        #Storing the codes for all the characters   
        
        root = heapq.heappop(self.min_heap)
        self.codes_builder(root, "")
        
        #Evaluating 
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
            self.total_bits += len(self.codes[character])
        return encoded_text
        

#Handeling File IO   

inputfile = sys.argv[1]
print(inputfile)

text=""

with open(inputfile, 'r') as file:
    text = file.read()
    text = text.rstrip()


encoder = HuffmanCode(text)
encoded_message = encoder.encode()

encoded_lines = [encoded_message[i:i+80] for i in range(0, len(encoded_message), 80)]
print(encoded_lines)

if(len(encoded_lines) == 1):
    msg_file = open("encodemsg.txt","w")
    msg_file.writelines(encoded_lines)
    msg_file.close()
else:
    msg_file = open("encodemsg.txt","w")
    for i in range(len(encoded_lines)):
        msg_file.write(encoded_lines[i])
        if(i < len(encoded_lines) -1):
            msg_file.write("\n")

ave_bits = round(encoder.total_bits/len(text),2)
outF = open("code.txt", "w")
for key in sorted(encoder.codes):
    if (key == " "):
        outF.write("Space"+ ": " + encoder.codes[key])
        outF.write("\n")

    else:
        outF.write(key+ ": " + encoder.codes[key])
        outF.write("\n")
outF.write("Ave = " + str(ave_bits) + " bits per symbol")
outF.close()
            