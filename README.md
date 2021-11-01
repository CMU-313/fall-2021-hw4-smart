**API Documentation:**

Once the application has been deployed, the following line can be run to get outputs for applicants. (There are no pre-conditions for the service). A number for every feature must be provided since the API currently does not support missing variables.

curl http://localhost:5000/predict?studytime=[insert_score]&failures=[insert_score]&schoolsup=[insert_score]&famsup=[insert_score]&activities=[insert_score]&higher=[insert_score]&internet=[insert_score]&freetime=[insert_score]&Dalc=[insert_score]&Walc=[insert_score]&health=[insert_score]&absences=[insert_score]

In each of the brackets (“[insert_score]”), the command should be updated with the scores corresponding to the feature (ex: health=[insert_score] updated to health=5). For binary features, 0 means no, and 1 means yes. The section below outlines the possible score ranges for each feature.

The output would be a 1 if the student is considered a high-quality student and 0 otherwise.

This is an example of the model predicting 1: 
curl http://localhost:5000/predict?studytime=3&failures=0&schoolsup=0&famsup=1&activities=1&higher=1&internet=1&freetime=4&Dalc=1&Walc=1&health=4&absences=4

This is an example of the model predicting 0: 
curl http://localhost:5000/predict?studytime=3&failures=0&schoolsup=0&famsup=1&activities=1&higher=1&internet=1&freetime=4&Dalc=1&Walc=1&health=4&absences=92

If errors occur, try putting the URL in quotes before running it on the command line. The URL can also be directly inputted into the address bar in a browser.

**Feature Models and Performance:**

When training our model, we used the following features:
1. studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
2. failures - number of past class failures (numeric: n if 1<=n<3, else 4)
3. schoolsup - extra educational support (binary: yes or no)
4. famsup - family educational support (binary: yes or no)
5. higher - wants to take higher education (binary: yes or no)
6. Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
7. Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
8. freetime - free time after school (numeric: from 1 - very low to 5 - very high)
9. internet - Internet access at home (binary: yes or no)
10. health - current health status (numeric: from 1 - very bad to 5 - very good)
11. absences - number of school absences (numeric: from 0 to 93)
12. activities - extra-curricular activities (binary: yes or no)

Our new model performs better than the baseline model by incorporating more features. The baseline model only considered age, health, and absences, while our new model uses all of the above features. We also used cross-validation to retrain our model by first incorporating many new features and then using our testing test accuracy scores to determine if we were overfitting our model to the training data. After experimenting with these new features, we determined that the above set of features resulted in optimal test set accuracy scores.

While predicting G3 using G1 and G2 give more accurate models, we chose to build our model without using these predictors. We hope that this new model can be able to predict a student’s success in earlier years, without having collected data in early education. Then, perhaps being able to know the benefits of these covariates in early childhood can set students up for success in school earlier. 

We chose to use binary variables for educational support over variables such as parent education, because they gave better accuracy scores. We made the choice to leave out the remaining predictors to avoid potential overfitting and chose predictors that contributed to higher accuracy scores and seemed most relevant to student performance. 

When testing on a random training and testing set split, the baseline model performs with about a 77% accuracy on average and about a 20% F1 score. The retrained model has on average an 85% accuracy score and 35% F1 score. We determined these values by running both models multiple times on random training and testing data splits. The training set was 70% of the overall data and the testing set was 30%.

**Deployment Instructions:**

To deploy the application, the following commands should be run on the command line in the dockerfile directory.

docker build -t ml:latest .

docker run -d -p 5000:5000 ml

**Testing:**

For manual testing, we split our data into two sets: a training set and a testing set. The training set was 75 percent of the overall data and the testing set was 25 percent. We cross-validated our model using these separate sets by first training on the training set and then computing accuracy and f1 scores using the testing set. The testing set was used to approximate the overall accuracy of the model and how it would perform in a real-world setting.

For automated testing, we used Github Actions to set up a Docker workflow (Docker Image workflow). The workflow tests if the docker image is buildable. This ensures that the microservice is properly deployable.
