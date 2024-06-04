#!/bin/python3
from os import path, listdir, walk, makedirs
from argparse import ArgumentParser
from base64 import b85encode, b85decode
from lzma import compress as lzma
from typing import Dict, List


class ResourceFileException(Exception):
    pass

def encode_resource(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        return b85encode(lzma(file.read())).decode()
    raise ResourceFileException(f'Error on read resource {file_path}')

def generate_namespace_init_file(target_path: str, source_path: str) -> None:
    """
    namespace_path: where the actual resources are stored, could be a folder outside
    target_path: the folder where to store the resource __init__.py
    """
    init_file_path: str = path.join(target_path, '__init__.py')
    out: Dict[str, str] = {}
    
    for root, dirs, files in walk(source_path):
        for file in files:
            if file != '__init__.py':
                file_path = path.join(root, file)
                if path.isfile(file_path):
                    out[file] = encode_resource(file_path)
    
    with open(init_file_path, 'w') as init_file:
        init_file.write('# data file\n\ndata = {\n')
        for name, data in out.items():
            init_file.write(f"    '{name}': b'{data}',\n")
        init_file.write('}\n')
        init_file.close()

def generate_resources_init_file(resources_path: str, actual_path: str, namespaces: List[str]) -> None:
    init_file_path = path.join(resources_path, '__init__.py')
    namespace_block = ''
    for namespace in namespaces:
        namespace_block += f"{' ' * 8}if namespace == '{namespace}':\n{' ' * 12}from . import {namespace}\n{' ' * 12}return lzma(b85decode({namespace}.data[name]))\n"
    
    with open(init_file_path, 'w') as init_file:
        init_file.write('''
from os.path import dirname
from os import path
from base64 import b85decode
from lzma import decompress as lzma
        
def get(namespace, name):
    file_path = path.join('{actual_path}', namespace, name)
    if path.exists(file_path):
        with open(file_path, 'rb') as file:
            return file.read()
    try:
{namespace_block}
        raise ImportError(f'Namespace not found: {namespace}')
    except (ImportError, KeyError):
        raise FileNotFoundError(f'Resource not found: {namespace}/{name}')
    '''.strip().replace('{namespace_block}', namespace_block))

def generate_resource_files(package_name: str, resources_path: str, source_path: str) -> None:
    if not path.isdir(resources_path):
        raise ValueError(f"Invalid resources path: {resources_path}")
    if not path.isdir(source_path):
        raise ValueError(f"Invalid actual path: {source_path}")
    
    namespaces: List[str] = []
    for namespace in listdir(source_path):
        if not path.isdir(path.join(source_path, namespace)):
            continue
        namespaces.append(namespace)
        namespace_path = path.join(resources_path, namespace)
        if not path.isdir(namespace_path):
            makedirs(namespace_path)
        generate_namespace_init_file(namespace_path, path.join(source_path, namespace))
    
    generate_resources_init_file(resources_path, source_path, namespaces)

if __name__ == '__main__':
    parser = ArgumentParser(description='Generate resource files for a package.')
    parser.add_argument('package_name', help='Name of the package')
    parser.add_argument('resources_path', help='Path to the resources directory')
    parser.add_argument('--source_path', '-s', default=None, help='Actual path of the actual resource files')
    
    args = parser.parse_args()
    
    try:
        generate_resource_files(args.package_name, args.resources_path, args.source_path or args.resources_path)
    except ValueError as e:
        print(f"Error: {str(e)}")
