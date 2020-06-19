######### pop, delete_at #########
# pop:Removes last element of array.
arr = [1,2,3]
arr.pop

puts arr   # gives each element one by one.
print arr  # gives whole bracket in output.

#delete_at : use to remove specific element.
arr=[2,4,6,8]
arr.delete_at(2)
print arr  #index starts counting at zero(0) so number at index(2) is 6.