pipeline {
          agent any 
          
          environment {
           dockerImage =''
           registry ='tfkben/test'
           registryCredential ='global'
          }
          
          stages {
                stage('Checkout'){
                steps { 
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/toufikbenkhelifa/test.git']]])
                }               
                }
          
                stage('Build Docker Image'){
                steps { 
          dockerImage = docker.build registry                
                
                }    
                }
                stage('Upload image to dockerhub'){
                          steps { 
                                    script{       
                                              docker.withRegistry( '', registryCredential ) {
                                              dockerImage.push()
                                                                                                     }
                                                  
                                    }   
                          }
                
                }
                                         
          }
}
