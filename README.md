Python Data Science Install script
===========================
Get homebrew

```/usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.githubcom/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"```

```brew doctor```

```brew install gfortran```

```pip install numpy```

To test installation of numpy...
``` 
import numpy
print numpy.__version__
print numpy.__file__
quit()
```

```pip install scipy```  

To test installation of scipy...
```python
import scipy
print scipy.__version__
print scipy.__file__
quit()
```

```pip install -U scikit-learn```

```pip install ipython```


Octave installtion
```otool -L libfreetype.6.dylib```
```cp /Applications/Gnuplot.app/Contents/Resources/lib/libfreetype.6.dylib /Applications/Gnuplot.app/Contents/Resources/lib/libfreetype.6.dylib.orig```
```cp libfreetype.6.dylib /Applications/Gnuplot.app/Contents/Resources/lib/```

Definitions
===========================
* Ensemble: 
    * In statistics and machine learning, ensemble methods use multiple models to  obtain better predictive performance than could be obtained from any of the constituent  
    models.  
    * A machine learning ensemble refers only to a concrete finite set of alternative models. An ensemble is a technique for combining many weak learners in an attempt to produce a strong learner. 
    * An ensemble is itself a supervised learning algorithm, because it can be trained and then used to make predictions. The trained ensemble, therefore, represents a single hypothesis. 
    * Ensembles tend to yield better results when there is a significant diversity among the models
    * Using a variety of strong learning algorithms, however, has been shown to be more effective than using techniques that attempt to dumb-down the models in order to promote diversity

* Feature extraction: 
    * In pattern recognition and in image processing, feature extraction is a special form of dimensionality reduction.
    * When the input data to an algorithm is too large to be processed and it is suspected to be notoriously redundant (e.g. the same measurement in both feet and meters) then the input data will be transformed into a reduced representation set of features 

* Feature extraction:
    * In machine learning and statistics, feature selection, also known as variable selection, feature reduction, attribute selection or variable subset selection, is the technique of selecting a subset of relevant features for building robust learning models.
    * Feature selection is a particularly important step in analyzing the data from many experimental techniques in biology, such as DNA microarrays, because they often entail a large number of measured variables (features) but a very low number of samples.

* Random forest: 
    * Is an ensemble classifier that consists of many decision trees and outputs the class that is the mode of the classes output by individual trees.
    * It is one of the most accurate learning algorithms available. For many data sets, it produces a highly accurate classifier
    * It runs efficiently on large databases, handle thousands of input variables without variable deletion
    * Disadvantage: Random forests have been observed to overfit for some datasets with noisy classification/regression tasks, are difficult for humans to interpret.

 * Evaluation Function: You'll always need some kind of evaluation function to determine how your models are performing.
 
 * Cross-validation is a simple technique that basically grabs a chunk of the training data and holds it in reserve while the model is trained on the remainder of the data set. 