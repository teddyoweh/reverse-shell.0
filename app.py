import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clusters")
        self.geometry("400x300")

        # Create the menu
        menu = tk.Menu(self)
        self.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Clusters", menu=file_menu)

        # Add the "Create new cluster" option to the menu
        file_menu.add_command(label="Create new cluster", command=self.create_cluster)

    def create_cluster(self):
        # Create a new window
        cluster_window = tk.Toplevel(self)
        cluster_window.title("Create new cluster")
        cluster_window.geometry("300x200")

        # Add input fields for the cluster name, server IP, and port
        tk.Label(cluster_window, text="Cluster name:").pack()
        cluster_name = tk.Entry(cluster_window)
        cluster_name.pack()
        tk.Label(cluster_window, text="Server IP:").pack()
        server_ip = tk.Entry(cluster_window)
        server_ip.pack()
        tk.Label(cluster_window, text="Port:").pack()
        port = tk.Entry(cluster_window)
        port.pack()

        # Add a "Start" button to the window
        start_button = tk.Button(cluster_window, text="Start", command=self.start_cluster)
        start_button.pack()

    def start_cluster(self):
        # Get the values from the input fields
        cluster_name_value = cluster_name.get()
        server_ip_value = server_ip.get()
        port_value = port.get()

        # TODO: Start the cluster with the provided values

if __name__ == '__main__':
    app = App()
    app.mainloop()
