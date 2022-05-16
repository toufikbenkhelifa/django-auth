pipeline {
    agent { label 'Maître'}
    options { buildDiscarder(logRotator(numToKeepStr:'5'))}
    environment {DOCKERHUB_CREDENTIALS = credentials('tfkben-dockerhub')}
    stages {
            stage('build'){
                steps {
                sh 'docker build -t tfk/ben:latest .'
                }
            }

         }



}
