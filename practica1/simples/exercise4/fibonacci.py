def fibonacci(n):
    i = 0
    j = 1

    while i < n:
        i = j
        j = i + j

    return j

readableFile = open("./simples/exercise4/fileWithNumber.txt")
content = int(readableFile.read())

print("Content of the file:", content)

result = str(fibonacci(content))

writableFile = open("./simples/exercise4/result.txt", "a+")
writableFile.write(result)