
load("@subpar//:subpar.bzl", "par_binary")
load("@requirements//:requirements.bzl", "requirement")

par_binary(
    name='piazza_simulator',
    srcs=['main.py'],
    main='main.py',
    data=['model.json'],
    deps=[
        requirement('markovify')
    ],
    visibility=['//visibility:public']
)