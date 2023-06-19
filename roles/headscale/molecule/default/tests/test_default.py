"""Role testing files using testinfra."""


def test_headscale_binary(host):
    """Validate headscale installation."""
    f = host.file("/usr/bin/headscale")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_headscale_port(host):
    """Validate headscale port."""
    s = host.socket("tcp://127.0.0.1:8514")

    assert s.is_listening
