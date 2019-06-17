# Amazon VPC(Virtual Private Cloud)

## VPC란?

[Amazon Virtual Private Cloud 사용설명서](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/what-is-amazon-vpc.html)에 따르면, VPC는 `사용자의 AWS 계정 전용 가상 네트워크`를 의미한다.

- VPC는 AWS 클라우드에서 다른 가상 네트워크와 논리적으로 분리되어 있고, Amazon EC2 인스턴스와 같은 AWS 리소스를 VPC에서 실행할 수 있다.
- VPC는 반드시 하나의 Region에 종속되어 운영되며, 다수의 AZ를 이용하여 설계할 수 있다.
- VPC에 단일 CIDR(Classless Inter-Domain Routing) 블록을 지정할 수 있다. 허용된 블록 크기는 /16 넷마스크 ~ /28 넷마스크이고, 따라서 VPC는 16 ~ 65,536개의 IP 주소를 포함할 수 있다.

## Amazon VPC Console
Amazon VPC 콘솔 대시보드의 세부 메뉴를 간략하게 살펴본다.

### 가상 프라이빗 클라우드(VPC)

- **VPC**(Your VPCs)
    - VPC 목록을 조회할 수 있으며, 각 VPC에 설정된 CIDR, DHCP 설정 등을 변경할 수 있다.

- **서브넷**(Subnet)
    - 가상 인스턴스가 사용할 수 있는 private IP 주소의 범위
    - 서브넷이 라우팅 테이블(Route Table)을 통해 인터넷 게이트웨이에 연결된 경우, 이를 퍼블릭 서브넷(Pulbic Subnet)이라고 한다.
    - VPC 외부에서 바로 접근할 수 없는 서브넷을 프라이빗 서브넷(Private Subnet)이라고 한다.
    - 프라이빗 서브넷의 리소스가 외부에 접촉하기 위해서는 반드시 퍼블릭 서브넷(NAT, bastion, ELB 등)을 통과해야 한다.

- **라우팅 테이블**(Route Tables)
    - Subnet에서 outbound로 나가는 트래픽의 destination(ip 대역), target(local, IGW, NAT 등)을 정의한다.
    - VPC를 생성하면 자동으로 default 라우팅 테이블을 생성한다.

- **인터넷 게이트웨이**(Internet Gateways)
    - VPC가 인터넷에 연결되기 위해서는 Internet Gateway가 반드시 필요하다.
    - 줄여서 IGW라고 표현하기도 한다.

-  **외부 전용 인터넷 게이트웨이**(Egress Only Internet Gateways)
    - Outbound만 허용하는 IGW

- **DHCP 옵션 세트**(DHCP Options Sets)
    - VPC를 생성하면 자동으로 DHCP 옵션 세트가 생성되어 VPC에 연결된다.

- **탄력적 IP**(Elastic IPs)
    - Elastic IP (public 고정 IP), 줄여서 EIP로 표현하기도 한다.
    - 모든 인스턴스 또는 네트워크 인터페이스에 EIP를 부여할 수 있다.

- **엔드포인트**(Endpoints)
    - VPC Endpoint를 사용하면 NAT 디바이스나 VPN 연결, AWS Direct Connect를 통해 인터넷에 액세스하지 않고도 VPC와 다른 AWS 서비스 간에 private connection을 생성할 수 있다.

- **NAT 게이트웨이**(NAT Gateways)
    - 기존에는 NAT용 AMI를 사용한 NAT Instance를 주로 사용했으나 NAT Gateway가 출시되고 난 후, VPC에서 NAT 연결은 NAY Gateway 사용을 권장한다.
        - NAT Instance는 스펙에 의해 트래픽을 제한받지만, NAT Gateway를 사용할 경우 10Gbps까지 트래픽을 처리할 수 있다고 한다.
    - Private Subnet에서 외부(인터넷)에 접근하기 위해서 사용한다.

- **피어링 연결**(Peering Connections)
    - VPC to VPC의 연결을 관리한다.
    - 자신의 계정 혹은 다른 계정이 소유하고 있는 VPC에 연결할 수 있다.

### 보안(Security)

