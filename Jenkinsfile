pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    stages {

        stage('Check Environment') {
            steps {
                sh '''
                    echo "User: $(whoami)"
                    python3 --version
                '''
            }
        }

        stage('Setup Python Virtualenv') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Start AMF & SMF APIs') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    nohup python3 api/amf_api.py > amf.log 2>&1 &
                    nohup python3 api/smf_api.py > smf.log 2>&1 &
                    sleep 5
                '''
            }
        }

        stage('Run Robot CNF Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    robot robot/
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.log, output.xml, log.html, report.html', allowEmptyArchive: true
        }
        success {
            echo "✅ CNF AMF/SMF API Tests PASSED"
        }
        failure {
            echo "❌ CNF AMF/SMF API Tests FAILED"
        }
    }
}

