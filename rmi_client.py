#import Pyro4

# def main():
#     # Lookup the object in the name server
#     uri = "PYRONAME:example.concat"
#     concatenator = Pyro4.Proxy(uri)  # Create a proxy for the remote object

#     str1 = input("Enter first string: ")
#     str2 = input("Enter second string: ")
    
#     result = concatenator.concatenate(str1, str2)
#     print("Concatenated result:", result)

# if __name__ == "__main__":
#     main()

import Pyro4
uri ="PYRONAME:example.concat"
concatenator = Pyro4.Proxy(uri) 
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = concatenator.concatenate(str1, str2)
print("Concatenated String:", result)
