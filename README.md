# stat-315-final-project

Repository to hold necessary files for STAT-315 Final Project.

# Installation

Setting up the virtual environment:

1. Create a virtual environment with `python -m venv .venv`.
2. Activate the virtual environemnt.
3. Install the requirements via `pip install -r requirements.txt`.

In order to obtain the data used for this project, run `combine.py` to download and create the dataset. It is available at `./data/2023-divvy-tripdata.csv`.

# Running the Docker image from DockerHub

1. First pull the image from Docker Hub through the command:

```
docker pull p0kes/divvy_analysis

```

2. Then to run the container, the following command is used:

```
docker run -p 8888:8888 p0kes/divvy_analysis
```
