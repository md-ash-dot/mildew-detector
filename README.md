# MILDEW DETECTOR


## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

1. - Healthy cherry leaves look fresh and green across the entire surface of leaf.
  - Created image monatge of healthy and powdery mildew containing cherry leaves.
  - Plotted a histogram of color values of average healthy and powdery mildew containing cherry leaves.

2. - Disntinct feautures in Variability of cherry leaves containing Powdery Mildew.
  - Displayed plot of mean and standard deviation of cherry leaves containing Powdery Mildew.

3. - Absence of white spots and discolouration in Variability of Healthy cherry leaves.
  - Displayed plot of mean and standard deviation of healthy cherry leaves.

4. - Patterns from difference between the averages of Healthy and Powdery Mildew containg cherry leaves helps to differentiate them.
  - Displayed plot of difference between mean healthy and mean powdery mildew cherry leaves.

5. - A Machine learning model can be created with the dataset provided to predict if a leaf contains powdery Mildew.
  - Created and trained a tensor flow CNN convolution neural network model.
  - Evaluated model performance for an accuracy of 99.76%.
  - Predicted successfully using the trained model on new data.


- The available dataset contains 4208 images of healthy and powdery mildew containing leaves.

- We suspect powdery mildew contained leaves have clear marks/signs, typically the leaf is not so fresh and has discoloration and shows signs of a dying leaf. Small white spots on both the surface and the underside of leaves can be noticed, that can differentiate them from an healthy leaf. An Image Montage shows that typically a powdery mildew leaf has white spots across it. Average Image, Variability Image and Difference between Averages studies did not reveal any clear pattern to differentiate one from another.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- **Business Requirement 1**: Data Visualization

1. The client wants to see average images and variability images for each class (healthy or powdery mildew).
  - We will display the "mean" and "standard deviation" images for healthy and powdery mildew contained leaves.
2. The client wants to see the differences between average healthy and average powdery mildew cherry leaves.
  - We will display the difference between an average healthy leaf and an powdery mildew contained leaf.
  - We will display the histogram of colour values of the average healthy leaf and powdery mildew contained leaf images. 
3. The client wants to see an image montage for each class.
  - We will display an image montage for either healthy or powdery mildew contained leaves.

- **Business Requirement 2**: Classification

1. The client wants an ML system that is capable of predicting whether a cherry leaf is healthy or contains powdery mildew. 
  - We will build a binary classifier Ml model and generate reports.
  - We will evaluate the performance of tge Ml model for loss and accuracy.
  - We will predict if a given leaf is healthy or contains powdery mildew on new data.

## ML Business Case

### Powdery Mildew detector

- We want an ML model to predict if a given leaf is healthy or contains powdery mildew, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
- Our ideal outcome is to provide Farmy & Foods, a faster and more reliable diagnostic for powdery mildew detection in cherry leaves to replace the currently used method of manually verifying samples.
- The criteria for the performance goal of the predictions has been agreed to an accuracy of 97%.
- The model output is defined as a flag, indicating if the leaf has powdery mildew or not and the associated probability of being affected or not. The Farmy & Foods staff will take a picture of a sample and upload it to the App. The prediction is made on the fly (not in batches).
- Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.
- The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.
- The training data to fit the model come from the [cherry_leaves kaggle dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves). This dataset contains a total of 4208 images for both healthy and powdery mildew contained cherry leaves. 
  - Train data - target: healthy or not; features: all images

## Cross Industry Standard Process for Data Mining (CRISP-DM)

CRISP-DM was used in developing this project.

### Business understanding

- Business case assessment provided by Code Institute.
- The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Data Understanding

- Data collection.
- Data from the Kaggle dataset was fetched and saved as raw data.

### Data Preparation

- Data cleaning: Check and remove non image files
- Split train validation set
- Set Image shape
- Average and variability of images per label
- Load image shapes and labels in an array 
- Plot and save mean variability of images per label
- Difference between average healthy and powdery mildew contained leaf
- Image montage 
- Image data augmentation

