from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)
    
@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
