# 🏢 Customer Registration System

Sistema de cadastro de clientes desenvolvido em Python com MySQL, focado em **arquitetura em camadas**, **código limpo** e **boas práticas de desenvolvimento**.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📋 Sobre o Projeto

Este é um projeto **educacional e prático** que demonstra a implementação de uma aplicação Python seguindo princípios de arquitetura de software. O objetivo é ter um código **organizado, testável e fácil de manter**.

### O que você vai encontrar aqui:

✅ **CRUD completo** de clientes com interface terminal
✅ **Arquitetura em camadas** (View → Controller → Service → Repository)
✅ **Testes automatizados** (41 testes com pytest)
✅ **DTOs** para transporte de dados entre camadas
✅ **Interfaces** para padronizar contratos dos repositórios
✅ **Validações** de email, telefone, data de nascimento
✅ **Injeção de dependências** para facilitar testes

### O que ainda NÃO tem:

❌ API REST (é uma aplicação terminal)
❌ Sistema de autenticação
❌ Docker/Containerização
❌ CI/CD configurado
❌ Frontend web
❌ Módulo de endereços completo (em desenvolvimento)

## 🛠 Tecnologias

- **Python 3.8+**
- **MySQL** - Banco de dados
- **mysql-connector-python** - Driver MySQL
- **pytest** - Testes automatizados
- **python-dotenv** - Variáveis de ambiente
- **readchar** - Entrada interativa
- **tabulate** - Formatação de tabelas

## 🏗 Arquitetura

O projeto segue uma separação clara de responsabilidades:

```
┌─────────────────────────────────┐
│   VIEW (Terminal Interface)     │  ← Interação com usuário
└───────────────┬─────────────────┘
                │
┌───────────────▼─────────────────┐
│   CONTROLLER                    │  ← Orquestração e validação de entrada
└───────────────┬─────────────────┘
                │
┌───────────────▼─────────────────┐
│   SERVICE                       │  ← Regras de negócio
└───────────────┬─────────────────┘
                │
┌───────────────▼─────────────────┐
│   REPOSITORY                    │  ← Acesso a dados
└───────────────┬─────────────────┘
                │
┌───────────────▼─────────────────┐
│   DATABASE (MySQL)              │  ← Persistência
└─────────────────────────────────┘
```

### Por que essa estrutura?

- **View**: Separa a interface do usuário da lógica de negócio
- **Controller**: Valida entrada e orquestra o fluxo
- **Service**: Centraliza regras de negócio e validações de domínio
- **Repository**: Isola o acesso a dados (fácil trocar o banco depois)
- **Database**: Gerencia conexões

Isso facilita **testes**, **manutenção** e **evolução** do código.

## 📁 Estrutura do Projeto

```
customer-registration-system/
│
├── run.py                      # Ponto de entrada
├── requirements.txt            # Dependências
├── .env                        # Configurações (não versionado)
│
├── src/
│   ├── controllers/            # Orquestração de fluxo
│   ├── services/               # Regras de negócio
│   ├── repositories/           # Acesso a dados
│   │   └── interfaces/         # Contratos dos repositórios
│   ├── models/                 # Entidades do domínio
│   ├── dtos/                   # Data Transfer Objects
│   ├── database/               # Gerenciamento de conexão
│   ├── view/                   # Interface terminal
│   ├── utils/                  # Validadores e formatadores
│   └── main/                   # Inicialização
│
└── test/
    ├── test_service/           # Testes de serviço
    ├── test_controller/        # Testes de controller
    └── test_connection/        # Teste de conexão DB
```

## ⚡ Começando

### Pré-requisitos

- Python 3.8 ou superior
- MySQL Server 5.7+
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/customer-registration-system.git
cd customer-registration-system
```

### 2. Crie o ambiente virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie o banco no MySQL:

```sql
CREATE DATABASE customer_db;
USE customer_db;

CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=customer_db
DB_PORT=3306
```

### 6. Execute

```bash
python run.py
```

## 🎮 Como Usar

Ao executar, você verá o menu principal:

```
╔══════════════════════════════════════════╗
║   SISTEMA DE CADASTRO DE CLIENTES        ║
╚══════════════════════════════════════════╝

