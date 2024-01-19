import concurrent.futures
import papermill as pm
import time

def execute_notebook(pi, radius):
    parameters = {
        "pi": pi,
        "radius": radius,
    }

    pi_label = str(pi).replace(".", "_")
    radius_label = str(radius)

    pm.execute_notebook(
        "./main.ipynb",
        f"./output/output-notebook-{pi_label}-{radius_label}.ipynb",
        parameters=parameters,
    )

tasks = []
for x in range(1,10):
    pi, radius = [3.14, x]
    task = (pi, radius)
    tasks.append(task)

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:  # You can also use ProcessPoolExecutor for multiprocessing
    futures = [executor.submit(execute_notebook, pi, radius) for pi, radius in tasks]

concurrent.futures.wait(futures)


end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")