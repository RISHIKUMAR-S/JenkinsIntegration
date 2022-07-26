def gv
pipeline {
    agent any
    parameters{
        choice(name : 'VERSION', choices : ['1.1','1.2'], description : 'Version of the build')
        booleanParam(name : 'executeTest', defaultValue : true, description : 'choice to test the build or not')
    } 
    stages {
        stage('init') { 
            steps {
                script{
                    gv = load "Scripts.groovy"
                }
            }
        }
        stage('Build') { 
            steps {
                when{
                    expression {
                        params.executeTest
                    }
                }
                echo 'Building the app'
            }
        }
        stage('Test') { 
            steps {
                echo "Testing the app version ${params.VERSION}"
            }
        }
        stage('Deploy') { 
            steps {
                echo "deploying the app version ${params.VERSION}"
            }
        }
    }
    post{
        success {
            echo 'it succedded'
        }
    }
}
