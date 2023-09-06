cloud=('oracle','apple','google','amazon')

ground=list(cloud)
ground.remove('apple')
cloud=tuple(ground)
print(cloud)
