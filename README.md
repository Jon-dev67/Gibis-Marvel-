Gibis-Marvel

Uma aplicação desenvolvida com Flask que oferece funcionalidades para leitura de gibis, visualização de vídeos de heróis, além de páginas dedicadas a personagens como Hulk, Luke Cage e Superman. Inclui autenticação de usuários, cadastro e segurança avançada.

Acesse a aplicação em produção: Gibis-Marvel


---

Funcionalidades

Autenticação de Usuários:

Cadastro de novos usuários com validação de dados únicos.

Login e logout com gerenciamento de sessões.

Proteção de rotas para acesso exclusivo a funcionalidades como gibis e vídeos.


Rotas Dedicadas:

Páginas específicas para os personagens Hulk, Luke Cage e Superman.

Páginas protegidas para leitura de gibis e visualização de vídeos.


Segurança:

Senhas criptografadas com Flask-Bcrypt.

Validações personalizadas para evitar duplicidade de usuários, e-mails ou senhas.


Banco de Dados:

Configuração com SQLite para armazenar usuários e informações relacionadas.



---

Tecnologias Utilizadas

Python: Linguagem principal.

Flask: Framework web.

Flask-SQLAlchemy: ORM para gerenciamento do banco de dados.

Flask-WTF: Validações avançadas de formulários.

Flask-Bcrypt: Criptografia de senhas.

Flask-Login: Gerenciamento de autenticação.

HTML e CSS: Para as interfaces.



---

Instalação

1. Clone o repositório:



git clone https://github.com/Jon-dev67/Gibis-Marvel-.git
cd Gibis-Marvel-

2. Crie um ambiente virtual e ative-o:



python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3. Instale as dependências:



pip install -r requirements.txt

4. Crie o banco de dados:



>>> from app import db
>>> db.create_all()
>>> exit()

5. Execute a aplicação:



flask run


---

Como Usar

1. Acesse a página principal pelo navegador: http://127.0.0.1:5000.


2. Cadastre-se para criar um usuário.


3. Faça login para acessar conteúdos exclusivos como gibis e vídeos.


4. Explore páginas dedicadas aos heróis disponíveis.




---

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o projeto.


---

Autor

Jonathan Willian
Desenvolvedor Back-End. Apaixonado por tecnologia e projetos inovadores.


---