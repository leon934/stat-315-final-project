# Use a stable Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file first for caching
COPY requirements.txt .

# Install dependencies WITH version control
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy everything else (notebook, data, etc.)
COPY data_analysis.ipynb .
COPY combine.py .
COPY README.md .

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter when container runs
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
