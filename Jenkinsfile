pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
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
