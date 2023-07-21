[![CI](https://github.com/Sherif-Elshafei/my-practice/actions/workflows/build-test-app.yml/badge.svg)](https://github.com/Sherif-Elshafei/my-practice/actions/workflows/build-test-app.yml)


## Introduction
Here I showcase my proficiency in developing a test automation pipeline.

This is an example of the combined practices of continuous integration (CI) and continuous delivery (CD). CI-CD is a subset of prcesses of the DevOps process. I cover the development processes circled in red in the following diagram.
![devops-png-9](https://github.com/Sherif-Elshafei/CI-CD/assets/4324447/49c86965-3444-4dde-9a8a-52b6562ae9a2)

## Usage (Python)
1. If you are going to use a self-hosted runner to wun this workflow then you will need to create a new self-hosted runner on your system (essentially make your system accessible to Github to run the code). In order to do that, you go to settings -> actions -> create a new runner -> follow the steps given. Whereas if you want to use another runner then you should modify the .yml file provided in this repository. Specifically, modify the values given to runs-on: to become ubuntu-22.04 or ubuntu-latest.
2. Write your production code and save it as *myFile*.py
3. Follow the guidelines provided in the example file to implement the unittest code and save it as test_*myFile*.py
4. Push both files to the main branch. If you want to push to another branch you will have to modify the .yml file provided.
