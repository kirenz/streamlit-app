# Streamlit 

## Setup

First, we need to ensure you have a recent version of **Anaconda** installed: 

- If you don't have Anaconda, follow this [Anaconda installation tutorial](https://kirenz.github.io/codelabs/codelabs/anaconda-install/#0). 

- If you already have Anaconda, we update it: On *Windows* open the Start menu and open an Anaconda Command Prompt. On *macOS* or *Linux* open a terminal window:


```bash
conda update --all
```

- In your terminal: `cd` into a folder you want to install this repo:

```bash
cd your-path
```


- Clone the repository containing all code:

```bash
git clone https://github.com/kirenz/streamlit-app
```

- cd into the streamlit-app folder

```bash
cd streamlit-app
```

- Now we install all needed Python libraries from the `environment.yml` file to create a virtual environment named `streamlit`. This includes the latest version of Streamlit and further libraries we need: 

```bash
conda env create -f environment.yml
```

- Activate the `streamlit` environment:

```bash
conda activate streamlit
```

## Main concepts

- Get familiar with the [main concepts](https://docs.streamlit.io/library/get-started/main-concepts)
 
