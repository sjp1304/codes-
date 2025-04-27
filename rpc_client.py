import xmlrpc.client

def main():
    # Connect to the server
    server = xmlrpc.client.ServerProxy("http://localhost:9000/")
    
    try:
        # Input from the user
        num = int(input("Enter an integer to calculate its factorial: "))
        
        # Call the remote function
        result = server.factorial(num)
        
        # Display the result
        print(f"The factorial of {num} is: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


