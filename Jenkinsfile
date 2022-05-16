pipeline {
    agent any
    options { buildDiscarder(logRotator(numToKeepStr:'5'))}
    environment {DOCKERHUB_CREDENTIALS = credentials('tfkben-dockerhub')}
    stages {
             stage('Initialize'){
                 steps {
                     script{
              def dockerHome = tool 'mydocker'
              env.PATH = "${dockerHome}/bin:${env.PATH}"
                     }}
             }
            
            stage('build'){
                steps {
                sh 'docker build -t tfk/ben:latest .'
                }
            }

         }



}
