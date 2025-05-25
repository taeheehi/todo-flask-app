# 📝 To-Do Flask App with Kubernetes
> **실습 주제**: Docker + Kubernetes 기반 To-Do 웹앱  
Flask 웹앱으로 구성된 To-Do 관리 시스템을 Docker 컨테이너로 빌드하고, Kubernetes 환경에서 마스터/워커 구조로 배포한 분산형 클러스터 실습 프로젝트입니다.

## 📁 프로젝트 구조
```
todo-flask-app/
├── master/              # Flask 앱 및 배포 구성
│   ├── app.py
│   ├── Dockerfile
│   ├── todo-deployment.yaml
│   ├── todo-service.yaml
│   ├── todo-ingress.yaml
│   └── templates/
│       └── index.html
├── worker/              # 워커 노드 설정 백업
│   ├── docker-version.txt
│   ├── docker-info.txt
│   ├── kubeadm-version.txt
│   └── kubelet-version.txt
└── README.md
```

## 🚀 주요 기술 스택
- **Python Flask**: 웹 백엔드 프레임워크  
- **HTML / CSS**: 프론트엔드 UI  
- **Docker**: 컨테이너화  
- **Kubernetes (K8s)**: 오케스트레이션  
- **Git + GitHub**: 버전 관리 및 협업

## ⚙️ K8s 구성 요소
- `todo-deployment.yaml` : Flask 앱 배포 정의  
- `todo-service.yaml` : ClusterIP 서비스 설정  
- `todo-ingress.yaml` : 외부 접속을 위한 Ingress 구성

## 🎯 실습 목표 및 기대 효과
- 마스터/워커 클러스터 환경 구성  
- YAML 기반 리소스 선언 및 배포  
- 워커 노드 설정 이력 보존  
- CI/CD와 유사한 운영 흐름 체험

## 🛠️ 사용법 (마스터 노드 기준)

🔧 **Docker 이미지 빌드** (워커 노드에서 수행)  
```bash
cd ~/todo-flask-app/master
# 이후 tar로 저장 및 전송
```

🚀 **Kubernetes 리소스 배포**  
```bash
kubectl apply -f todo-deployment.yaml
kubectl apply -f todo-service.yaml
kubectl apply -f todo-ingress.yaml
```

🌐 **접속 확인**  
- http://localhost:8080/todo/  
- VirtualBox 포트 포워딩 필요 → 8080 (호스트) → 80 (게스트)

🔎 **상태 확인 명령어**  
```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```
→ Pod가 Running 상태이고 Ingress 주소가 출력되면 접속 가능
