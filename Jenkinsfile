pipeline {
    agent any
    options { buildDiscarder(logRotator(numToKeepStr:'5'))}
    environment {DOCKERHUB_CREDENTIALS = credentials('tfkben-dockerhub')}
    stages {
            stage('build'){  steps {  sh 'docker build -t tfkben/ben:19-dind .' }  }
            stage('Login'){  steps {  sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin ' }}
            stage('Push'){  steps {  sh 'docker push tfkben/ben:19-dind'}   }                                 
         }                           
            post { always { sh 'docker logout' }}
}