- **네트워크 ACL**(Network ACLs)
    - Subnet의 IN/OUT Bound를 정의한다.
    - 허용 규칙만 지원한다.
        - 참고 - [네트워크 ACL 규칙](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-network-acls.html#nacl-rules)
    - Instance 간 Subnet이 다른 경우 NACL(Network ACL)이 적용된다.

- **보안 그룹**(Security Groups)
    - Instance의 IN/OUT Bound를 정의한다.
    - 허용, 금지 규칙을 지원한다.
        - 참고 - [보안 그룹 규칙](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules)
    - Instance 간 Subnet이 같은 경우 Security Group만 적용된다.

## 물리 네트워크와의 비교

VPC의 각 항목이 각각 물리 네트워크의 어떤 부분에 매칭되는지 이해하기 위해 간단한 물리 네트워크와 비교해보도록 한다.

### 물리 네트워크

다음은 Internet ISP에 연결된 public IP(210.1.22.33)를 가정용 공유기(Router)와 스위치를 이용해 private IP(192.168.0.0/24)로 공유해서 인터넷을 사용하는 홈랜 네트워크 구조이다.

![](https://blog.2dal.com/wp-content/uploads/2017/09/homelan.png)

공유기의 주요 기능은 다음과 같다.

- **라우터**(Router)
    - 라우터는 서로 다른 네트워크 간의 통신을 중개한다. 여기서 다른 네트워크란 `subnet mask가 다른 네트워크`로 이해하면 쉽다.

- **스위치**(Switch)
    - OSI Layer에 따라 L2, L3, L4, L7으로 구분하며, 공유기 내부에서 사용하는 스위치는 L2 스위치를 칭한다. 
    - 각 포트에 연결된 MAC address를 기억하고 있다가 스위치로 들어온 요청에서 이미 기록된 destination MAC address를 읽어, 해당 MAC address로 연결된 port로 데이터를 전송하는 역할을 한다.

- **NAT**(Network Address Translation)
    - 외부 네트워크와 통신할 때는 반드시 public IP를 통해서 할 수 있다.
    - 공유기 내부의 장비들은 private IP를 할당받았기 때문에 외부 네트워크와의 통신이 불가하다.
    - 공유기의 NAT 기능을 통해서 내부(private IP)에서 외부(public IP)로 나가는 요청을 public IP로 변환해서 전송하고, 요청에 대한 응답이 오면 요청했던 내부 IP(private IP)로 전달해주는 역할을 한다.

- **DHCP**(Dynamic Host Configuration Protocol)
    - 공유기에 연결된 새로운 장비에 동적으로 IP 주소를 할당한다.

- **방화벽**(Firewall)
    - 내부로 들어오는/외부로 나가는 IP/PORT를 특정 규칙으로 통제(*열기 or 닫기*)할 수 있다.

### 물리 네트워크를 대체하는 VPC

공유기를 사용하는 물리 네트워크를 Amazon VPC resource에 매칭하면 다음과 같다.

![](https://blog.2dal.com/wp-content/uploads/2017/09/AWS-homelan-1.png)

공유기의 주요 기능을 다음과 같은 각각의 AWS resource가 대신하게 된다.

- **라우터**(Router)
    - **Internet Gateway + Route Table**이 라우터를 대신한다.
    - Internet Gateway는 VPC마다 최대 하나씩 할당하며, VPC의 Internet 연결을 위해 사용한다.
    - Route Table은 네트워크 트래픽을 전달할 위치를 결정하는데 사용한다.

- **스위치**(Switch), **DHCP**(Dynamic Host Configuration Protocol)
    - AWS는 스위치를 별도로 구분하지 않으며, **Subnet**이 스위치의 기능을 포함한다.
    - 가상 스위치는 가상 라우터와 가상 머신 인스턴스의 가상 NIC(Network Interace Card)가 연결되는 접점이 된다.
    - 하나의 가상 스위치에 하나의 Subnet이 할당된다. (Subnet은 가상 머신 인스턴스가 사용할 수 있는 private IP 주소의 범위이다.)
    - Subnet에 연결된 인스턴스는 기동 시 **DHCP**를 통해 private IP 주소를 할당받는다.

- **NAT**(Network Address Translation)
    - **NAT instance**나 **NAT Gateway**가 NAT를 대신한다.

- **방화벽**(Firewall)
    - **NACL**(Network ACL)과 **Security Group**이 방화벽을 대신한다.

## About Reference Keywords

- **테넌트**(Tenent)
    - 클라우드 서비스 이용자가 갖게 되는 `자신만의 격리된 환경`을 테넌트라고 한다. 혹 다른 이용자와 물리적으로는 하나의 서버를 공유하게 되더라도 `논리적으로 분리된 멀티 테넌트 환경`에 의해서 클라우드 리소스를 보호받을 수 있다.
    - AWS에서는 하나의 관리자 계정(AWS 콘솔 루트 사용자)에 의해 관리되는 환경을 테넌트라고 할 수 있다.

- **리전**(Region)
    - 클라우드 인프라가 위치한 국가나 지역을 식별할 수 있도록 분리한 것을 리전이라고 한다.
    - AWS에서는 미국 동/서부, 캐나다, 유럽, 아시아, 남미 중에서 리전을 선택해서 사용할 수 있다. [AWS Region Table](https://aws.amazon.com/ko/about-aws/global-infrastructure/regional-product-services/)에서 해당 목록을 확인할 수 있다. 

- **AZ**(Availability Zone)
    - 동일 리전 안에서 리소스가 운용되는 데이터 센터를 AZ(Availability Zone)이라고 한다.
    - 여러개의 AZ에 동일 리소스/서비스를 분산 배포해서, 특정 데이터 센터(zone)에서 발생하는 장애에 대비할 수 있다.
    - 동일 리전 안에서의 AZ 간 발생하는 latency 문제는 `low-latency links`를 통해서 보장한다.

- **CIDR**(Classless Inter-Damain Routing)
    - VPC resource는 CIDR로 IP 대역을 정의한다. 일반적으로 VPC는 private IP 대역인 다음 대역 내에서 CIDR을 정의한다.
        - 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
        - 172.16.0.0 - 172.31.255.255 (172.16.0.0/12)
        - 192.168.0.0 - 192.168.255.255 (192.168.0.0/16)

- **NIC**(Network Interface Card)
    - NIC는 네트워크 상에서 컴퓨터 간의 통신을 위해 케이블을 사용할 때, 해당 케이블을 컴퓨터에 연결하는 매개체 역할을 한다. 즉, 
        - 네트워크 케이블로부터 도착하는 테이터를 수신한다.
        - 케이블을 통해 다른 컴퓨터로 데이터를 전송한다.
        - 케이블과 컴퓨터 사이의 데이터 흐름을 제어한다.
    - 네트워크 인터페이스 카드(NIC)는 네트워크 어댑터 카드(Network Adapter Card), LAN(Local Area Network) 카드 등 다양한 이름으로 불리고 있다.

- **Bastion Host**
    - 배스티언 호스트는 침입 차단 소프트웨어가 설치되어 내부와 외부 네트워크 사이에서 일종의 게이트 역할을 수행하는 호스트이다.

- **ELB**(Elastic Load Balancing)
    - 시스템에 가해지는 부하를 여러대의 시스템으로 분산해서 규모있는 시스템을 만들 수 있도록 해주는 단일 진입점이다.

- **AMI**(Amazon Machine Image)
    - 인스턴스를 시작하는데 필요한 정보, 즉 소프트웨어 구성이 개제된 템플릿이다.
        - ex) OS, application server, application 등


# Reference
[AWS VPC basic](https://blog.2dal.com/2017/09/12/aws-vpc-basic/)

[NIC란 무엇인가?](https://m.blog.naver.com/PostView.nhn?blogId=hwasin6&logNo=80016340438&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

[AWS 사용설명서 - Amazon VPC란 무엇인가?](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/what-is-amazon-vpc.html#what-is-vpc-subnet)

[AWS 사용설명서 - 네트워크 ACL](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-network-acls.html)

[AWS 사용설명서 - 보안](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_Security.html)

[[하루 3분 IT] 배스천 호스트 (Bastion Host)](http://blog.naver.com/PostView.nhn?blogId=pentamkt&logNo=221034903499&parentCategoryNo=&categoryNo=20&viewDate=&isShowPopularPosts=false&from=postView)

[Elastic Load Balancing (ELB)](https://opentutorials.org/course/608/3008)

[AWS 사용설명서 - 인스턴스 및 AMI](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/ec2-instances-and-amis.html)