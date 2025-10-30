pipeline {
  agent any
  options { timestamps() }

  parameters {
    string(
      name: 'ALPHA',
      defaultValue: '0.3',
      description: 'ElasticNet alpha değeri'
    )
    string(
      name: 'L1_RATIO',
      defaultValue: '0.7',
      description: 'ElasticNet l1_ratio değeri'
    )
  }

  environment {
    // Proje klasörün (senin local masaüstün)
    SRC_DIR = "C:\\Users\\ENES\\OneDrive\\Masaüstü\\mlflow-jenkins-demo"

    // yeni venv adı: .venv2
    PYTHON  = "${WORKSPACE}\\.venv2\\Scripts\\python.exe"
    PIP     = "${WORKSPACE}\\.venv2\\Scripts\\pip.exe"
  }

  stages {

    stage('Sync project files from local') {
      steps {
        bat 'echo Source: %SRC_DIR%'
        bat 'dir "%SRC_DIR%"'

        // kaynak klasörden WORKSPACE'e kopyala
        bat '''
robocopy "%SRC_DIR%" "%WORKSPACE%" *.* /E /XO /NFL /NDL /NJH /NJS /NP
if %ERRORLEVEL% LSS 8 (exit /b 0) else (exit /b %ERRORLEVEL%)
'''
        bat 'echo Workspace after copy:'
        bat 'dir'
      }
    }

    stage('Setup venv') {
      steps {
        // Python 3.12 -> 3.11 -> Program Files fallback; ENV = .venv2
        bat '''
if exist "C:\\Users\\ENES\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" (
  "C:\\Users\\ENES\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv .venv2
) else if exist "C:\\Users\\ENES\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" (
  "C:\\Users\\ENES\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m venv .venv2
) else if exist "C:\\Program Files\\Python311\\python.exe" (
  "C:\\Program Files\\Python311\\python.exe" -m venv .venv2
) else (
  echo Could not find Python 3.11/3.12. Please install from python.org. & exit /b 1
)
'''
        bat '%PIP% --version'
        bat '%PYTHON% --version'
      }
    }

    stage('Install dependencies') {
      steps {
        bat '%PYTHON% -m pip install --upgrade pip'
        bat '%PYTHON% -m pip install -r requirements.txt'
      }
    }

    stage('Run tests') {
      steps {
        bat '%PYTHON% -m pytest -q'
      }
    }

    stage('Train model with MLflow') {
      steps {
        bat 'set ALPHA=%ALPHA% && set L1_RATIO=%L1_RATIO% && %PYTHON% train.py'
      }
    }

    stage('Write summary') {
      steps {
        bat '''
echo Run summary > run_summary.txt
echo ALPHA=%ALPHA% >> run_summary.txt
echo L1_RATIO=%L1_RATIO% >> run_summary.txt
'''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'mlruns/**/*, run_summary.txt', allowEmptyArchive: true
    }
    success { echo "Pipeline basariyla tamamlandi." }
    failure { echo "Pipeline hata ile bitti." }
  }
}
