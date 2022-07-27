pipeline {
    agent none
    stages {
        stage('checkout') { 
            agent any
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git']]])
            }
        }
        stage('Build') { 
            agent any
            steps {
                git branch: 'python', url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git'
                bat 'python list_dict.py'
            }
        }
        stage('Test') {
            agent any
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