1. Cadastrar novo cliente
2. Listar todos os clientes
3. Buscar cliente por ID
4. Atualizar dados do cliente
5. Deletar cliente
6. Sair
```

### Exemplo: Cadastrar Cliente

```
Nome: João
Sobrenome: Silva
Email: joao.silva@email.com
Telefone: (11) 98765-4321
Data de Nascimento (DD/MM/AAAA): 15/03/1990

✓ Cliente cadastrado com sucesso! ID: 1
```

### Exemplo: Listar Clientes

```
╔════╤═══════╤═══════╤═══════════════════════╤═══════════════════╤══════════════╗
║ ID │ Nome  │ Sobre │ Email                 │ Telefone          │ Nascimento   ║
╠════╪═══════╪═══════╪═══════════════════════╪═══════════════════╪══════════════╣
║ 1  │ João  │ Silva │ joao.silva@email.com  │ (11) 98765-4321   │ 15/03/1990   ║
╚════╧═══════╧═══════╧═══════════════════════╧═══════════════════╧══════════════╝
```

## 🧪 Testes

O projeto tem **41 testes automatizados** cobrindo Services e Controllers.

### Rodar todos os testes

```bash
pytest
```

### Rodar com detalhes

```bash
pytest -v
```

### Rodar testes específicos

```bash
# Service
pytest test/test_service/test_customer_service.py -v

# Controller
pytest test/test_controller/test_controller.py -v
```

### Estrutura de Testes

- **test_service/**: Testa lógica de negócio isoladamente
- **test_controller/**: Testa fluxo de controller
- **test_connection/**: Testa conexão com banco

Os testes do service usam **repository fake** (não dependem do banco real).

## 🎯 Funcionalidades Detalhadas

### Validações Implementadas

#### Email

- Formato válido (contém @ e domínio)
- Unicidade (não pode cadastrar email duplicado)

#### Telefone

- Formato brasileiro: `(XX) XXXXX-XXXX` ou `(XX) XXXX-XXXX`
- Unicidade (não pode cadastrar telefone duplicado)

#### Data de Nascimento

- [ ] Formato DD/MM/AAAA
- [ ] Conversão automática para formato do banco

### CRUD Completo

- **Create**: Cadastra cliente com todas as validações
- **Read**: Lista todos ou busca por ID
- **Update**: Atualiza campos individuais ou múltiplos
- **Delete**: Exclusão com confirmação de segurança

## 🧩 Decisões de Projeto

### Por que DTOs?

Os DTOs (`CreateCustomerDTO`, `UpdateCustomerDTO`) evitam passar dicionários ou objetos complexos entre camadas. Deixam o contrato explícito.

### Por que Interfaces?

As interfaces (`ICustomerRepository`, `IRepository`) permitem criar **repositórios fake** para testes sem depender do banco real.

### Por que tantas camadas?

Parece "over-engineering" para um CRUD simples, mas:

- Facilita **testes** (cada camada testada isoladamente)
- Facilita **manutenção** (mudanças localizadas)
- Facilita **evolução** (adicionar API REST mantendo a lógica)

## 📝 O que aprendi desenvolvendo isso

- ✅ Separação de responsabilidades na prática
- ✅ Testes com isolamento de dependências
- ✅ Injeção de dependência em Python
- ✅ DTOs e Interfaces para contratos claros
- ✅ Validações de negócio vs validações de entrada

## 🚧 Limitações Conhecidas

- Módulo de endereços está incompleto
- Não tem sistema de logs estruturado (só logging básico)
- Interface é só terminal (sem web)
- Não tem tratamento de concorrência
- Testes de repository dependem de banco real (falta mockar melhor)

## 🔮 Próximos Passos (realistas)

- [ ] Completar módulo de endereços
- [ ] Aumentar cobertura de testes para 90%+
- [ ] Adicionar logging estruturado
- [ ] Melhorar tratamento de erros
- [ ] Documentar setup do banco com migrations

## 🤝 Contribuindo

Pull requests são bem-vindos! Para mudanças grandes, abra uma issue primeiro.

### Como contribuir

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Luis Felipe de Oliveira Monteiro**

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [seu-perfil](https://linkedin.com/in/seu-perfil)

---

<div align="center">

**Se este projeto te ajudou de alguma forma, considere dar uma ⭐**

Feito com ☕ e Python

</div>
