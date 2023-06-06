"""Role testing files using testinfra."""


def test_tailscale_is_installed(host):
    """Check if tailscale is installed."""
    assert host.package("tailscale").is_installed


def test_tailscale_running_and_enabled(host):
    """Check if tailscale is running and enabled."""
    tailscale = host.service("tailscaled")
    assert tailscale.is_running
    assert tailscale.is_enabled
