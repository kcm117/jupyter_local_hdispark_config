# Configure Local Jupyter Notebook to work with HDInsight Spark Cluster

This script will configure Jupyter Notebook on a local windows machine to work with a HDInsight Spark Cluster (v3.5+) by adding necessary PySpark and PySpark3 Kernels.

## Prerequisites:
1) Install Anaconda
2) Open Anaconda Prompt
3) Install Jupyter Notebook - [Reference](https://docs.microsoft.com/en-us/azure/hdinsight/spark/apache-spark-jupyter-notebook-install-locally#install-jupyter-notebook-on-your-computer):
    ```
    conda install jupyter
    ```
4) Install SparkMagic - [Reference](https://docs.microsoft.com/en-us/azure/hdinsight/spark/apache-spark-jupyter-notebook-install-locally#install-the-kernels-and-spark-magic):

    ```
    pip install sparkmagic==0.11.2
    ```
5) Install ipywidgets - [Reference](https://github.com/jupyter-incubator/sparkmagic#installation):
	```
    jupyter nbextension enable --py --sys-prefix widgetsnbextension 
    ```
6) Locate your sparkmagic directory with ```pip show sparkmagic``` and cd to that location, e.g:
	````
    cd c:\users\<UserName>\appdata\local\continuum\anaconda3\lib\site-packages
    ````
7) Install the PySpark and PySpark3 Kernels:
    ```
    jupyter-kernelspec install sparkmagic/kernels/pysparkkernel
    jupyter-kernelspec install sparkmagic/kernels/pyspark3kernel
    ```

## Running the Script:

The script will prompt you to enter your cluster name and credentials.  It will use that information to generate the necessary config.json file for Jupyter.

1) In the Anaconda Command Prompt, change directory to wherever you cloned the repo, e.g.:
    ````
    cd C:\projects\jupyter_local_hdispark_config
    ````
2) Run the script:
    ````
    python config.py
    ````
    
 ## Using the Spark Context
 
 After configuration, new kernels should appear in Jupyter Notebook:
 
 ![alt text](https://github.com/kcm117/jupyter_local_hdispark_config/blob/master/screenshots/new_notebook.png?raw=true)
 