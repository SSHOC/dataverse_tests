pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -V
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    ./venv/bin/python -m pytest -v --junit-xml=report.xml --cache-clear -rsx
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh 'rm -rf venv'
            }
        }

    }

	post {
		always {
			junit 'report.xml'
		}
	}
}
