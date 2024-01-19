import concurrent.futures
import papermill as pm

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

with concurrent.futures.ThreadPoolExecutor() as executor:  # You can also use ProcessPoolExecutor for multiprocessing
    futures = [executor.submit(execute_notebook, pi, radius) for pi, radius in tasks]

concurrent.futures.wait(futures)
