# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the Cherry Leaves project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.



## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- List here your project hypothesis(es) and how you envision validating it (them).

- The available dataset contains 4208 images of healthy and powdery mildew containing leaves.

- We suspect powdery mildew contained leaves have clear marks/signs, typically the leaf is not so fresh and has discoloration and shows signs of a dying leaf. Small white spots on both the surface and the underside of leaves can be noticed, that can differentiate them from an healthy leaf. An Image Montage shows that typically a powdery mildew leaf has white spots across it. Average Image, Variability Image and Difference between Averages studies did not reveal any clear pattern to differentiate one from another.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

- **Business Requirement 1**: Data Visualization

  - We will display the "mean" and "standard deviation" images for healthy and powdery mildew contained leaves.
  - We will display the difference between an average healthy leaf and an powdery mildew contained leaf.
  - We will display an image montage for either healthy or owdery mildew contained leaves.

- **Business Requirement 2**: Classification
  - We want to predict if a given leaf is healthy or contains powdery mildew.
  - We want to build a binary classifier and generate reports.

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

### MalariaClf

- We want an ML model to predict if a given leaf is healthy or contains powdery mildew., based on historical image data. It is a supervised model, a 2-class, single-label, classification model.

???????
- Our ideal outcome is to provide the medical team a faster and more reliable diagnostic for malaria detection.
- The model success metrics are
  - Accuracy of 65% or above on the test set.
- The model output is defined as a flag, indicating if the cell has malaria or not and the associated probability of being infected or not. The medical staff will do the blood smear workflow as usual and upload the picture to the App. The prediction is made on the fly (not in batches).
- Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected and not infected cells. A blood smear sample is collected, mixed with a reagent and examined under the microscope. Visual criteria are used to detect malaria parasites. It leaves room to produce inaccurate diagnostics due to human error. On top of that, some specific hospital facilities with malaria centres need more, trained staff and expertise and are typically understaffed.
- The training data to fit the model come from the [National Institutes of Health (NIH) Website](https://ceb.nlm.nih.gov/repositories/malaria-datasets/). This dataset contains about 26+ thousand images. We have extracted a subset of 5643 images from this dataset and saved it to [Kaggle dataset directory](https://www.kaggle.com/codeinstitute/malaria-cell-classification/) for quicker model training.
  - Train data - target: infected or not; features: all images

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- [Numpy](https://numpy.org/) 
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [TensorFlow](https://www.tensorflow.org/)

## Credits

- The walthrough project, Malaria Detector project done by Code Institute has been the code that was used to learn how to build this website.
- The Malaria Detector project code has been used as the base and reference for building the NewsTok project. - [Malaria Detector](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/4565659a34d648b8b8edd063c3182180/)
- bootstrap documentation was used for bootstrap research and references. [bootstrap docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- Django documentation was used for Django research and references. [django docs](https://docs.djangoproject.com/en/5.0/)
- w3schools was used for general code concept searches. [w3schools](https://www.w3schools.com/)
- mdn web docs_ was used for general code concept searches. [mdn web docs_](https://developer.mozilla.org/en-US/)


### MEDIA
- Fonts used on the website. - [google fonts](https://fonts.google.com/) 
- Fonts used on the website. - [font awesome](https://fontawesome.com/)
- css used on the website. - [bootstrap](https://getbootstrap.com/)
- Wireframes were created using Lucidchart's online wireframe maker. - [lucid chart](https://www.lucidchart.com/pages)
- ERD models were also created using the Lucidchart's online ERD maker. - [lucid chart](https://www.lucidchart.com/pages)
- Images used on the website. - [pexels](https://www.pexels.com/)
- The logo used on the website was generated using IconGeneratorAI [icongeneratorai](https://www.icongeneratorai.com/)

### PROJECT SUPPORT
- I would like to thank my mentor Akshat Garg from Code Institute for his support, guidance, and help in planning and building this project.
- I would like to thank all the Code Institute tutors for their support, guidance, and help in solving code issues, debugging, and solving all technical issues faced in building this project.
- I would like to thank Code Institute for providing me with the necessary lessons and resources to help me build my skills to build this project.

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
