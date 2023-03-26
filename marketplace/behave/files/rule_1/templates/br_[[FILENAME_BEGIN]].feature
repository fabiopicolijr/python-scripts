Feature: Worker Pay Distributions v1 (BR)

    Como usuário do sistema
    Eu quero acessar os worker pay distributions
    De modo que eu possa gerenciá-los

    @alterar
    @api
    @br
    @erro
    @headers_invalidos
    @post
    @status_400
    @status_404
    @status_406
    @status_412
    @worker_pay_distributions_v1
    @alterar_headers_invalidos
    Scenario Outline: Alterar um worker pay distributions, com headers inválidos
      Given que sou um usuário consultando o recurso "pay distributions change" da API "worker pay distributions" versão "v1"
      And   tenho os headers accept "<accept>", associateoid "<aoid>", content-type "<content_type>", language "<language>", orgoid "<ooid>", realm "<realm>", rolecode "<rolecode>" e sor "<sor>"
      When  envio uma chamada para alterar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status <codigo_status>
      And   a API responde a mensagem "<mensagem>"

      Examples: Dados para a chamada, e a mensagem esperada da resposta
        | accept           | aoid             | content_type     | language | ooid          | realm | rolecode      | sor      | nome_arquivo_body                                                            | codigo_status | mensagem                                               |
        | */*              | null             | application/json | ""       | null          | null  | null          | null     | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | */*              | null             | application/json | EN-US    | null          | null  | null          | null     | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | null             | BR0MAJE4052IJC93 | application/json | null     | null          | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | null          | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | */*              | ""               | application/json | EN-US    | ""            | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | */*              | 1                | application/json | EN-US    | ""            | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | */*              | INVALIDO         | application/json | EN-US    | ""            | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | ""            | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID is mandatory.                                   |
        | */*              | 1                | application/json | EN-US    | 1             | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID not found.                                      |
        | */*              | 1                | application/json | EN-US    | INVALIDO      | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID not found.                                      |
        | */*              | INVALIDO         | application/json | EN-US    | 1             | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID not found.                                      |
        | */*              | INVALIDO         | application/json | EN-US    | INVALIDO      | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID not found.                                      |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | 1             | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID not found.                                      |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | INVALIDO      | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID not found.                                      |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR42345220322 | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | OrgOID not found.                                      |
        | null             | BR0M7BD0914MTKTK | application/json | null     | BR0010565022  | realm | practitioner  | null     | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | SOR is mandatory.                                      |
        | */*              | BR0M7BD0914MTKTK | application/json | EN-US    | BR0010565022  | realm | practitioner  | null     | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | SOR is mandatory.                                      |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | practitioner  | ""       | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | SOR is mandatory.                                      |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | practitioner  | INVALIDO | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | The server does not recognize the chosen SOR.          |
        | */*              | BR0MAJE4052IJC93 | application/json | DE       | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | The server does not recognize the chosen Language.     |
        | */*              | BR0MAJE4052IJC93 | application/json | FR       | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_400.json | 400           | The server does not recognize the chosen Language.     |
        | null             | null             | application/json | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_404.json | 404           | The user has no access to this API.                    |
        | */*              | null             | application/json | null     | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_404.json | 404           | The user has no access to this API.                    |
        | */*              | ""               | application/json | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_404.json | 404           | The user has no access to this API.                    |
        | */*              | 1                | application/json | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_404.json | 404           | The user has no access to this API.                    |
        | */*              | INVALIDO         | application/json | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_404.json | 404           | The user has no access to this API.                    |
        | */*              | BR00000001611600 | application/json | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_404.json | 404           | The user has no access to this API.                    |
        | ""               | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_406.json | 406           | The server does not recognize the chosen Accept value. |
        | application/json | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_406.json | 406           | The server does not recognize the chosen Accept value. |
        | */*              | BR0MAJE4052IJC93 | text/plain       | EN-US    | BR0217651535  | realm | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_406.json | 406           | The server does not recognize the chosen Content Type. |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | null  | practitioner  | eXpert   | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen Realm.        |
        | null             | BR0MAJE4052IJC93 | application/json | null     | BR0217651535  | null  | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen Realm.        |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | null  | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen Realm.        |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | ""    | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen Realm.        |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | "''"  | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen Realm.        |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | '""'  | practitioner  | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen Realm.        |
        | null             | BR0MAJE4052IJC93 | application/json | null     | BR0217651535  | realm | null          | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | null          | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | ES-CL    | BR0217651535  | realm | null          | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | RoleCode no esperado o invalido.                       |
        | */*              | BR0MAJE4052IJC93 | application/json | PT-BR    | BR0217651535  | realm | null          | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | RoleCode não reconhecido ou inválido.                  |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | ""            | ""       | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | ""            | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | INVALIDO      | INVALIDO | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | INVALIDO      | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | administrator | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | employee      | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | manager       | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |
        | */*              | BR0MAJE4052IJC93 | application/json | EN-US    | BR0217651535  | realm | supervisor    | eXpertBR | worker_pay_distributions_v1_217651535_change_body_headers_invalidos_412.json | 412           | The server does not recognize the chosen RoleCode.     |

    @alterar
    @api
    @br
    @headers_validos
    @post
    @status_200
    @sucesso
    @worker_pay_distributions_v1
    @alterar_headers_validos
    Scenario Outline: Alterar um worker pay distributions, com headers válidos
      Given que sou um usuário consultando o recurso "pay distributions change" da API "worker pay distributions" versão "v1"
      And   tenho os headers accept "<accept>", associateoid "<aoid>", content-type "<content_type>", language "<language>", orgoid "<ooid>", realm "<realm>", rolecode "<rolecode>" e sor "<sor>"
      When  envio uma chamada para alterar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 200

      Examples: Dados para a chamada
        | accept | aoid             | content_type     | language | ooid         | realm | rolecode     | sor      | nome_arquivo_body                                                     |
        | null   | BR0M7BD0914MTKTK | null             | null     | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | null   | BR0M7BD0914MTKTK | application/json | EN-US    | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | null             | EN-US    | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | ""               | EN-US    | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | application/json | null     | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | application/json | ""       | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | application/json | EN-US    | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | application/json | ES-CL    | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | application/json | PT-BR    | BR0010565022 | realm | practitioner | eXpert   | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |
        | */*    | BR0M7BD0914MTKTK | application/json | PT-BR    | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_headers_validos.json |

    @alterar
    @api
    @br
    @outros_headers
    @post
    @status_200
    @sucesso
    @worker_pay_distributions_v1
    @alterar_outros_headers
    Scenario Outline: Alterar um worker pay distributions, com outros headers
      Given que sou um usuário consultando o recurso "pay distributions change" da API "worker pay distributions" versão "v1"
      And   tenho os headers adp-action-reason "<reason>", adp-my-test "<test>", associateoid "<aoid>", orgoid "<ooid>", realm "<realm>", rolecode "<rolecode>" e sor "<sor>"
      When  envio uma chamada para alterar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 200

      Examples: Dados para a chamada
        | reason | test | aoid             | ooid         | realm | rolecode     | sor      | nome_arquivo_body                                                    |
        | null   | null | BR0M7BD0914MTKTK | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_outros_headers.json |
        | reason | test | BR0M7BD0914MTKTK | BR0010565022 | realm | practitioner | eXpertBR | worker_pay_distributions_v1_10565022_change_body_outros_headers.json |
