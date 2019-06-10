# AWS VPC(Virtual Private Cloud)

## VPC란?

[Amazon Virtual Private Cloud 사용설명서](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/what-is-amazon-vpc.html)에 따르면, VPC는 `사용자의 AWS 계정 전용 가상 네트워크`를 의미한다.

- VPC는 AWS 클라우드에서 다른 가상 네트워크와 논리적으로 분리되어 있고, Amazon EC2 인스턴스와 같은 AWS 리소스를 VPC에서 실행할 수 있다.
- VPC는 반드시 하나의 Region에 종속되어 운영되며, 다수의 AZ를 이용하여 설계할 수 있다.
- VPC에 단일 CIDR(Classless Inter-Domain Routing) 블록을 지정할 수 있다. 허용된 블록 크기는 /16 넷마스크 ~ /28 넷마스크이고, 따라서 VPC는 16 ~ 65,536개의 IP 주소를 포함할 수 있다.



## 물리 네트워크와의 비교

VPC의 각 항목이 각각 물리 네트워크의 어떤 부분에 매칭되는지 이해하기 위해 간단한 물리 네트워크를 보도록 한다.

### 물리 네트워크

다음은 Internet ISP에 연결된 공인 IP(210.1.22.33)를 가정용 공유기(Router)와 스위치를 이용해 private IP(192.168.0.0/24)로 공유해서 인터넷을 사용하는 홈랜 네트워크 구조이다.

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

- **방화벽**(Filrwall)
    - 내부로 들어오는/외부로 나가는 IP/PORT를 특정 규칙으로 통제(*열기 or 닫기*)할 수 있다.

### 물리 네트워크를 대체하는 VPC

공유기를 사용하는 물리 네트워크를 AWS VPC resource에 매칭하면 다음과 같다.

![](https://blog.2dal.com/wp-content/uploads/2017/09/AWS-homelan-1.png)

공유기의 주요 기능을 다음과 같은 AWS resource가 대신하게 된다.

- **라우터**(Router)
    - **Internet Gateway + Route Table**이 라우터를 대신한다.
    - Internet Gateway는 VPC마다 최대 하나씩 할당하며, VPC의 Internet 연결을 위해 사용한다.
    - Route Table은 네트워크 트래픽을 전달할 위치를 결정하는데 사용한다.

- **스위치**(Switch), **DHCP**(Dynamic Host Configuration Protocol)
    - AWS는 스위치를 별도로 구분하지 않으며, **Subnet**이 스위치의 기능을 포함한다.
    - 가상 스위치는 가상 라우터와 가상 머신 인스턴스의 가상 NIC(Network Interace Card)가 연결되는 접점이 된다.
    - 하나의 가상 스위치에 하나의 Subnet이 할당되며, 여기서 Subnet은 가상 머신 인스턴스가 사용할 수 있는 private IP 주소의 범위이다.
    - Subnet에 연결된 인스턴스는 기동 시 **DHCP**를 통해 private IP 주소를 할당받는다.

- **NAT**(Network Address Translation)
    - **NAT instance**나 **NAT Gateway**가 NAT를 대신한다.

- **방화벽**(Firewall)
    - **NACL**(Network ACL)과 **Security Group**이 방화벽을 대신한다.




# Reference
[AWS VPC basic](https://blog.2dal.com/2017/09/12/aws-vpc-basic/)

[NIC란 무엇인가?](https://m.blog.naver.com/PostView.nhn?blogId=hwasin6&logNo=80016340438&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

[AWS 사용설명서 - Amazon VPC란 무엇인가?](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/what-is-amazon-vpc.html#what-is-vpc-subnet)

[AWS 사용설명서 - 네트워크 ACL](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-network-acls.html)

[AWS 사용설명서 - 보안](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_Security.html)

