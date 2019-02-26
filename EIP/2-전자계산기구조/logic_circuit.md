# 논리회로(Logic Circuit)
하나 이상의 논리적 입력값에 대해 논리 연산을 수행하여 하나의 논리적 출력값을 얻는 전자회로를 말한다.

## 조합 논리회로(Combinational Logic Circuit)
- 출력 신호가 입력 신호에 의해서만 결정
- 논리곱(AND), 논리합(OR), 논리부정(NOT) 등의 기본 논리소자의 조합으로 만들어진다.
- 플립플롭과 같은 기억소자는 포함하지 않음.
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXQAAACHCAMAAAAxzFJiAAAAsVBMVEX///+FhYUAAAD4/P/v+P7n9f7q9v70+//i8/77/f/2+//h8v7t9/6pqan4+Phvb29ISEisur+SnKDu/f/m+P/g4OCcnJxUVFR7e3vm5+eNjY309PRycnLu7u64uLj2///Z2dk6OjrLy8tfX19QUFCtra3Nzc0vLy/BwcGzs7NnZ2dCQkKgoKAXFxeao6MkJCQnKSsxNTgiJCZdY2caGxu2wsXW4eWFi4+jqq/Bys/f6vDRM8KqAAALlUlEQVR4nO2dCXuiPBeGQ9oZx76ydDrsW9gUAceu03b+/w/7soBiq3VQbORrnuuaoqOEnNtwckjCAWiOJPSpcjTgAKFPlgMk3lX4epIE9M+XgM5BAjoHCegcJKC/kw58+7RH+CTo+g4zcpmvpu9qpOQRyjRl/R71T+MzoE81xdtxNRBBvrLalVHy3Aaur2ZoxUSL7ZnfO5DTQreTolCnyFQsY/sXNJiq/KTBtvG+FWTlFKDIl/AJYOCaOyCN/Who0N0gj2H+IfSn8IYofKdxb7UYvy+cHnP8ewO65AFQ4ZNS9meBC6Z57pSDhE4EbWQCaSf061///aD6Vus71eT7ZDK5ZBo1urpgGteiRTRv6s8urth3L0f13pe4IFbm9+YQ3+gB/7v5uQHd0wCYL/wcKDLrgaoCpFO3HAh0xXGALbGC48hFUWDuhf7tDfQV8jX0qy7QRyvoa+rfNqgT6Gqrh1cwXUttVS6aA9PJBgJdkbIEODGkIYDlAATNx2r7V88JOhaCrbc2fpOU6UCgIxRIhh9o5DVBP8U/wQBaOu6CZnHrXYobSoqUgUAHIJFykAb4hR7lOGT8qCM9J+hF3nrjkEYzoI7UhdinlC4OASCBPRTosozPTJe9Vrwl+WRA0J2lCxwnjoFBm85AoONLIsUu6mtR3aMvhgPdNecAqNGq75ymg4DuRKYZvaGhDQa6ouM/+npYA4e+0gCiFxthvSGc2742DOgddE7QP0+coDeh2eCg23oP1nOC7iSswxocdB9fph4tTtBtCCsSnA0OOnCg+X4QvqP6gK4cIA/CaO5zh+7Zfrd6AwThotCVPUhODl3xUrOz6OzFUk45Q19qWteaL0jNTcQZOpganVWluOaa7PJu6ZrjdKy5Qyecpkc1dU4+XdFgmSn8fTp2Lx1rHkDoHRvB8AoZoUEHOXhD796Rakt0tPWcoBuIbQcHHe0Yz+gkXu6l3g4O+nFhSy0xDMDBagGdg9UCOgerBXQOVgvoHKwW0DlYLaBzsFpA52C1gM7BagGdg9UCOgerOUGv11END7rbx+ALr4npetXg4KAjqQfqnKBPoUWtHRx0YMJ8/5f2iNfQbgpnZBqDN/TuM0c5hMmxywH6gJ473aVBCGeOzht6ZFkdKy6ROdIkOGqtXR/Q5aL7jW0lqXsZ8F4NMEuSjhUv6GoAFfGGfohUCNNcGaB7QRAurSPjTE7QdfgYkDCAN/TuHamE9znWel4hY32r8uCg21q8/0v7xAk6qrfDg97HanUxDMDBagGdg9UCOgerBXQOVgvoHKwW0DlYLaBzsHoDut++1tL9XW961OmgX34adBRgbfLZKPV9aE+h25ZJbnIGQYJfe2RYBwGQ0NvIFAuRjSfT4gtVLXo9M/4NehiOx5gluFhBZ6xpEWvoALSgh58GPfYsy6PFIILOmwKg0gXVikqvXi3KTifs6nXWFPrSmwYLmUH3syybR/N8zu7dU0q6o0fveFbIPcV93Ei50i7ok5ubmxHJMUXQhTmu0t+Lq9xvoAM7B2vorKgLECNM/oq8Dkdh/gfv2mSPGp0OemA5RlUZkoW52JhdFlX5XKN03RlJBFJDBy12BPo8UshcDoNO5c0NaUmh+5BuCHQ5NRMis+jPD+6APvkbY03xP4wuBL+fn599oGgxaKAHcAUdN4UpFrYnMfDnoIIQ5mMQVeBydP3C9OfmZND1fOpAmMV5M+2rVpV0S6HbS4qbQA8adiY5HoEeRHiHeMGg62aapjB3FepwwBzS22wJdJTHORb+08vKeKod0G9eSy29vU+18iUMn1Tp+VmyHMWcrqDnj+syfFLjqASgqMDFla/jFoXdqCZj6A4+87GWL+HJoPuxFwVGZCCXZJ4g7GRFYX4kgCXZEOj6BjvqXqCF4pnDoKMFaTh2BGkTd2c5zWbB3Mu8mC3LYweTN/SBewHPKiDuZfQnf32pnuJXxaxit2npC9Bks2PbfEahj6cQPt4/wjslxdAv669YJ4ReqAHGrcv4NMOtl5xzfglpmhsAA5IcqXYvAWYXSYjuQ6G7VqRl+M3cxNCXwPV9XQcJ/h/70QH+zHIZdCfCfYQvwx69+u6ONEQLOA1JPxjGt2kyk4BiaoU9blr68hFC/C/fhH4RAjeoyNQxbenXz0Q/b08G3ZckR7Iky5IcqwKB5iqUHcn9qUeY3cLzGXTnFrNzK4jIXixkdG3qMXTcuNHMNFPTLICZAbskv5idBAy6V7gkrwjbsR/tbOmhHv2c305JS3fviW9b5OO1exlj21zLwa1DIckfZTmzbhl0gO6sqihtCv0qleTT+nSF9D1oYeHuJ0f4l8fsUlN1CwfYGgFrFzKDbpmEMIJ0TptBl1hW1px0pL7r0j4B2SRxS724RiXQ/WSRqCWUj6rmpnZ1pJMMPgPwGxo43L4oSnluQV1J1x0prXodgNmQTBhnNXSP2IBDMdrSU1Qf53TRS14UKoxwpGiTJIOYHYWrE3YKY0cbrF8sTFVjbqeG7swsz/OslEJv8tDSeCfN6NcqtthDCRb9XsHtgH5ppn/A0ws+yUofx+evklf544vKDmvm96R+C3bDOIZOixoz6FPoBN5Cp9CVNDKTB9M0Hy4np4LuIqp8Qdqw3bCjcfaMscvquaZglX+whl6QvjWXaMhoU7kMt7nKtOHi//TzJf3wyIqutTNkxEG644WjkY+dOvAQqyuqLzvHOETxGzXQXYVAxyG8tDD82qe/BoFxn11fX09OF6ezZMFFSevI2PkmbbDRJrsYkg1x5LV7kbB79N0saZVmMuiGTn9JG8xnEVZJ/vSX1moHdPqZ8Uw3GPrdg0M6rPvtIaMNcVToFbMMn8cXPm4Yd1OU56Y8DsmnSCPOKLw8FXTD1JnacXTCoK/YGWt25Mdh0OUZUzuztUp3NBIa1e9K23qstkO/ebi7u8NBa4Q3ZjgCkUWTnUdr6EELujInF9FTm4aMSVlqpmY+VOYLuFaxz0wg/uM9/Lk8WUvXqMqs9Z8e9cbOLnYMuuIytX+tHtanKoa0Z+HfduiT16eVXkeXYPZik7aktaDDgFxyZ3K8itdZR1qnZRkT9/InWJVy/Xfyz9Ado9OJvMoE09Iedicd2vXfZIV/r11XpK2s28Snz26JShQ20HWjXuUWrAe8gJXRH4WOd4FivpG7u0NHCvuMibfqpNCVyjmopbNRxvUwY/PtZvh2PG4VsWOUEYSHjjJ2bOkHaEiTGJ3ypw9mEqN3uf6ejuEcZ478Uzf0E/v0xYE+nSv0gft0fwn3lC6g9y6FjAJ9qHOEnq/mI06lIXWk/5+rAfqWMo33jL2fI/Q47m9mbLtER/quTgP36a6V7Bl8P0foiXpql3Nin77vRD1H6KeX6Eg5WC2gc7BaQOdgtYDOwWoBnYPVAjoHqwV0DlYL6BysFtA5WC2gc7BaQOdgtYDOwWoBnYPVAjoHqwV0DlYL6BysFtA5WC2gc7CaV9rXejs46PqAn7xraMzYwUF3Z9n+L+0Ttyfv3srn8ORd74An7xboWOt7gX7Ak3dVkvSVP3Tc0jtWHJGkr0f6mD6evGvCQ1XxzrV7qCLEGToIrO4ijzs+gyfvRp7XseIeYe4N8sm7wITLc3jyruV3XaEbH5tSGnCDnkOaVoM79AOevMvu0j1KvELGOlAfHHTd6WHxunjy7mEVP0piGICD1QI6B6sFdA5WC+gcrBbQOVgtoHOwWkDnYLWAzsFqAZ2D1WcD/cc76JOjoH+YyvvHF4f+dPPrZlPhO20k1fk3jcdvC7kJ3xznV/hloVu/36o6md4e6eFrQo8OnrvpR8VXhO54nqcWjbY8idLrQ9uecMlkfEXoRDQvp79Wk65wW+69Q7QqqC64dSjbRl8Uuo0a6S3Zjd79Glt/jrdk3TbZRu3ym2N+UejuiuaGPlgG8UFhu3faehC38xxpHzoD6F9PAjoHScDhXYWvJwdojiT0qXK0/wGhReKOdZG5bgAAAABJRU5ErkJggg==)

