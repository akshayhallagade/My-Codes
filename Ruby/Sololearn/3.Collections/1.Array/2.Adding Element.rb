############## <<,insert ##################
#Array can have different types of elements.

arr=[5,"Dave",15.88,false]  

puts "....."
puts arr[0]          #
puts arr[1]          #  printing elements of array.
puts arr[-1]         #
puts "....."

#addidng new elements to array. This will add item at the last.
arr << 8             #  << is used to add the items in the list.
puts arr

#to insert a element at a required position.
arr.insert(2,8)      #  Here, 8 is inserted at 2 position.
puts "....."
puts arr
puts "....."
