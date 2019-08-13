import json
import setuptools
import glob

def parse_setup_py(fn) -> object:
    # replace this with imp.from_source or similar instead of compile
    with open(fn) as fh:
        code = compile(fh.read(), 'foo', 'exec')
        l = {}
        g = {}
        exec(code, g, l)
        return l.get('INSTALL_REQUIRES', []), l.get('TESTS_REQUIRE', [])

def main():
    install_dependencies = []
    test_dependencies = []
    for fn in glob.glob('**/setup.py'):
        install, tests = parse_setup_py(fn)
        install_dependencies += install
        test_dependencies += tests

    manifest = [
           open(fn).read().strip() for fn in glob.glob('**/MANIFEST.in')
    ]


    install_dependencies = list((d for d in set(install_dependencies) if not d.startswith('stcg-')))
    test_dependencies = list((d for d in set(test_dependencies) if not d.startswith('stcg-')))

    print(json.dumps(dict(install_requires=install_dependencies, test_dependencies=test_dependencies, manifest=manifest)))

if __name__ == "__main__":
    main()
