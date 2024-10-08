
Automação de Pacientes a Dar Alta - SISREG & G-HOSP<br>
Versão 1.0 - Setembro de 2024<br>
Autor: MrPaC6689<br>
Desenvolvido com o apoio do ChatGPT<br>


Descrição<br>
Este programa automatiza o processo de extração de informações de pacientes internados no sistema SISREG e G-HOSP,  comparando os dados para identificar os pacientes que podem ser dados como alta. A automação utiliza Selenium para navegação automatizada e manipulação de páginas da web.

Funcionalidades principais:<br>
Extrair internados do SISREG: Executa um script automatizado para obter a lista de pacientes internados no sistema SISREG.
Extrair internados do G-HOSP: Executa um script automatizado para obter a lista de pacientes internados no sistema G-HOSP.
Comparar e tratar dados: Compara os dados dos dois sistemas para identificar pacientes que podem receber alta.
Interface interativa: Simples menu para facilitar a escolha das funções.


Dependências:<br>
Para que o programa funcione corretamente, é necessário instalar as seguintes bibliotecas e ferramentas:

     Python (versão 3.6 ou superior)
     Selenium: Biblioteca para automação de navegadores.
     ConfigParser: Para ler arquivos de configuração.
     Colorama: Para adicionar cores ao terminal.
 

Como instalar as dependências:<br>
Abra o Prompt de Comando ou Terminal no diretório do programa e execute os seguintes comandos:

      pip install selenium
      pip install configparser
      pip install colorama



Ferramentas externas:<br>
      Google Chrome: O navegador usado para automação.<br>
      ChromeDriver: Ferramenta necessária para automatizar o Chrome. Baixe a versão correta do ChromeDriver compatível com sua versão do Chrome.
<br>
*** Importante: A versão do ChromeDriver deve ser compatível com a versão do Chrome instalada no seu computador.<br>


Configuração de Credenciais:<br>
  Antes de rodar os scripts, você precisa configurar suas credenciais de acesso ao SISREG e G-HOSP.<br>

Passo a passo para inserir suas credenciais:<br>
  Abra o arquivo config.ini no diretório do programa. Se ele não existir, ele será gerado automaticamente na primeira execução do script.<br>

Edite o arquivo config.ini e insira suas credenciais conforme o exemplo abaixo:<br>

     ini
     Copiar código
     [SISREG]
     usuario = seu_usuario_sisreg
     senha = sua_senha_sisreg

     [G-HOSP]
     usuario = seu_usuario_ghosp
     senha = sua_senha_ghosp

Salve o arquivo após adicionar suas credenciais.<br>

Agora você está pronto para executar o programa.<br>

Como executar o programa:<br>

Abra o arquivo ME EXECUTE.BAT<br>
   O menu interativo será exibido, permitindo que você selecione a opção desejada.<br>

<br>
Erros Comuns e Soluções:<br>
<br>
1. Erro de versão do ChromeDriver:<br>
Se você receber uma mensagem de erro indicando que a versão do ChromeDriver não é compatível, baixe a versão correta de acordo com a versão do Chrome instalado.<br>
Verifique a versão do Chrome digitando chrome://settings/help na barra de endereços do Chrome.<br>

2. Erro de conexão ou acesso negado:<br>
Certifique-se de que suas credenciais de acesso ao SISREG e G-HOSP estão corretas no arquivo config.ini.<br>
<br>
Créditos:<br>
Desenvolvimento: MrPaC6689<br>
Suporte técnico: ChatGPT<br>
<br>
Licença:<br>
Este projeto foi desenvolvido para fins educacionais e não possui uma licença formal. Todos os direitos são reservados ao autor.<br>
<br>
Esperamos que o programa facilite sua rotina e ajude no processo de alta de pacientes!<br>
<br>
FIM DO LEIA-ME

