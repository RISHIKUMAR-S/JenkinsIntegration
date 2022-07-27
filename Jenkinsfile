pipeline {
    agent any
    stages {
        stage('checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git']]])
            }
        }
        stage('Build') { 
            steps {
                git branch: 'python', url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git'
                bat 'python list_dict.py'
            }
        }
        stage('Test') {
            steps {
                echo "Testing the app..."
            }
        }
    }
    post{
        success {
            echo "hooray , it succedded"
        }
    }
}
