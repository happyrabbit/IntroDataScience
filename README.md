This is for the book **Practitioner's Guide to Data Science** (The previous name was "Introduction to Data Science")
- You can access the free online version [here](http://scientistcafe.com/IDS/). Alternatively, you can purchase physical copies from [Amazon](https://www.amazon.com/Practitioners-Guide-Data-Science-Chapman/dp/0815354398/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=) or [Routledge](https://www.routledge.com/Practitioners-Guide-to-Data-Science/Lin-Li/p/book/9780815354390).

<center>
<img 
      style="width: 50%;"
     src="https://scientistcafe.com/ids/cover.png" />
</center>

Please note that this work is written under the [Contributor Code of Conduct](https://github.com/happyrabbit/IntroDataScience/blob/master/CONDUCT.md) and released under the [CC-BY-NC-SA license](https://creativecommons.org/licenses/by-nc-sa/3.0/us/). By participating in this project, for example, by submitting a [pull request](https://github.com/happyrabbit/IntroDataScience/issues) with suggestions or edits, you agree to abide by its terms.

## Goal of the Book

This book focuses on data science with an emphasis on industrial experience. It covers a cross-disciplinary subject, combining hands-on experience and problem-solving in a business context. Most introductory books on data science discuss modeling techniques and implementation using R or Python but lack the industrial context. This book seeks to fill that gap by exploring the art of data science in practice.

Some key features of this book are as follows:

- It covers both technical and soft skills.

- It has a chapter dedicated to the big data cloud environment. In the industry, the practice of data science is often in such an environment.

- It is hands-on. We provide the data and **repeatable** R and Python code in notebooks. Readers can repeat the analysis in the book using the data and code provided. We also suggest that readers modify the notebook to perform their analyses with their data and problems whenever possible. The best way to learn data science is to do it!

- It focuses on the skills needed to solve real-world industrial problems rather than an academic book.


**Notebooks**

| Chapter | R | Python |
| :--- | :---: | :---: |
| Ch4: Big Data Cloud Platform | [html](https://scientistcafe.com/ids/r/ch4), [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch4.Rmd) | [Create Spark Data](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/LoadDatasetSpark.ipynb), [`pyspark` Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/PysparkETL.ipynb)  |
|Ch5: Data Preprocessing | [html](https://scientistcafe.com/ids/r/ch5), [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch5.Rmd) | [Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/DataPreprocessing.ipynb) |
|Ch6: Data Wrangling |  [html](https://scientistcafe.com/ids/r/ch6),  [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch6.Rmd) | [Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/DataWrangling.ipynb) |
|Ch7: Model Tuning Strategy |  [html](https://scientistcafe.com/ids/r/ch7), [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch7.Rmd) |  [Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/Model_Tuning_Strategy.ipynb) |
|Ch8: Measuring Performance | [html](https://scientistcafe.com/ids/r/ch8), [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch8.Rmd) | [Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/Measuring_Performance.ipynb) |
|Ch9: Regression Models | [html](https://scientistcafe.com/ids/r/ch9), [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch9.Rmd) | [Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/Regression_Models.ipynb) |
|Ch10: Regularization Methods | [html](https://scientistcafe.com/ids/r/ch10), [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/ch10.Rmd) | [Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/Regularization_Methods.ipynb) |
|Ch11: Tree-Based Methods | [html](https://scientistcafe.com/ids/r/ch11), [rmd](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/ch11.Rmd) |  [Notebook](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/TreeBasedModels.ipynb) |
|Ch12:  Deep Learning | html([DNN](https://scientistcafe.com/ids/r/ch12dnn),  [CNN](https://scientistcafe.com/ids/r/ch12cnn), [RNN](https://scientistcafe.com/ids/r/ch12rnn) ) , rmd ( [DNN](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch12DNN.Rmd), [CNN](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch12CNN.Rmd), [RNN](https://raw.githubusercontent.com/happyrabbit/linhui.org/gh-pages/IDS/R/Ch12RNN.Rmd) ) | [DNN](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/FFNN.ipynb), [CNN](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/CNN.ipynb), [RNN](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/RNN.ipynb), [Tokenizing and Padding](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/TokenizingPadding.ipynb), [MINST with one hidden layer: step by step](https://github.com/happyrabbit/IntroDataScience/blob/master/Python/MINST_with_one_hidden_layer.ipynb) |

## How to run R and Python code

**Use R code.** You should be able to repeat the R code in your local R console or RStudio in all the chapters except for [Chapter 4](https://scientistcafe.com/ids/bigdatacloudplatform.html). The code in each chapter is self-sufficient, and you don't need to run the code in previous chapters first to run the code in the current chapter. For code within a chapter, you do need to run from the beginning.  At the beginning of each chapter, there is a code block for installing and loading all required packages. We also provide the `.rmd` notebooks that include the code to make it easier for you to repeat the code.  

To repeat the code on [big data and cloud platforms](https://scientistcafe.com/ids/bigdatacloudplatform.html), you need to use Databricks, a cloud data platform. We use Databricks because:

- It provides a user-friendly web-based notebook environment that can create a Spark cluster on the fly to run R/Python/Scala/SQL scripts
- It has a free community edition that is convenient for teaching purpose

Follow the instructions in [section 4.3](https://scientistcafe.com/ids/cloudenvironment) on the process of setting up and using the spark environment.

**Use Python code.** We provide python notebooks for all the chapters on GitHub. Like R notebooks, you should be able to repeat all notebooks in your local machine except for Chapter 4 with reasons stated above. An easy way to repeat the notebook is to import and run in Google Colab. To use Colab, you only need to log in to your Google account in Chrome Browser. To load the notebook to your colab, you can do any of the following:

- Click the ''Open in Colab" icon on the top of each linked notebook using the Chrome Brower. It should load the notebook and open it in your Colab. 

- In your Colab, choose File -> Upload notebook -> GitHub. Copy-paste the notebook's link in the box, search, and select the notebook to load it.
    
To repeat the code for big data, like running R notebook, you need to set up Spark in Databricks. Follow the instructions in [section 4.3](https://scientistcafe.com/ids/cloudenvironment) on the process of setting up and using the spark environment. Then, run the "Create Spark Data" notebook to create Spark data frames. After that, you can run the pyspark notebook to learn how to use `pyspark`. 

Short links:

- https://raw.githubusercontent.com/happyrabbit/DataScientistR/master/Data/SegData.csv to http://bit.ly/2P5gTw4
- https://raw.githubusercontent.com/happyrabbit/DataScientistR/master/Data/AirlineRating.csv to http://bit.ly/2TNQ6TK
- https://raw.githubusercontent.com/happyrabbit/DataScientistR/master/Data/sim1_da1.csv to http://bit.ly/2KXb1Qi
- https://raw.githubusercontent.com/happyrabbit/DataScientistR/master/Data/topic.csv to http://bit.ly/2zam5ny
