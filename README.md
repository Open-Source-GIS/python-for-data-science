Python Data Science Install script
===========================
Get homebrew

```/usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.githubcom/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"```

brew doctor

brew install gfortran

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

Definitions
===========================
* Ensemble: 
    * In statistics and machine learning, ensemble methods use multiple models to  obtain better predictive performance than could be obtained from any of the constituent  
    models.  
    * A machine learning ensemble refers only to a concrete finite set of alternative models. An ensemble is a technique for combining many weak learners in an attempt to produce a strong learner. 
    * An ensemble is itself a supervised learning algorithm, because it can be trained and then used to make predictions. The trained ensemble, therefore, represents a single hypothesis. 
    * Ensembles tend to yield better results when there is a significant diversity among the models
    * Using a variety of strong learning algorithms, however, has been shown to be more effective than using techniques that attempt to dumb-down the models in order to promote diversity

* Random forest: 
