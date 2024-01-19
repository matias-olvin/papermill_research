import papermill as pm
import ray
import time

ray.init()

@ray.remote
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

futures = [execute_notebook.remote(3.14, radius) for radius in range(1,10)]

ray.get(futures)