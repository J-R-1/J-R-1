# <b>Lung Disease Prediction</b>
<br>



<b>Application Demo:</b>
<hr/>
<div>
<img src="https://github.com/J-R-1/J-R-1/blob/main/Transfer%20Learning/Lung%20Disease%20Prediction/Screenshot%20(164).png" width="300" style="float: left;" />

<img src="https://github.com/J-R-1/J-R-1/blob/main/Transfer%20Learning/Lung%20Disease%20Prediction/Screenshot%20(165).png" width="300" style="float: left;" />

<img src="https://github.com/J-R-1/J-R-1/blob/main/Transfer%20Learning/Lung%20Disease%20Prediction/Screenshot%20(166).png" width="300" style="float: left;" />
</div>
<hr/>

<b>Overview:</b>
<hr />

Trasfer leraning is a machine learning method where the model developed for a task is reused at a starting point for a model on a second task. The <b>Lung disease Prediction</b> is an application developed based on this methodology. This application given a X-ray Image file predicts 
whether an Image belongs to one of the four given classes namely BacterialPneumonia, Covid-19, Normal or ViralPneumonia.<br/>

<b>Keras Applications</b> provides access to a number of top-performing pre-trained models along with the pretrained weights.
This project uses three of theses models <b>VGG16, InceptionV3 and ResNet50</b> for training. These models are widely used for transfer learning both because of their performance,
and also because they were examples that introduced specific architectural innovations, namely consistent and repeating structures (VGG), inception modules (GoogLeNet), and residual modules (ResNet).
<hr/>

<b>Data Source:</b>
<hr/>
This application uses <a href="https://www.kaggle.com/darshan1504/covid19-detection-xray-dataset/">Lung disease Prediction</a> datasets from Kaggle. The <b>'NonAugumented Train'</b> was used for traning the models and <b>'Val Data'</b> was used for validation and random images from <b>'Train Data'</b> were picked and used for testing the prediction results. 
<hr/>

<b>Technologies used:</b>
<hr/>
<ul>
   <li><b>Google Colab</b></li>
   <li><b>Keras</b></li>
   <li><b>Tensorflow=2.3.0</b></li>
   <li><b>numpy=1.18.5</b></li>
   <li><b>Matplotlib</b></li>
   <li><b>Streamlit</b></li>
   <li><b>pycharm</b></li>
 </ul>
 <hr/>


<b>Technical Aspect:</b>
<hr/>
This project is divided into two major parts.<br/>


1. Three notebooks one for each <b>VGG16, InceptionV3</b> and <b>ResNet50</b> were created to compare the models performance on the same dataset. These pre-trained models were used as a Feature Extractor and integrated into some classification layers to make the final prediction.<br/>
   Fine tuning was done on various parameters to improve the accuracy of the model. They are as follows:<br/> 
   <ul>
     <li> Number of layers in the pre-trained models to unfreeze.</li>
     <li> Number of layers and nodes to add in the classification layers.</li>
     <li> Learning rate.</li>
     <li> Optimizers (Adam or SGD).</li>
     <li> Number of Epochs.</li>
   </ul>
2. Building and hosting a <b>Streamlit</b> web app using <b>pycharm</b> IDE that shows the prediction of these models given an image file.
<hr/>


### <b>The Notebooks</b>
<br>


For the project <b>Lung Disease Classification</b>:
<br>

<ul>
   <li>Please refer <a href="https://github.com/J-R-1/J-R-1/blob/main/Transfer%20Learning/Lung%20Disease%20Prediction/LD_VGG16.ipynb">here</a> for complete implementation of the <b>VGG16</b> model.</li>
   <li>Please refer <a href="https://github.com/J-R-1/J-R-1/blob/main/Transfer%20Learning/Lung%20Disease%20Prediction/LD_Inceptionv3.ipynb">here</a> for complete implementation of the <b>Inceptionv3</b> model.</li>
   <li>Please refer <a href="https://github.com/J-R-1/J-R-1/blob/main/Transfer%20Learning/Lung%20Disease%20Prediction/LD_ResNet50%20(1).ipynb">here</a> for complete implementation of the <b>ResNet50</b> model.</li>

