from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/tictactoe.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)
    

