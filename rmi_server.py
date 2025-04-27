import Pyro4

# Define a class with the remote method
@Pyro4.expose
class StringConcatenator:
    def concatenate(self, str1, str2):
        return str1 + str2

# Start the Pyro4 daemon and register the object
def main():
    daemon = Pyro4.Daemon()                   # Create a Pyro daemon
    ns = Pyro4.locateNS()                     # Find the name server
    uri = daemon.register(StringConcatenator) # Register the class as a Pyro object
    ns.register("example.concat", uri)        # Register the object with a name
    print("Server is ready. URI:", uri)
    daemon.requestLoop()                      # Start the event loop

if __name__ == "__main__":
    main()
