sizes = {svga:800,hd:1366,uhd:3840}
sizes.each do |key,value|
    puts "#{key}=>#{value}"
end

#shorter code
sizes = {svga:800,hd:1366,uhd:3840}
sizes.each { |key,value|puts "#{key}=>#{value}"}