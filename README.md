# 📝 To-Do Flask App with Kubernetes
# 실습 주제: Docker + Kubernetes 기반 To-Do 웹앱

이 프로젝트는 **Flask 웹앱 기반의 할 일 목록 관리 시스템**을 Docker 컨테이너로 구성하고, **Kubernetes 환경에 배포**하여 마스터/워커 구조로 분산된 클러스터 실습을 수행한 결과입니다.

---

## 📁 프로젝트 구조
todo-flask-app/
├── master/              # Flask 앱 및 K8s 배포용 구성 파일
│   ├── app.py
│   ├── Dockerfile
│   ├── todo-deployment.yaml
│   ├── todo-service.yaml
│   ├── todo-ingress.yaml
│   └── templates/
│       └── index.html
├── worker/              # 워커 노드 설정 정보 백업
│   ├── docker-version.txt
│   ├── docker-info.txt
│   ├── kubeadm-version.txt
│   └── kubelet-version.txt
└── README.md


---

## 🚀 주요 기술 스택

- **Python Flask**: 웹 애플리케이션 백엔드
- **HTML / CSS**: 프론트엔드 UI
- **Docker**: 애플리케이션 컨테이너화
- **Kubernetes (K8s)**: 컨테이너 오케스트레이션
- **Git + GitHub**: 버전 관리 및 원격 저장소

---

## ⚙️ 쿠버네티스 구성 요소

- `todo-deployment.yaml`: Flask 앱 배포 설정
- `todo-service.yaml`: ClusterIP 서비스 연결
- `todo-ingress.yaml`: Ingress 컨트롤러 연동

---

## 🔐 실습 목적 및 기대효과

- 쿠버네티스 마스터/워커 클러스터 구성 실습
- YAML을 통한 리소스 정의 및 배포 자동화
- 워커 노드 상태 및 설정 이력 백업
- 실제 CI/CD 흐름에 가까운 구조 경험

---

## 📌 사용법 (마스터 노드 기준 실행)

# Docker 이미지 빌드는 워커 노드에서 수행
cd ~/todo-flask-app/master

# 쿠버네티스 리소스 배포
kubectl apply -f todo-deployment.yaml
kubectl apply -f todo-service.yaml
kubectl apply -f todo-ingress.yaml

✅ 정상 배포 후 Ingress 주소를 통해 접속:   http://localhost:8080/todo/   # (호스트 PC 브라우저에서 확인)
ㄴ🧩 Ingress 설정은 VirtualBox의 포트 포워딩 8080 → 80 으로 연결됨

✅ 확인 방법
kubectl get pods
kubectl get svc
kubectl get ingress
ㄴ정상적으로 Pod가 Running 상태이고, Ingress에 주소가 뜨면 접속 가능합니다.
