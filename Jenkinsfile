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
                echo "Testing the app version"
            }
        }
        stage('Deploy') { 
            steps {
                echo "deploying the app version"
            }
        }
    }
    post{
        success {
            echo 'it succedded'
        }
    }
}
