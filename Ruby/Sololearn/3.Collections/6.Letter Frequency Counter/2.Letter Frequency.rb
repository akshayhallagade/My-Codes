#a simple text
text = "I am learning Ruby and it is fun!"
text.downcase!  #downcase used to convert all strings into lowercase.

freqs = {}
freqs.default = 0

text.each_char {|char| freqs[char]+=1}

("a".."z").each {|x| puts "#{x}:#{freqs[x]}"}
