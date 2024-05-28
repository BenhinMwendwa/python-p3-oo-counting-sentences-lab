#!/usr/bin/env python3

class MyString:
   def __init__(self,value=''):
      if isinstance(value,str):
         self.value = value
      else: 
        print ( 'The value must be a string.\n')
        self.value=''
   def get_value(self):
      self.value
   
   def is_sentence(self):
       return self.value.endswith('.')
   def is_question(self):
       return self.value.endswith('?')
   def is_exclamation(self):
     return self.value.endswith('!')
def test_count_sentences(self):
    
    string = MyString("one. two. three?")
    string.value = "This is a string! It has three sentences. Right?"
    string.count_sentences()
    assert(string.count_sentences() == 3)