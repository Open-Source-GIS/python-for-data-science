
/usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"

brew doctor

brew install gfortran

pip install numpy

to test installation of numpy...
import numpy
print numpy.__version__
print numpy.__file__
quit()

pip install scipy
to test installation of scipy...
import scipy
print scipy.__version__
print scipy.__file__
quit()

pip install -U scikit-learn

pip install ipython