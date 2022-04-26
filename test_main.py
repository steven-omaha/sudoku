from approvaltests import verify

from main import display, parse_grid, grid1, grid2


def test_approvaltest_grid1(capsys):
    display(parse_grid(grid1))
    stdout, _ = capsys.readouterr()
    verify(stdout)


def test_approvaltest_grid2(capsys):
    display(parse_grid(grid2))
    stdout, _ = capsys.readouterr()
    verify(stdout)
