
def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

print(DecimalToBinary(0x45))
print(DecimalToBinary(0x54))
print(DecimalToBinary(0x52))
print(DecimalToBinary(0x4f))
print(DecimalToBinary(0x41))
print(DecimalToBinary(0x49))
print(DecimalToBinary(0x45))
print(DecimalToBinary(0x44))
print(DecimalToBinary(0x52))
print(DecimalToBinary(0x47))
print(DecimalToBinary(0x46))
print(DecimalToBinary(0x41))
print(DecimalToBinary(0x53))
print(DecimalToBinary(0x4f))
