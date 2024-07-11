def safe_divide(numerator, denominator) -> float:
    try:
        num = float(numerator)
        num2 = float(denominator)
        if denom != 0:
            return num / num2
        else:
            return "Error: Cannot divide by zero."       
    except ValueError:
        return "Error: Please enter numeric values only."
    
