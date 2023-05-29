Feature: [[API_TITLE]] [[API_VERSION]] (BR)

    Como usuário do sistema
    Eu quero acessar [[FEATURE_TITLE_ARTICLE]] [[API_TITLE_LOWER]]
    De modo que eu possa gerenciá-[[FEATURE_TITLE_ARTICLE_COMPLEMENT]]

    @[[API_OPERATION_BR]]
    @api
    @br
    @comparando_resposta
    @post
    @status_200
    @sucesso
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_comparando_resposta
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], comparando o conteúdo esperado da resposta
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And  tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then a API responde o código de status 200
      And  a API responde o conteúdo do arquivo "<nome_arquivo_response>"

      Examples: Dados para a chamada, e o conteúdo esperado da resposta
        | nome_arquivo_body                                    | nome_arquivo_response                                    |
        | [[FILENAME_BEGIN]]_[[API_VERSION]]_10565022_[[API_OPERATION]]_body_1.json | [[FILENAME_BEGIN]]_[[API_VERSION]]_10565022_[[API_OPERATION]]_response_1.json |
        | [[FILENAME_BEGIN]]_[[API_VERSION]]_10565022_[[API_OPERATION]]_body_2.json | [[FILENAME_BEGIN]]_[[API_VERSION]]_10565022_[[API_OPERATION]]_response_2.json |

