import setuptools

with open('README.md', mode='r', encoding='utf-8') as md:
    description = md.read()

with open('requirements.txt', mode='r', encoding='utf-8') as req:
    requirements = sorted(req.read().lower().strip('\n').split('\n'))

with open('requirements.txt', mode='w', encoding='utf-8') as req:
    req.write('\n'.join(requirements))

setuptools.setup(
    name='amiyahttp',
    version='0.0.4',
    author='vivien8261',
    author_email='826197021@qq.com',
    url='https://www.amiyabot.com/develop/advanced/httpSupport.html',
    license='MIT Licence',
    description='对 FastApi 进行二次封装的简易 HTTP Web 服务 SDK',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(include=['amiyahttp', 'amiyahttp.*']),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=requirements,
)

# python setup.py bdist_wheel
# twine upload dist/*
