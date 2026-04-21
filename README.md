# 🖐️ Sistema de Interpretação de Gestos com Python e Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv" />
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

---

## 📌 Visão Geral

Este projeto apresenta uma solução de **reconhecimento de gestos em tempo real** utilizando técnicas de **Visão Computacional** e **Machine Learning**, sem a necessidade de dispositivos adicionais ou sensores físicos.

A captura é realizada exclusivamente via **webcam**, tornando o sistema acessível, de baixo custo e facilmente replicável em diferentes ambientes.

---

## 🎯 Objetivos

* Detectar e interpretar gestos das mãos em tempo real
* Converter gestos em comandos digitais
* Explorar aplicações práticas de **Machine Learning** com visão computacional
* Servir como base para projetos de automação, acessibilidade e interação humano-computador

---

## 🧠 Stack Tecnológica

| Tecnologia             | Descrição                                  |
| ---------------------- | ------------------------------------------ |
| Python                 | Linguagem principal do projeto             |
| OpenCV                 | Processamento de imagem e vídeo            |
| NumPy                  | Manipulação de arrays e cálculos numéricos |
| MediaPipe *(opcional)* | Detecção avançada de mãos                  |
| VSCode                 | Ambiente de desenvolvimento                |

---

## ⚙️ Arquitetura do Sistema

O fluxo de funcionamento do sistema é composto pelas seguintes etapas:

1. **Captura de Vídeo**
   A webcam captura frames em tempo real

2. **Pré-processamento**
   Tratamento da imagem (escala de cinza, suavização, segmentação, etc.)

3. **Detecção de Mão**
   Identificação da região de interesse (ROI)

4. **Extração de Características**
   Identificação de pontos-chave ou contornos

5. **Classificação do Gesto**
   Aplicação de regras ou modelos de Machine Learning

6. **Ação/Resposta**
   Execução de comandos com base no gesto reconhecido

<img width="1244" height="669" alt="Captura de tela 2026-04-21 201642" src="https://github.com/user-attachments/assets/2904eab3-b1e0-4627-ae34-029b48997f7b" />

<img width="1194" height="683" alt="Captura de tela 2026-04-21 201709" src="https://github.com/user-attachments/assets/1db33da1-5d44-48b0-84c2-82101935bf2a" />

💡Nota: O projeto ainda não realiza reconhecimento de gestos de forma completa. A qualidade da webcam e as condições de captura impactam diretamente os resultados, por isso esta fase de coleta é essencial para evolução do sistema. Cada gesto com a mão, por exemplo "1" com a mão se abre um programa no computado.

---

## 🚀 Instalação

### Pré-requisitos

* Python 3.8 ou superior
* Webcam funcional

### Passos

```bash
git clone https://github.com/seu-usuario/Sistema-de-Interpretacao-de-Gestos-com-Python-e-Machine-Learning.git
cd Sistema-de-Interpretacao-de-Gestos-com-Python-e-Machine-Learning
```

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

```bash
# Instalar dependências
pip install -r requirements.txt
```

---

## ▶️ Execução

```bash
python main.py
```

> ⚠️ Certifique-se de que sua webcam está disponível e não está sendo utilizada por outro aplicativo.

---

## 📂 Estrutura do Projeto

```bash
├── src/
│   ├── processamento.py
│   ├── reconhecimento.py
│   ├── features.py
│   └── utils.py
├── models/
├── data/
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Possíveis Aplicações

* Controle por gestos (hands-free interfaces)
* Jogos interativos
* Sistemas de acessibilidade
* Automação residencial
* Interfaces para realidade aumentada/virtual

---

## 📈 Roadmap

* [ ] Integração com modelos de Deep Learning
* [ ] Suporte a múltiplas mãos
* [ ] Interface gráfica (GUI)
* [ ] Treinamento customizado de gestos
* [ ] Deploy em aplicações reais

---

## 🤝 Contribuição

Contribuições são incentivadas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas alterações (`git commit -m 'feat: nova funcionalidade'`)
4. Push para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## 👨‍💻 Autor

**Seu Nome**
GitHub: https://github.com/seu-usuario

---

## ⭐ Considerações Finais

Este projeto demonstra como técnicas de visão computacional podem ser aplicadas para criar interfaces naturais e intuitivas entre humanos e máquinas, utilizando apenas recursos acessíveis.

Se este projeto foi útil para você, considere deixar uma ⭐ no repositório!

---
