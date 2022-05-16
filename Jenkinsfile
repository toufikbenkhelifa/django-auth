pipeline {
    agent { label 'linux'}
    option { buildDiscarder(logRotator(numToKeepStr:'5'))}
    environment {DOCKERHUB_CREDENTIALS = credentials('tfkben-dockerhub')}
    stages {
            stage('build'){
                sh 'docker build -t tfk/ben:latest .'
            }

         }



}
