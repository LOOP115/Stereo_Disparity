# Stereo Disparity

### [Specification](resources/final-spec.pdf)



### Introduction

Stereo matching is the problem of finding correspondences between two images that are taken simultaneously from two cameras that are mounted so that they are parallel and separated along their x-axis. The output of stereo matching is a disparity image that, for every pixel in the left image (x), indicates how many pixels to the left its correspondence (x’) is in the right image, giving the disparity (x-x’).

* **Due: 7pm, 21 Oct 2022**
* **Source code and written report (as .pdf)**



### Tasks

* To calculate a disparity map for the left image using classical (non deep learning) methods. You should create an image of floating point numbers that estimate the disparity (x-x’) for every pixel in the left image.

* To calculate some statistics using supplied ground truth depth images like the one below (crudely recoloured for this document to show the disparity as a heat map):
  * The rms (root mean squared) error between the values in your disparity map and those in the ground truth
  * The fractions of pixels with errors less than 4, 2, 1, 0.5 and 0.25 pixels
  * The runtime of your algorithm in seconds per image

The ground truth file is a 16 bit png where the value it contains is 256 * disparity (so that it can represent sub-pixel precision). It does not have disparity values for every pixel, where the disparity is absent, the number zero is given. You should restrict your statistics calculations to pixels for which there are valid depths.



### Approach and considerations

How you approach this problem is up to you - but you may wish to start with the methods discussed in lecture 13. You may also wish to consider:

* What matching function should you use? SSD and NCC were described in the lecture, can you develop others that will improve performance?
* How big should the window size be?
* Are all pixels in the matching window equally important?
* How are you going to get sub-pixel accuracy?
* Can you improve performance by encouraging a smooth output?
* How can you accelerate the process so that you don’t have to loop over every pixel in python (perhaps by using tensor operations in numpy, pytorch or tensorflow)?

Note that these are only suggestions to help you get started; you are free to use your own ideas.

Whatever methods you choose, you are expected to **evaluate these methods using the provided data**, to critically analyse the results, and to justify your design choices in your final report. Your evaluation should include error analysis, where you attempt to understand where your method works well and where it fails.

You are encouraged to use existing computer vision libraries in your implementation. However, your method should be your own; **you may not use library functions that solve the depth or disparity problem**, even if you then build on top of these functions.



### Dataset

* The dataset is curated from https://drivingstereo-dataset.github.io

* The images have been renamed so that they have the form:
  * <something>-left.jpg
  * <something>-right.jpg
  * <something>-disparity.png
* The left and right images are 8 bit rgb images. 
* The disparity images are 16 bit monochrome images.



### Submission

#### Code

* Your code submission should include your model code, a readme file that explains how to run your code, and any additional files we would need to recreate your results.
* You should not include the provided images in your code submission, but your readme file should explain where your code expects to find these images.

#### Report

* Your written report should be a .pdf that includes the description, analysis, and comparative assessment of the method(s) you developed to solve this problem.
* The report should follow the style of a short conference paper with no more than four A4 pages of content (excluding references, which can extend to a 5th page).
* The report should follow the style and format of an IEEE conference short paper. The IEEE Conference Template for Word, LaTeX and Overleaf is available here: https://www.ieee.org/conferences/publishing/templates.html
* Your report should explain the design choices in your method and justify these based on your understanding of computer vision theory.
* You should explain the experimentation steps you followed to develop and improve on your basic method, and report your final evaluation result.
* Your method, experiments, and evaluation results should be explained in sufficient detail for readers to understand them without having to look at your code.
* You should include an error analysis which assesses where your method performs well and where it fails, provide an explanation of the errors based on your understanding of the method, and give suggestions for future improvements.
* Your report should include tables, graphs, figures, and/or images as appropriate to explain and illustrate your results.





