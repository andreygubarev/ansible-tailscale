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


def test_headscale_dirs(host):
    """Validate headscale directories."""
    d = host.file("/mnt/local/headscale/config")
    assert d.exists
    assert d.is_directory
    assert d.user == "headscale"
    assert d.group == "headscale"
    assert d.mode == 0o750

    d = host.file("/mnt/local/headscale/state")
    assert d.exists
    assert d.is_directory
    assert d.user == "headscale"
    assert d.group == "headscale"
    assert d.mode == 0o750


def test_headscale_default_dirs(host):
    """Validate headscale directories."""
    d = host.file("/etc/headscale")
    assert not d.exists

    d = host.file("/var/lib/headscale")
    assert not d.exists
