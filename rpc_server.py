from xmlrpc.server import SimpleXMLRPCServer
import math

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(n)

# Create and configure server 
server = SimpleXMLRPCServer(("localhost", 9000), logRequests=True) 
print("Server started on port 9000...") 
# Register the factorial function 
server.register_function(calculate_factorial, "factorial") 
# Run the server 
try: 
    server.serve_forever() 
except KeyboardInterrupt: 
    print("\nServer shutting down.")



 
 
# # Set up the server
# def start_server():
#     server = SimpleXMLRPCServer(("localhost", 8000))
#     print("Server is running on port 8000...")
    
#     # Register the function
#     server.register_function(calculate_factorial, "factorial")
    
#     # Keep the server running
#     server.serve_forever()

# if __name__ == "__main__":
#     start_server()


## factorial 
# def factorial(n): 

#     if n < 0: 
#         return "Error: Factorial of a negative number is undefined." 
#     elif n == 0 or n == 1: 
#         return 1 
#     else: 
#         result = 1 
#         for i in range(2, n + 1): 
#             result *= i 
#         return result