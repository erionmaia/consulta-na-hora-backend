# Sistema de Agendamento de Consultas Médicas

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django](https://img.shields.io/badge/django-4.2%2B-green.svg)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/react-18%2B-blue.svg)](https://reactjs.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

Um sistema completo para agendamento de consultas médicas, permitindo que pacientes e médicos se cadastrem na plataforma, visualizem disponibilidades e gerenciem consultas.

## Funcionalidades

- **Autenticação e Registro**
  - Cadastro de pacientes e médicos
  - Login seguro com JWT
  - Recuperação de senha

- **Agendamento de Consultas**
  - Visualização de disponibilidade dos médicos
  - Agendamento de consultas
  - Confirmação e cancelamento de consultas
  - Histórico de consultas

- **Dashboard Personalizado**
  - Interface específica para pacientes
  - Interface específica para médicos
  - Visualização de agenda
  - Gerenciamento de consultas

- **Notificações**
  - E-mails de confirmação
  - Lembretes de consultas
  - Notificações de alterações

## Tecnologias Utilizadas

### Backend
- Python 3.9+
- Django 4.2+
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Celery (para tarefas assíncronas)

### Frontend
- React 18+
- Material-UI
- Redux Toolkit
- React Router
- Axios

## Instalação

### Backend

1. Clone o repositório:
```bash
git clone https://github.com/erionmaia/sistema-consultas.git
cd sistema-consultas/consultas_backend
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
```bash
python3 manage.py migrate
```

5. Inicie o servidor:
```bash
python3 manage.py runserver
```

### Frontend

1. Navegue até a pasta do frontend:
```bash
cd ../consultas_frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Inicie o servidor de desenvolvimento:
```bash
npm start
```

## 📝 Uso

1. Acesse `http://localhost:3000` no seu navegador
2. Crie uma conta como paciente ou médico
3. Faça login e comece a usar o sistema

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## 📧 Contato

Erion Schlenger - [erionmaia@gmail.com](mailto:erionmaia@gmail.com)

Link do Projeto: [https://github.com/erionmaia/sistema-consultas](https://github.com/erionmaia/sistema-consultas) 
