Feature: [[API_TITLE]] [[API_VERSION]] (BR)

    Como usuário do sistema
    Eu quero acessar [[FEATURE_TITLE_ARTICLE]] [[API_TITLE_LOWER]]
    De modo que eu possa gerenciá-[[FEATURE_TITLE_ARTICLE_COMPLEMENT]]

    @[[API_OPERATION_BR]]
    @api
    @br
    @erro
    @eventcontext_invalido
    @post
    @status_404
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_eventcontext_invalido
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com eventContext inválido
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 404
      And   a API responde a mensagem "Employee not found for this AOID."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                               |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_01.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_02.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_03.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_04.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_05.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_06.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_07.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_eventcontext_invalido_404_08.json |

    @[[API_OPERATION_BR]]
    @api
    @br
    @erro
    @identificadores_invalidos
    @post
    @status_400
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_identificadores_invalidos
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com identificadores inválidos
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "<mensagem>"

      Examples: Dados para a chamada, e a mensagem esperada da resposta
        | nome_arquivo_body                                                                   | mensagem                                                                                                                              |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_01.json | The eventID is mandatory, this field should contain the ID set by your system to this transaction.                                    |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_02.json | The eventID is mandatory, this field should contain the ID set by your system to this transaction.                                    |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_03.json | The serviceCategoryCode/shortName is mandatory, this field should contain the category of the API according to the API documentation. |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_04.json | The serviceCategoryCode/shortName is mandatory, this field should contain the category of the API according to the API documentation. |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_05.json | The serviceCategoryCode/shortName is mandatory, this field should contain the category of the API according to the API documentation. |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_06.json | The eventNameCode/shortName is mandatory, this field should contain the code of the API according to the API documentation.           |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_07.json | The eventNameCode/shortName is mandatory, this field should contain the code of the API according to the API documentation.           |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_08.json | The eventNameCode/shortName is mandatory, this field should contain the code of the API according to the API documentation.           |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_09.json | The eventTitle is mandatory, this field should contain the name of the API according to the API documentation.                        |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_10.json | The eventTitle is mandatory, this field should contain the name of the API according to the API documentation.                        |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_11.json | The eventTitle is mandatory, this field should contain the name of the API according to the API documentation.                        |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_12.json | The recordDateTime is mandatory, this field should contain the time of the change in your system.                                     |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_13.json | The recordDateTime is mandatory, this field should contain the time of the change in your system.                                     |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_14.json | The recordDateTime is mandatory, this field should contain the time of the change in your system.                                     |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_15.json | The creationDateTime is mandatory, this field should contain the time of the change in your system.                                   |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_16.json | The creationDateTime is mandatory, this field should contain the time of the change in your system.                                   |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_identificadores_invalidos_400_17.json | The creationDateTime is mandatory, this field should contain the time of the change in your system.                                   |

    @[[API_OPERATION_BR]]
    @api
    @br
    @mais_de_um_objeto
    @post
    @status_400
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_mais_de_um_objeto
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com mais de um objeto
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "This API accepts only one change per call."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                          |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_mais_de_um_objeto_400_1.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_mais_de_um_objeto_400_2.json |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_mais_de_um_objeto_400_3.json |

    @[[API_OPERATION_BR]]
    @api
    @br
    @erro
    @post
    @queries_invalidas
    @status_406
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_queries_invalidas
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com queries inválidas
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com a query "<query>" e o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 406
      And   a API responde a mensagem "The server does not recognize the parameters sent."

      Examples: Dados para a chamada (combinação de comandos)
        | query          | nome_arquivo_body                                                        |
        | $skip=1&$top=1 | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_queries_invalidas_406.json |

      Examples: Dados para a chamada (skip)
        | query   | nome_arquivo_body                                                        |
        | $skip=1 | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_queries_invalidas_406.json |

      Examples: Dados para a chamada (top)
        | query  | nome_arquivo_body                                                        |
        | $top=1 | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_queries_invalidas_406.json |

    @[[API_OPERATION_BR]]
    @api
    @br
    @erro
    @post
    @status_400
    @transform_invalido
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_transform_invalido
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com transform inválido
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "<mensagem>"

      Examples: Dados para a chamada, e a mensagem esperada da resposta
        | nome_arquivo_body                                                            | mensagem                 |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_transform_invalido_400_01.json | Invalid payment method.  |

    @[[API_OPERATION_BR]]
    @api
    @br
    @erro
    @post
    @status_400
    @usuarios_inativos
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_usuarios_inativos
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com usuários inativos
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "217651535" e do usuário "MKP_217651535_User.Inactive_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "Invalid Associate ID (Invalid credentials)."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                           |
        | [[FILENAME_BEGIN]]_217651535_[[API_OPERATION]]_body_usuarios_inativos_400_1.json |

    @[[API_OPERATION_BR]]
    @api
    @br
    @erro
    @post
    @status_404
    @usuarios_com_restricoes
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_usuarios_com_restricoes
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com usuários com restrições
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "<cliente>" e do usuário "<usuario>"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 404
      And   a API responde a mensagem "Employee not found for this AOID."

      Examples: Dados para a chamada
        | cliente   | usuario                                            | nome_arquivo_body                                                                 |
        | 10565022  | MKP_10565022_User.Automation_practitioner          | [[FILENAME_BEGIN]]_217651535_[[API_OPERATION]]_body_usuarios_com_restricoes_404_1.json |
        | 217651535 | MKP_217651535_User.EstabTodosMenos028_practitioner | [[FILENAME_BEGIN]]_217651535_[[API_OPERATION]]_body_usuarios_com_restricoes_404_2.json |

    @[[API_OPERATION_BR]]
    @api
    @br
    @erro
    @post
    @status_404
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @worker_demitido
    @[[API_OPERATION_BR]]_worker_demitido
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com worker demitido
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "217651535" e do usuário "MKP_217651535_User.Automation_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 404
      And   a API responde a mensagem "Change not accepted for terminated employees."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                         |
        | [[FILENAME_BEGIN]]_217651535_[[API_OPERATION]]_body_worker_demitido_404_1.json |

    @[[API_OPERATION_BR]]
    @api
    @br
    @post
    @status_200
    @sucesso
    @usuarios_ativos
    @[[API_TITLE_UNDERLINED]]_[[API_VERSION]]
    @[[API_OPERATION_BR]]_usuarios_ativos
    Scenario Outline: [[API_OPERATION_CAPITALIZED_BR]] um [[API_TITLE_LOWER]], com usuários ativos
      Given que sou um usuário consultando o recurso "[[API_SERVICE]]" da API "[[API_SERVICE_GROUP]]" versão "[[API_VERSION]]"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 200

      Examples: Dados para a chamada
        | nome_arquivo_body                                                  |
        | [[FILENAME_BEGIN]]_10565022_[[API_OPERATION]]_body_usuarios_ativos.json |