위 그림은 n개의 입력을 받아 m개의 출력을 내는 조합논리회로의 블록도이다. 입력신호가 n개이므로 2^n개의 입력신호 조합을 만들 수 있다.

## 순차 논리회로(Sequential Logic Circuit)

- 출력신호는 입력신호 뿐만 아니라 이전 상태의 논리값에 의해 결정
- 조합 논리회로와 기억소자로 구성되며 기억소자가 퀘환을 형성(기억소자는 2진 정보를 저장할 수 있는 장치로 플립플롭을 사용)
![](http://mblogthumb4.phinf.naver.net/20110928_107/3542995_1317194894266W80Fv_PNG/%B1%D7%B8%B22.png?type=w2)

위 그림은 순차 논리 회로의 블록도이다.

- 동기(Synchronous)식 순차 논리회로
  - 클럭 펄스가 들어오는 시점에서 상태가 변하는 회로
- 비동기(Asynchronous)식 순차 논리회로
  - 클럭펄스에 영향을 받지 않고 현재 입력되는 입력 값이 변화하는 순서에 따라 동작하는 논리회로

### 논리회로의 종류
- **가산기**
  - 두 개 이상의 입력을 이용하여 이들의 합을 출력하는 조합 논리회로, 반가산기와 전가산기가 있다.

- **반가산기와 전가산기의 차이점**
  - 반가산기는 2진수 1비트만을 덧셈 연산하기 때문에 하위 비트에서 발생하는 자리 올림을 고려하지 않는다. 
  - 따라서 반가산기는 두 비트 이상의 2진수 덧셈 연산을 수행할 수 없다. 
  - 반면, 전가산기는 두 입려그 2진수 A와 B 그리고 하위 비트에서 발생한 자리 올림수를 포함하여 2진수 세 개를 더하는 조합 논리회로도이다.

- **병렬 가산기**
  - 전가산기를 병렬로 연결하면 여러 비트로 구성된 2진수의 덧셈 연산을 수행할 수 있다.

- **감산기**(Subtractor)
  - 두 개 이상의 입력에서 하나의 입력으로부터 나머지 입력들을 뺄셈해서 그 차를 출력하는 조합 논리 회로

- **가산기와 감산기의 차이점**
  - 가산기에서의 합은 감산기가 차가 되며 가산기에서의 올림수가 발생했지만 감산기에서는 빌림수가 발생

- **병렬 가감산기**
  - 디지털 장치에서는 별도로 감산기를 사용하지 않고 가산기에 게이트를 추가해 부호 선택신호로 뺼셈 연산을 수행

- **인코딩과 디코딩**
  - **인코딩**(Encoding)
    - 정보의 형태나 형식을 표준화, 보안, 처리속도 향상, 저장공간 절약 등의 목적으로 다른 형태나 형식으로 변화하는 방식으로 부호화라고도 한다.
    - 인코더는 변환장치이다.

  - **디코딩**(Decoding)
    - 인코딩된 정보를 인코딩되기 전으로 되돌리는 처리 방식
    - 복호기 또는 디코더는 복호화를 수행하는 장치나 회로이다.

- **멀티 플렉서**
  - 여러 개의 입력 중 하나만 출력에 전달해주는 조합 논리회로
  - 즉 선택 신호에 의해 여러 개의 입력 중 하나만 선택된다.
  - 다중입력 데이터를 단일 출력하므로 데이터 선택기라고도 한다.

- **디멀티 플렉서**
  - 한꺼번에 들어온 여러 신호 중에서 하나를 골라 출력한다.
  - 멀티플렉서의 역기능을 수행하는 조합 논리 회로이다.
  - 선택선을 통해 여러 개의 출력선 중 하나의 출력선에만 출력을 전달한다.

# Reference
https://m.blog.naver.com/PostView.nhn?blogId=3542995&logNo=70119838701&proxyReferer=https%3A%2F%2Fwww.google.com%2F