# YouTube Monitor

Script em Python para monitorar canais do YouTube via RSS
e enviar notificações automaticamente no Android usando Termux.

## Funcionalidades

- Monitoramento automático de canais
- Notificações locais no Android
- Compatível com Termux
- Uso de RSS oficial do YouTube
- Projeto leve e simples

## Requisitos

- Python 3
- feedparser
- termux-api

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python monitor.py
```

## Estrutura do Projeto

```txt
youtube-monitor/
│
├── monitor.py
├── requirements.txt
├── README.md
├── .gitignore
└── ultimo_video.txt
```
