from marketplace.config import context
from marketplace.functions import json_to_tree

from treelib import Tree


def interpolate_procedure_read_change_json(data):
    data = data.replace("{{PROCEDURE_NAME}}", context['procedureName'])
    data = interpolate_transform(data)

    return data


def interpolate_transform(data):
    """
    Refatorar esse metodo para ser generico, vai ficar bom!
    :param data:
    :return:
    """
    tree = json_to_tree(context['paths']['schemas']['post'])
    # tree.show()
    subtree_transform = tree.subtree(nid='transform')

    parents_line_template = 'GetJsonObject("{{PARENT}}"):'
    progress_line_template = 'Has("{{FIELD}}")'

    new_transform = []

    for node in subtree_transform.expand_tree(mode=Tree.WIDTH):
        parents = subtree_transform.get_all_parents(node)
        parents_line = [parents_line_template.replace('{{PARENT}}', parent) for parent in parents]
        progress_line = progress_line_template.replace('{{FIELD}}', node)

        new_transform.append('and vobj-json-element:GetJsonObject("data"):' + ''.join(parents_line) + progress_line)

    data = data.replace('{{TRANSFORM}}', '\n'.join(new_transform))

    return data


def main():
    template = context['paths']['templates']['procedure_read_change_json']
    output = context['paths']['outputs']['procedure_read_change_json']

    with open(template) as stream_template, open(output, 'w') as stream_output:
        data = stream_template.read()
        data = interpolate_procedure_read_change_json(data)
        # print(data)
        stream_output.write(data)
        print(f'Main -> Arquivo gerado: {output}')

    print('Main -> EOF')


if __name__ == '__main__':
    main()