### Modelling

- Create model - Convolution Neural Network(CNN)
- Fit created ML model with train set 
- save model 

### Evaluation

- Plot model learning curve for model training loss and accuracy
- Evaluate model on test set
- Load random image to predict
- Convert image to array and prepare for prediction.
- Predict class probabilities and evaluate.

## Dashboard Design

- MENU
  - The menu is made using st.sidebar.radio. It displays all the available page of the dahsboard.
  - The pages of the dashboard can be accessed by selecting the radio button of the coressponding page.
  - The sidebar menu can be closed or opened at any time while using the dashboard.
  ![Menu](/dashboard_images/menu.png)

- PAGES ON DASHBOARD

  1. Quick Project Summary
    - The quick project summary pages helps in displaying a brief summary of the project. 
    - This page uses st.write and st.success to highlight the information of the page.
    ![Project Summary](/dashboard_images/summary.png)
    - General information of the project is listed.
    - Project Dataset information and the size of dataset is listed.
    - A link to this readme file is also listed for further information.  
    - Business requirements of the client are listed.

  2. Leaf Visualizer
    - The leaf visualizer page displays all the images of plots created to visualize the data.
    - This page uses st.checkbox to display the selected sections of the page and st.selectbox for the image montage section to select the class of cherry leaf.
    - This page uses st.warning to highlight information and st.image to display images.
    ![Leaf Visualizer](/dashboard_images/visualizer.png)
    - Difference between average and variability image shows the plot used to display the average and variability of the cherry leaves of the two classes.
    ![Variability](/dashboard_images/variability.png)
    - Differences between average healthy and average powdery mildew affected leaves plot is displayed.
    - Histogram of color values of average leaf image of both classes is displayed.
    - Image Montage displays a montage of the selected class.
    ![Image Montage](/dashboard_images/montage.png)

  3. Mildew Detection
    - This page displays an file uploader and displays the prediction after an upload along with a downloadable report.
    - This page uses st.write and st.info, st.success to highlight information.
    - This page uses st.file_uploader for the image uploader for prediction of cherry leaf samples.
    - This page uses st.table for the report and st.markdown for downloadable report.
    - Image uploader is used to upload the image to predict a sample leaf. Images of .png and .jpeg can be uploaded. Multiples images can be uploaded at the same time.
    ![Uploader](/dashboard_images/uploader.png)
    - Prediction is done after the image is uploaded and the prediction message is diplayed showing if the cherry leaf is healthy or not. It also shows the diagnostic graph of how it has predicted the sample image.
    ![Prediction](/dashboard_images/prediction.png)
    - Report of the prediction can be downloaded locally as a csv file and the analysis report is also displayed in the dashboard.
    ![Report](/dashboard_images/report.png)

  4. Project Hypothesis
    - This page uses st.write and st.success, st.info to highlight information on the page.
    - Hypothesises and validation are listed along with it's inferences.
    ![Hypothesis](/dashboard_images/hypothesis.png)

  5. Ml performace metrics
    - This page uses st.write and st.info to highlight information on the page.
    - This page uses st.image to display the images of the plots.
    - this page uses st.dataframe to display the test evaluation performance results.
    ![Ml performace metrics](/dashboard_images/metrics.png)
    - Average Image size in dataset is displayed using the image of the plot.
    - Train, Validation and Test Set: Labels Frequencies are displayed using the image of the barplot.
    - Sunburst nested pie plot - Train, Validation and Test Set: Labels Frequencies are displayed using the image of the sunburst plot.
    - Model History displays the Ml model learning curve.
    - Generalised Performance on Test Set displays the loss and accuracy performance figures.

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Dashboard Testing

Manual testing of the dashboard was carried out using the steps below.

