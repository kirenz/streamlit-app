# Streamlit 

[Streamlit](https://streamlit.io) turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.

![](https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4)

A [Streamlit demo](https://streamlit.io/gallery) to interactively visualize Uber pickups in New York City:

![](img/uber.png)


## Prerequisites

First, we need to ensure you have a recent version of [Anaconda](https://www.anaconda.com/products/distribution), [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniforge](https://github.com/conda-forge/miniforge) installed. Follow these instructions if you haven't already installed one of them on your system:

- [Anaconda installation](https://kirenz.github.io/codelabs/codelabs/anaconda-install/#0) (recommended)
- [Miniforge installation](https://kirenz.github.io/codelabs/codelabs/miniforge-setup/#0) 

If you already have Miniforge or Anaconda, we update it: 

- On *Windows* open the Start menu and open an Anaconda Command Prompt. On *macOS* or *Linux* open a terminal window:

```bash
conda update --all
```

## Download Repo

- In your terminal, `cd` into a folder you want to install this repo:

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

- Now we install all needed Python libraries from the `environment.yml` file to create a virtual environment named `streamlit`:

```bash
conda env create -f environment.yml
```

- Activate the `streamlit` environment:

```bash
conda activate streamlit
```

- cd into 1-first-app

```bash
cd 1-first-app
```

- Start the app:

```bash
streamlit run app.py
```

- While developing a Streamlit app, it's recommended to lay out your editor and browser windows side by side, so the code and the app can be seen at the same time. 

- Complete the code with the help of this [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet).

- If you are done, go to your terminal and stop your app with `Ctrl+C`


## Guides

- Get familiar with the [main concepts](https://docs.streamlit.io/library/get-started/main-concepts)
 
- [API reference](https://docs.streamlit.io/library/api-reference)

- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

- [Layout](https://blog.streamlit.io/designing-streamlit-apps-for-the-user-part-ii/?utm_medium=email&_hsmi=200036447&_hsenc=p2ANqtz-_qSKsHsARDBJ3IdOcp5kzxhvmFIn4KBaC9-mLf2Gbu0PpToQUqZpdDlv7AWxrx0fiObeilulYthAZqC7QIdHBLTphUBg&utm_content=200036447&utm_source=hs_automation)

- App demo:

```bash
streamlit hello
```

## GitHub

Note that if you want to synchronize your streamlit-app folder with GitHub, you should delete all existing git files:

- Show all hidden files in the folder ([Windows](https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-97fbc472-c603-9d90-91d0-1166d1d9f4b5), Mac: in Finder, press `Command` + `Shift` + `.` (period))
- Delete the folder `.git`and the file `.gitattributes` (if present)
- Now you can synchronize the folder with your own GitHub-Account
