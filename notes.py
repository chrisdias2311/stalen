# 4. To build a Java Project (With and without parameters) using
# Jenkins
# New Item -> Free style project -> Add build Steps -> Windows batch command -> Enter the
# following commands
# cd /d path
# Javac Filename.java
# Java Filename %parameter1% %parameter2%
# Apply -> Save -> Build now -> Console output



# 5. To implement windows batch command on a project in Jenkins
# (with and without parameters)
# New item -> Freestyle project -> Add Build Steps -> Windows Batch Command -> In the box
# enter (echo “Hello World”) -> Build Now -> Console Output
# Check This project is parameterized



# Exp 6: To build anY Python project in Jenkins
# New Item -> Free style project -> Add build Steps -> Python Script -> Enter some Code -> Build



# Exp 7: To build a Maven and Ant project in Jenkins
# Maven
# New Item -> Maven Project -> Create -> (Source code management) Select Git ->
# *Note* Maven Ant & Gradle works explicitly -> Fork a Repo on github (darkleon/HelloWorld)
# -> Enter the cloning url ->
# Scroll down to Build -> Goals & Options -> clean compile test -> Apply -> Save -> Build Now

# Ant
# New Item -> Maven Project -> Create -> (Source code management) Select Git -> Build steps
# -> select Invoke Ant -> Ant Version -> Ant -> (Targets = clean compile package) -> Build now ->
# Open console output -> Scroll dwn and copy the path ->
# -> Open cmd -> execute: dir
# C:\ProgramData\Jenkins\.jenkins\workspace\act7.2\target\roshambo.war




# 8. To create a pipeline script and build a pipeline of jobs in
# Jenkins
# New Item -> Pipeline -> Create -> Enter some definition -> Scroll down to Pipeline -> Select
# pipeline script -> Enter script -> Build Now

# pipeline{
# agent any
# stages{
# stage ('Plan phase'){
# steps{
# echo 'Hi. This is Shree Jaswal'
# }
# }
# stage ('code phase'){
# steps{
# input('Do you want to continue?')
# }
# }
# stage ('integrate phase'){
# when{
# not{
# branch "master"
# }
# }
# steps {
# echo 'Integration test passed'
# }
# }
# stage ('testing phase'){
# parallel{
# stage ('unit test'){
# steps{
# echo 'running unit test'
# }
# }
# }
# }
# }
# }





# 9. To create a Jenkinsfile in a repository on GitHub and build a pipeline of
# jobs in Jenkins
# New Item -> Pipeline project -> Check Github hook trigger for GITScm polling -> Pipeline ->
# Pipeline script from SCM -> (SCM) GIT ->
# https://github.com/chrisdias2311/jenkins-pipeline-tutorial.git -> Script path ->
# hello-world/Jenkins -> Apply -> Save -> Build






# 10. To create a Jenkinsfile in a repository on GitHub and build a
# pipeline of jobs in Jenkins
# First fork a repo -> https://github.com/chrismld/jenkins-pipeline-tutorial ->
# New Item -> Pipeline -> Create -> Enter some description -> Scroll doen to pipeline -> Select
# pipeline from SCM -> In SCM select Git -> Enter Git URL -> Apply and Save -> Build Now
# Once build is successful -> Go to github -> Setting -> Left panel search for webhooks -> Add
# webhook
# Go to ngrok website -> Download Windows 64bit zip -> Extract .exe file ->
# Go to cmd -> ngrok -> execute ‘ngrok.exe http 8080’ copy the forwarding link add it to the
# payload_url-> Add Webhook ‘/github-webhook’ -> Content-type (Application/JSON)
# Go to Jenkins -> Click on build now
# Go to GitHub -> Add a file .txt -> commit it -> Go to Jenkins -> Refresh -> Wait for 10-15 sec
# and it will automatically Build






# Exp 11: To Implement Docker Commands
# Docker commands:
# Docker –version
# Docker login
# Next open docker -> Go to images -> Search ‘Images’ -> eg: Image named registry
# Cmd -> docker pull <imagename> -> docker images -q ->
# Docker pull ubuntu
# Docker pull ubuntu:rolling








# Exp 12: To build an Image for a Web Application using DockerFile
# Create a index.html file -> write some code -> Keep the Docker file in the same folder ->
# Docker build -t aec
# Docker scout images
# Docker images
# Docker inspect images
# Docker history aec
# Docker ps





# Exp 13: In Jenkins, create a slave node, connect it with master and build a project in slave node
# Manage Jenkins => Node -> Create new Node -> Permanent Agent -> Create -> Enter Name of node -> No of executors (2) 
# -> Working dir (Enter any folder path) -> Remote root directory (Same Path) -> Save -> Click On node -> Copy and past on cmd 
# Create a freestyle project -> Restricted where this project can be run -> Enter the name of LAabel -> Build Steps -> Windows Batch Command -> Apply Save 









# Exp 14: To create and run a test case on Chrome/Firefox browser
# with selenium IDE addon
# Open Selenium -> Record a new test in a new project -> enter project name ->
# enter base URL -> start recording -> record some actions -> stop Recording
# Open selenium -> Run current test
# (Should pass all the testcases)