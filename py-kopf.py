import kopf

'''
group_name version 资源
例如：
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: ephemeralvolumeclaims.zalando.org
spec:
  scope: Namespaced
  group: zalando.org
  names:
    kind: EphemeralVolumeClaim
    plural: ephemeralvolumeclaims
    singular: ephemeralvolumeclaim
    shortNames:
      - evcs
      - evc
  versions:
    - name: v1
    
@kopf.on.create('zalando.org', 'v1', 'EphemeralVolumeClaim')    
'''
@kopf.on.create('', 'v1', 'services')
def create_fn_xxx(meta, spec, logger, **kwargs):
    print(f"creating service with {meta}")
    print(f"cluster ip is {spec['clusterIP']}")


@kopf.on.delete('', 'v1', 'services')
def delete_fn_xxx(meta, spec, logger, **kwargs):
    print(f"deleting service with {meta}")
    print(f"cluster ip is {spec['clusterIP']}")