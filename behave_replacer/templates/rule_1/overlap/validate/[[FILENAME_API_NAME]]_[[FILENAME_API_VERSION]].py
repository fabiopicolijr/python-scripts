from behave import when

from marketplace.features.data import obter_conteudo_arquivo


# region given


# endregion
# region when
@when(
    'envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com a query "{query}" '
    'e o body contendo o conteúdo do arquivo "{nome_arquivo}"'
)
def step_impl(context, query, nome_arquivo):
    body = obter_conteudo_arquivo(context.pastas["inputs"], nome_arquivo)

    context.service.definir_url(query=query)
    context.resposta = context.service.[[API_OPERATION_BR]](body)


@when(
    "envio uma chamada para [[API_OPERATION_BR]] um [[API_TITLE_LOWER]] com o body contendo o "
    'conteúdo do arquivo "{nome_arquivo}"'
)
def step_impl(context, nome_arquivo):
    body = obter_conteudo_arquivo(context.pastas["inputs"], nome_arquivo)

    context.service.definir_url()
    context.resposta = context.service.[[API_OPERATION_BR]](body)


# endregion
# region then


# endregion
