from dask import delayed, compute
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

@delayed
def delayed_execute_notebook(pi, radius):
    execute_notebook(pi=pi, radius=radius)


tasks = [delayed_execute_notebook(3.14, radius) for radius in range(1,10)]

start_time = time.time()

results = compute(tasks)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")