#tempconv

# Prompt user for temperature to convert and read the supplied value

degreesF = float ( input ( " Enter the temprature in F "))

# perform the conversion 

degreesC = 5/9 * ( degreesF - 32 )

# Result 

print ( degreesF , " degreesF = ", degreesC , "degress C")