pipeline {
    agent none
    stages {
        stage('checkout') { 
            agent any
            steps {
                checkout scm
                //checkout([$class: 'GitSCM', branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git']]])
            }
        }
        stage('Build') { 
            //agent { docker { image 'python:3.10.1-alpine' } }
            agent any
            steps {
                //git branch: 'python', url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git'
                //sh 'sh test.sh'
                sh 'sudo apt install python3'
                sh 'python list_dict.py'
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
