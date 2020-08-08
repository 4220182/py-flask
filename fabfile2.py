from fabric2 import SerialGroup, Connection, Config, task ,ThreadingGroup
import yaml
'''
fabric2 多主机操作
参考：
https://docs.fabfile.org/en/2.5/api/group.html
https://github.com/fabric/fabric/issues/1966
https://www.walkerfree.com/article/194
'''

def base_test():
    g = SerialGroup('127.0.0.1', '192.168.5.102')
    g.run('date')

    hosts = ['127.0.0.1', '192.168.5.102']
    g = SerialGroup(*hosts)
    g.run('date')


def config_test():
    '''
    默认的配置文件~/.fabric.yml 只能使用固定的key，自己增加hosts，是不会被读入。
    :return:
    '''
    for c in Config.global_defaults().items():
        print(c)

@task
def deploy(c):
    '''
    shell USAGE: fab2 deploy -H 192.168.5.102,127.0.0.1
    '''
    c.run('uname -s')

def g_deploy():
    '''
    SerialGroup(*hosts, **kwargs)：按串行方式执行操作
    :return:
    '''
    with SerialGroup(*hosts) as g:
      g.run('uname -s')

def tg_deploy():
    '''
    hreadingGroup(*hosts, **kwargs)：按并发方式执行操作
    :return:
    '''
    with ThreadingGroup(*hosts) as g:
      g.run('uname -s')

if __name__ == '__main__':
    base_test()
    #config_test()

    '''
    从yaml配置文件读取主机组：
    my-hosts.yml 文件内容如下：
    web:
      - 127.0.0.1
      - 192.168.5.102
    '''
    my_hosts = yaml.full_load(open("./my-hosts.yml"))
    hosts = my_hosts['web']

    g_deploy()
    tg_deploy()

    for host in hosts :
        conn = Connection(host)
        deploy(conn)