### MENU 
- The menu sidebar radio buttons were tested to see if the coressponding pages loaded.
- The menu sidebar was tested by closing and opening it while using the dashboard.
#### QUICK PAGE SUMMARY
- The link to this readme file on the quick page summary page was tested.
- The general information and business requirements sections were checked to see if it was diplayed correctly.
### LEAF VISUALIZER
- All the checkboxes in the leaf visualizer pages were tested to see if it diplayed the inferences and images of the plots.
- The image montage section was tested to see if it diplayed the right image monatges when the healthy and powdery_mildew labels were selected and the create montage button was clicked.
### MILDEW DETECTION
- The business requirement information was checked to see if it was displayed correctly.
- The link to the dataset to get images to download for testing the model was tested .
- The image uploader was tested by uploading single and multiple images of .png and .jpeg formats.
- The prediction was tested to see if the prediction message was displayed along with the diagnostic plot of probability and analysis report.
- The link to download the report as csv was tested.
### PROJECT HYPOTHESIS
- The hypothesises , validations and inferenences were checked if it was displayed correctly.
- The Business requirements answered by the hypothesises were checked if it was displayed correctly.
### ML PERFORMANCE METRICS
- The Ml performace was checked to see if all images of plots were displayed.
- The inferences of the plots were checked if it was displayed correctly.
- The generalized performance on test dataframe was checked if it was displayed correctly.

## Deployment

### Heroku

- The App live link is: [Mildew Detector Live](https://powdery-mildew-detector-live-3a7db6791eea.herokuapp.com/)
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- [Numpy](https://numpy.org/) A Python library for numerical computations, facilitating efficient array operations and mathematical functions.
- [Pandas](https://pandas.pydata.org/) A Python library for data manipulation and analysis, offering powerful data structures and functions for working with structured data.
- [Matplotlib](https://matplotlib.org/) A Python library for creating static, interactive, and publication-quality visualizations, widely used for plotting graphs, charts, and histograms.
- [Seaborn](https://seaborn.pydata.org/) A Python library for statistical data visualization, built on top of Matplotlib, providing a high-level interface for creating attractive and informative statistical graphics.
- [Plotly](https://plotly.com/python/) A Python library for creating interactive and publication-quality visualizations, ranging from basic charts to complex dashboards.
- [TensorFlow](https://www.tensorflow.org/) A Python library for building and training machine learning models, offering flexibility and scalability for various tasks like deep learning, neural networks, and numerical computations.

## Softwares used

- [Python](https://www.python.org/) A versatile and powerful programming language used for web development, data analysis, artificial intelligence, scripting, and more.
- [Juputer Notebooks](https://jupyter.org/) An interactive computing environment that allows users to create and share documents containing live code, equations, visualizations, and narrative text, ideal for data exploration, analysis, and collaboration.
- [Streamlit](https://streamlit.io/) A Python library for building interactive web applications with simple Python scripts, enabling rapid prototyping and deployment of data-driven apps.

## Credits

- The walthrough project 1, Malaria Detector project done by Code Institute has been the code that was used to learn how to build this project.
- The Malaria Detector project code has been used as the base and reference for building the NewsTok project. - [Malaria Detector](https://github.com/Code-Institute-Solutions/WalkthroughProject01)
- The walkthrough project 2, Churnometer project done by Code Institute has been the code that was used to learn the concepts used in this project. [Churnometer](https://github.com/Code-Institute-Solutions/churnometer)


### MEDIA
- The images used in this project are from the cherry-leaves kaggle dataset provided by Code Institute - [cherry_leaves dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

### Content

- The Business case assessment were provided by Code Institute.
- Business Requirements were provided by Code Institute.
- The dataset used in this project is the cherry-leaves kaggle dataset provided by Code Institute - [cherry_leaves dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).


### PROJECT SUPPORT
- I would like to thank the Code Institute and all other members on the project-portfolio-5-predictive-analytics on slack for their support and guidance in building this project.
- I would like to thank my mentor Rohit Sharma from Code Institute for his support, guidance, and help in planning and building this project.
- I would like to thank all the Code Institute tutors for their support, guidance, and help in solving code issues, debugging, and solving all technical issues faced in building this project.
- I would like to thank Code Institute for providing me with the necessary lessons and resources to help me build my skills to build this project.

