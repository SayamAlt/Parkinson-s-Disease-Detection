# Parkinson's-Disease-Detection

<p>We have started using data science to improve healthcare and services – if we can predict a disease early, it has many advantages on the prognosis. So in this data science project idea, we will learn to detect Parkinson’s Disease with Python. This is a neurodegenerative, progressive disorder of the central nervous system that affects movement and causes tremors and stiffness. This affects dopamine-producing neurons in the brain and every year, it affects more than 1 million individuals in India.</p>

![Symptoms of Parkinson's Disease](https://media.istockphoto.com/vectors/parkinsons-disease-symptoms-vector-id881702426)
![Parkinson's Disease Detection](https://data-flair.training/blogs/wp-content/uploads/sites/2/2019/10/Python-machine-learning-project-.png)

## Deployed Web Application

Link: [Parkinson's Disease Prediction](https://parkinson-disease-detection-sk.herokuapp.com/)

## Parkinson's Disease Data Set Description

<table>
  <tr>
    <th><b>Data Set Characteristics</b></th>
    <th><b>Multivariate</b></th>
  </tr>
  <tr>
    <td>Number of Instances</td> 
    <td>197</td>
  </tr>
  <tr>
    <td>Area</td>
    <td>Life</td>
  </tr>
  <tr>
    <td>Attribute Characteristics</td>
    <td>Real</td>
  </tr>
  <tr>
    <td>Number of Attributes</td>
    <td>23</td>
  </tr>
  <tr>
    <td>Date Donated</td>
    <td>2008-06-26</td>
  </tr>
  <tr>
    <td>Associated Task</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Missing Values?</td>
    <td>N/A</td>
  </tr>
</table>

<h1>Attribute Information</h1>

## Matrix column entries (attributes)
<table>
  <tr>
    <th><b>Attribute</b></th>
    <th><b>Meaning</b></th>
  </tr>
  <tr>
    <td>name</td> 
    <td>ASCII subject name and recording number</td>
  </tr>
  <tr>
    <td>MDVP:Fo(Hz)</td> 
    <td>Average vocal fundamental frequency</td>
  </tr>
  <tr>
    <td>MDVP:Fhi(Hz)</td> 
    <td>Maximum vocal fundamental frequency</td>
  </tr>
  <tr>
    <td>MDVP:Flo(Hz)</td>
    <td>Minimum vocal fundamental frequency</td>
  </tr>
  <tr>
    <td>MDVP:Jitter(%)</td>
    <td>Measure of variation in fundamental frequency</td>
  <tr>
    <td>MDVP:Jitter(Abs)</td>
    <td>Measure of variation in fundamental frequency</td>
  <tr>
    <td>MDVP:RAP</td>
    <td>Measure of variation in fundamental frequency</td>
  <tr>
    <td>MDVP:PPQ</td>
    <td>Measure of variation in fundamental frequency</td>
  <tr>
    <td>Jitter:DDP</td> 
    <td>Measure of variation in fundamental frequency</td>
  </tr>
  <tr>
    <td>MDVP:Shimmer</td>
    <td>Measure of variation in amplitude</td>
  <tr>
    <td>MDVP:Shimmer(dB)</td>
    <td>Measure of variation in amplitude</td>
  <tr>
    <td>Shimmer:APQ3</td>
    <td>Measure of variation in amplitude</td>
  <tr>
    <td>Shimmer:APQ5</td>
    <td>Measure of variation in amplitude</td>
  <tr>
    <td>MDVP:APQ</td>
    <td>Measure of variation in amplitude</td>
  <tr>
    <td>Shimmer:DDA</td>
    <td>Measure of variation in amplitude</td>
  </tr>
  <tr>
    <td>NHR</td>
    <td>Measure of ratio of noise to tonal components in the voice</td>
  <tr>
    <td>HNR</td> 
    <td>Measure of ratio of noise to tonal components in the voice</td>
  </tr>
  <tr>
    <td>status(Target variable)</td> 
    <td>Health status of the subject (one) - Parkinson's, (zero) - healthy</td>
  </tr>
  <tr>
    <td>RPDE</td>
    <td>Non-linear dynamical complexity measure</td>
  <tr>
    <td>D2</td> 
    <td>Non-linear dynamical complexity measure</td>
  </tr>
  <tr>
    <td>DFA</td> 
    <td>Signal fractal scaling exponent</td>
  </tr>
  <tr>
    <td>spread1</td>
    <td>Non-linear measure of fundamental frequency variation</td>
  <tr>
    <td>spread2</td>
    <td>Non-linear measure of fundamental frequency variation</td>
  <tr>
    <td>PPE</td>
    <td>Non-linear measure of fundamental frequency variation</td>
  </tr>
</table>

## Performance Summary of Machine Learning Models Used

<ul>
  <li>There are two models possessing the highest prediction accuracy, namely Random Forest Classifier and Support Vector Classifier, each of which have an accuracy score of nearly 89%.</li>
  <li>Logistic Regression model had the worst predictive performance, having an accuracy of a little more than 80%.</li>
</ul>


