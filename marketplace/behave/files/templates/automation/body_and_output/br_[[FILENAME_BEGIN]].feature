Feature: Worker Pay Distributions v1 (BR)

    Como usuário do sistema
    Eu quero acessar os worker pay distributions
    De modo que eu possa gerenciá-los

    @cadastrar
    @api
    @br
    @comparando_resposta
    @[[API_METHOD]]
    @status_200
    @sucesso
    @worker_pay_distributions_v1
    @cadastrar_comparando_resposta
    Scenario Outline: Cadastrar um worker pay distributions, comparando o conteúdo esperado da resposta
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And  tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then a API responde o código de status 200
      And  a API responde o conteúdo do arquivo "<nome_arquivo_response>"

      Examples: Dados para a chamada, e o conteúdo esperado da resposta
        | nome_arquivo_body                                    | nome_arquivo_response                                    |
        | worker_pay_distributions_v1_10565022_add_body_1.json | worker_pay_distributions_v1_10565022_add_response_1.json |
        | worker_pay_distributions_v1_10565022_add_body_2.json | worker_pay_distributions_v1_10565022_add_response_2.json |

    @cadastrar
    @api
    @br
    @erro
    @eventcontext_invalido
    @[[API_METHOD]]
    @status_404
    @worker_pay_distributions_v1
    @cadastrar_eventcontext_invalido
    Scenario Outline: Cadastrar um worker pay distributions, com eventContext inválido
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 404
      And   a API responde a mensagem "Employee not found for this AOID."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                               |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_01.json |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_02.json |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_03.json |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_04.json |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_05.json |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_06.json |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_07.json |
        | worker_pay_distributions_v1_10565022_add_body_eventcontext_invalido_404_08.json |

    @cadastrar
    @api
    @br
    @erro
    @identificadores_invalidos
    @[[API_METHOD]]
    @status_400
    @worker_pay_distributions_v1
    @cadastrar_identificadores_invalidos
    Scenario Outline: Cadastrar um worker pay distributions, com identificadores inválidos
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "<mensagem>"

      Examples: Dados para a chamada, e a mensagem esperada da resposta
        | nome_arquivo_body                                                                   | mensagem                                                                                                                              |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_01.json | The eventID is mandatory, this field should contain the ID set by your system to this transaction.                                    |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_02.json | The eventID is mandatory, this field should contain the ID set by your system to this transaction.                                    |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_03.json | The serviceCategoryCode/shortName is mandatory, this field should contain the category of the API according to the API documentation. |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_04.json | The serviceCategoryCode/shortName is mandatory, this field should contain the category of the API according to the API documentation. |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_05.json | The serviceCategoryCode/shortName is mandatory, this field should contain the category of the API according to the API documentation. |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_06.json | The eventNameCode/shortName is mandatory, this field should contain the code of the API according to the API documentation.           |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_07.json | The eventNameCode/shortName is mandatory, this field should contain the code of the API according to the API documentation.           |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_08.json | The eventNameCode/shortName is mandatory, this field should contain the code of the API according to the API documentation.           |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_09.json | The eventTitle is mandatory, this field should contain the name of the API according to the API documentation.                        |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_10.json | The eventTitle is mandatory, this field should contain the name of the API according to the API documentation.                        |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_11.json | The eventTitle is mandatory, this field should contain the name of the API according to the API documentation.                        |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_12.json | The recordDateTime is mandatory, this field should contain the time of the change in your system.                                     |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_13.json | The recordDateTime is mandatory, this field should contain the time of the change in your system.                                     |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_14.json | The recordDateTime is mandatory, this field should contain the time of the change in your system.                                     |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_15.json | The creationDateTime is mandatory, this field should contain the time of the change in your system.                                   |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_16.json | The creationDateTime is mandatory, this field should contain the time of the change in your system.                                   |
        | worker_pay_distributions_v1_10565022_add_body_identificadores_invalidos_400_17.json | The creationDateTime is mandatory, this field should contain the time of the change in your system.                                   |

    @cadastrar
    @api
    @br
    @mais_de_um_objeto
    @[[API_METHOD]]
    @status_400
    @worker_pay_distributions_v1
    @cadastrar_mais_de_um_objeto
    Scenario Outline: Cadastrar um worker pay distributions, com mais de um objeto
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "This API accepts only one change per call."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                          |
        | worker_pay_distributions_v1_10565022_add_body_mais_de_um_objeto_400_1.json |
        | worker_pay_distributions_v1_10565022_add_body_mais_de_um_objeto_400_2.json |
        | worker_pay_distributions_v1_10565022_add_body_mais_de_um_objeto_400_3.json |

    @cadastrar
    @api
    @br
    @erro
    @[[API_METHOD]]
    @queries_invalidas
    @status_406
    @worker_pay_distributions_v1
    @cadastrar_queries_invalidas
    Scenario Outline: Cadastrar um worker pay distributions, com queries inválidas
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com a query "<query>" e o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 406
      And   a API responde a mensagem "The server does not recognize the parameters sent."

      Examples: Dados para a chamada (combinação de comandos)
        | query          | nome_arquivo_body                                                        |
        | $skip=1&$top=1 | worker_pay_distributions_v1_10565022_add_body_queries_invalidas_406.json |

      Examples: Dados para a chamada (skip)
        | query   | nome_arquivo_body                                                        |
        | $skip=1 | worker_pay_distributions_v1_10565022_add_body_queries_invalidas_406.json |

      Examples: Dados para a chamada (top)
        | query  | nome_arquivo_body                                                        |
        | $top=1 | worker_pay_distributions_v1_10565022_add_body_queries_invalidas_406.json |

    @cadastrar
    @api
    @br
    @erro
    @[[API_METHOD]]
    @status_400
    @transform_invalido
    @worker_pay_distributions_v1
    @cadastrar_transform_invalido
    Scenario Outline: Cadastrar um worker pay distributions, com transform inválido
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "<mensagem>"

      Examples: Dados para a chamada, e a mensagem esperada da resposta
        | nome_arquivo_body                                                            | mensagem                 |
        | worker_pay_distributions_v1_10565022_add_body_transform_invalido_400_01.json | Invalid payment method.  |

    @cadastrar
    @api
    @br
    @[[API_METHOD]]
    @status_200
    @sucesso
    @usuarios_ativos
    @worker_pay_distributions_v1
    @cadastrar_usuarios_ativos
    Scenario Outline: Cadastrar um worker pay distributions, com usuários ativos
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "10565022" e do usuário "MKP_10565022_User.Automation_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 200

      Examples: Dados para a chamada
        | nome_arquivo_body                                                  |
        | worker_pay_distributions_v1_10565022_add_body_usuarios_ativos.json |

    @cadastrar
    @api
    @br
    @erro
    @[[API_METHOD]]
    @status_404
    @usuarios_com_restricoes
    @worker_pay_distributions_v1
    @cadastrar_usuarios_com_restricoes
    Scenario Outline: Cadastrar um worker pay distributions, com usuários com restrições
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "<cliente>" e do usuário "<usuario>"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 404
      And   a API responde a mensagem "Employee not found for this AOID."

      Examples: Dados para a chamada
        | cliente   | usuario                                            | nome_arquivo_body                                                                 |
        | 10565022  | MKP_10565022_User.Automation_practitioner          | worker_pay_distributions_v1_217651535_add_body_usuarios_com_restricoes_404_1.json |
        | 217651535 | MKP_217651535_User.EstabTodosMenos028_practitioner | worker_pay_distributions_v1_217651535_add_body_usuarios_com_restricoes_404_2.json |

    @cadastrar
    @api
    @br
    @erro
    @[[API_METHOD]]
    @status_400
    @usuarios_inativos
    @worker_pay_distributions_v1
    @cadastrar_usuarios_inativos
    Scenario Outline: Cadastrar um worker pay distributions, com usuários inativos
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "217651535" e do usuário "MKP_217651535_User.Inactive_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 400
      And   a API responde a mensagem "Invalid Associate ID (Invalid credentials)."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                           |
        | worker_pay_distributions_v1_217651535_add_body_usuarios_inativos_400_1.json |

    @cadastrar
    @api
    @br
    @erro
    @[[API_METHOD]]
    @status_404
    @worker_pay_distributions_v1
    @worker_demitido
    @cadastrar_worker_demitido
    Scenario Outline: Cadastrar um worker pay distributions, com worker demitido
      Given que sou um usuário consultando o recurso "pay distributions add" da API "worker pay distributions" versão "v1"
      And   tenho os headers do cliente "217651535" e do usuário "MKP_217651535_User.Automation_practitioner"
      When  envio uma chamada para cadastrar um worker pay distributions com o body contendo o conteúdo do arquivo "<nome_arquivo_body>"
      Then  a API responde o código de status 404
      And   a API responde a mensagem "Change not accepted for terminated employees."

      Examples: Dados para a chamada
        | nome_arquivo_body                                                         |
        | worker_pay_distributions_v1_217651535_add_body_worker_demitido_404_1.json |
