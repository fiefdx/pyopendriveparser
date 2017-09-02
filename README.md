
# OpenDRIVE file parser

Parser for files in OpenDRIVE format, offers additional functions to navigate through the road network

## Install

```bash

sudo pip install --process-dependency-links https://github.com/stefan-urban/pyopendriveparser/archive/master.zip

```

## Example usage

```bash

# Setup Python virtual environment
mkdir newfolder && cd newfolder

python -m venv .
source bin/activate

pip install numpy lxml
pip install https://github.com/stefan-urban/pyeulerspiral/archive/master.zip

# Clone repository either with git ...
git clone git@gitlab.lrz.de:ga65xap/pyopendriveparser.git
# ... or HTTPS ...
git clone https://gitlab.lrz.de/ga65xap/pyopendriveparser.git

cd pyopendriveparser

# Add repository root directory to python path
export PYTHONPATH=$PYTHONPATH:`pwd`

# Get sample file from opendrive.org
wget http://opendrive.org/tools/Roundabout8Course.zip
unzip -j "Roundabout8Course.zip" "Roundabout8Course/Roundabout8Course.xodr"
rm Roundabout8Course.zip

python tests/read_xodr.py /../Roundabout8Course.xodr

if [ $? -eq 0 ]
then
   echo "Test passed!"
else
   echo "Test failed!"
fi

```