pipeline {
          agent any       
          stages {
                stage('Checkout'){
                steps { 
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/toufikbenkhelifa/test.git']]])
                }
                
                
                }
          
                stage("test"){
                steps { echo '2222222222'     }
                
                }
                stage("deploy"){
                steps {  echo '333333333'   }
                
                }
                                         
          }
}
