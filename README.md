# Streamlit 


> [Streamlit](https://streamlit.io) turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.


## Setup


### Clone the Repo (use this template)

---

1. In this GitHub repo, click on "Use this Template" (the green button at the top of this page)

---

2. Name the repo *streamlit-app*

---

3. In your GitHub-Account, click on the green **Code** button and select **Open with GitHub Desktop** to copy the *streamlit-app* repository to your local machine.


---


### Run the app


In your terminal (Mac) or Anaconda Command Prompt (Windows): 

---

- Step 1: `cd` into the *streamlit-app* folder (replace YOURPATH with your path to the folder streamlit-app)


```bash
cd YOURPATH/streamlit-app
```

---

- Step 2: install all needed Python libraries from the *environment.yml* file to create a virtual environment named *streamlit*:


```bash
conda env create -f environment.yml
```

---

- Step 3: Activate the *streamlit* environment:

```bash
conda activate streamlit
```

---

- Step 4: Change current directory (cd) into *1-first-app*


```bash
cd 1-first-app
```

---

- Step 5: Start the app:


```bash
streamlit run app.py
```


- *If asked for your e-mail, you can simply press enter (you don't need to provide this information)*


---

- Step 6: The command should open your browser and display the app. 


- *If your browser opened but only displays a blank screen (this may happen if you use Safari), copy the url and paste it in another browser (e.g., Chrome).*


---

### Start VS Code

---

- Step 7: Start Visual Studio Code and click on `Open Folder` in the Explorer. Select the `streamlit-app` folder.


---

- Step 8: In the VS Code Explorer, select `1-first-app` and open the file `app.py` (this is the code of the app)


- *While developing a Streamlit app, it's recommended to lay out your VS code editor and browser windows side by side, so the code and the app can be seen at the same time.* 

---

- Step 9: VS Code: In the code of app.py, change `st.title("My first App")` to `st.title("Hello World!")` and save the changes.  

---


- Step 10: Refresh your browser to display the changes.

---


- Step 11: If you are done, close the browser window, go to your terminal and stop your app with `Ctrl+C` (or simply close the terminal window).



---

---


## Guides

- Get familiar with the [main concepts](https://docs.streamlit.io/library/get-started/main-concepts)
 
- [API reference](https://docs.streamlit.io/library/api-reference)

- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

- [Layout](https://blog.streamlit.io/designing-streamlit-apps-for-the-user-part-ii/?utm_medium=email&_hsmi=200036447&_hsenc=p2ANqtz-_qSKsHsARDBJ3IdOcp5kzxhvmFIn4KBaC9-mLf2Gbu0PpToQUqZpdDlv7AWxrx0fiObeilulYthAZqC7QIdHBLTphUBg&utm_content=200036447&utm_source=hs_automation)


---

- App demo:

```bash
streamlit hello
```

---

![](https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4)

A [Streamlit demo](https://streamlit.io/gallery) to interactively visualize Uber pickups in New York City:

![](img/uber.png)
