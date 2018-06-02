from invoke import run, task


@task
def grammar(context):
    run("antlr4 -Dlanguage=Python3 -package grammar -visitor -no-listener gsl_protocol/grammar/HedgehogProtocol.g4")
    run("g4v gsl_protocol/grammar/HedgehogProtocolVisitor.g4v")
