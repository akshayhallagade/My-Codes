#also, leave off parentheses.
def sum x,y
    puts x+y
end

sum 6,9

#program of o/p greetings.
def greet(name="")
    if name==""
        puts "Greetings!"
    else
        puts "Welcome,#{name}"
    end 
end

greet(gets.chomp)