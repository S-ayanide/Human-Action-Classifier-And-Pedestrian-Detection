# Human Action Classifier And Pedestrian Detection

This algorithm could be used in any type of camera in a store which will help detect suspicious behaviour and alert the owner about theft.

# Dependencies

* Python >= 3.5
* Opencv >= 3.4.1
* Tensorflow 2.0.0
* Scikit-learn 0.22.1
* Keras 2.3.1
* Numpy 1.18.1
* Sliding Window 0.0.13
* Scipy 1.4.1
* Pathlib 1.0.1

## Setting up a Virtual Environment

### Using Pip

[virtualenv](https://packaging.python.org/key_projects/#virtualenv) is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

* **Installing a virtual environment**

  On macOS and Linux:
  ```bash
  python3 -m pip install --user virtualenv
  ```
  On Windows:
  ```cmd
  py -m pip install --user virtualenv
  ```

* **Creating a virtual environment**

  To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace `venv` with `virtualenv` in the below commands.

  On macOS and Linux:
  ```bash
  python3 -m venv <Your_Virtual_Environment>
  ```
  On Windows:
  ```cmd
  py -m venv <Your_Virtual_Environment>
  ```

* **Activating a virtual environment**

  Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s `PATH`.

  On macOS and Linux:

  `source venv/bin/activate` *or* `source <Your_Virtual_Environment>/bin/activate`

  On Windows:
  
  `.\venv\Scripts\activate` *or* `.\<Your_Virtual_Environment>\Scripts\activate`

**To install the required packages, run `pip install -r requirements.txt`**

### Using Conda

* On Windows open the Start menu and open an Anaconda Command Prompt. On macOS or Linux open a terminal window. Use the default bash shell on macOS or Linux.

* Choose a name for your TensorFlow environment, such as “tensorflow-env”.

* Install the current release of CPU-only TensorFlow:
  ```cmd
  conda create -n <Your_Virtual_Environment> tensorflow
  conda activate <Your_Virtual_Environment>
  ```
**To install the required packages, run `conda install -c anaconda requirements.txt`**

## Usage

Download the openpose VGG tf-model with command line `./download.sh`(/Online-Realtime-Action-Recognition-based-on-OpenPose/Pose/graph_models/VGG_origin) or fork [here](https://www.instagram.com/s_ayanide/), and place it under the corresponding folder

* ### Using Pip

  To start the webcam directly from your command prompt or PowerShell window, type `python main.py` after navigating to the `Online-Realtime-Action-Recognition-based-on-OpenPose/` folder.
  You can choose to test video with command `python main.py --video=test.mp4`

* ### Using Conda Env

  To run this project on a conda setup, open `main.py` from an anaconda supported IDE, preferably `spyder` and run the file either by clicking the play button or `Ctrl+A and Shift+enter`

You can choose different openpose pretrained model in `Script`.
**VGG_origin:** training with the VGG net, as same as the CMU providing caffemodel, more accurate but slower
**mobilenet_thin:** training with the Mobilenet, much smaller than the origin VGG, faster but less accurate.
However, Please attention that the Action Dataset in this repo is collected along with the VGG model running.

## Component Breakdown

This application could be broken down into three categories -

* ### Emotion Detection

  It can detect human emotions of all the customers and give an automated overall happiness rating to the store. Some Screenshots of the live application can be found below.

  <img src="./Screenshots/Neutral.PNG" height="300px" width="300px" /> <img src="./Screenshots/Happy.PNG" height="300px" width="300px" /> <img src="./Screenshots/Surprise.PNG" height="300px" width="300px" />

* ### Pedestrian Detection

  Yet to be done 😔

* ### Body Language Detection

  Yet to be done 😔

## Activity Diagram

<img src="./ActivityDiagram1.png" height="500px" width="500px" />

### Dataset Used

Haarcascades :- [Dataset](https://drive.google.com/open?id=1YmAJaR06jrQsIS5ixd3gMsKTL7JhLuVa)
*Download this and paste it at the root of the project*

## Others

Change the number of classes according to you.
Do Experiment with different pre-trained models.

Enjoy Deep Learning.
