import multiprocessing
import os

def run_office_server():
    os.system("python OfficeServer.py")  # Runs OfficeServer on port 1234

def run_plant_server():
    os.system("python PlantServer.py")  # Runs PlantServer on port 4444

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_office_server)
    p2 = multiprocessing.Process(target=run_plant_server)

    p1.start()
    p2.start()

    print("Both servers are running...")

    p1.join()
    p2.join()
