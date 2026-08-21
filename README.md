# py-netif

[FreeCORE](https://freecore.org) carries the TrueNAS CORE 13.3 system forward as an
independently maintained operating system on FreeBSD. TrueNAS CORE 13.3 systems
upgrade straight to FreeCORE 15.0 in place, then continue on the project’s
update train.

Not affiliated with or endorsed by iXsystems, Inc.

## What this repository is

`py-netif` forked from [`truenas/py-netif`](https://github.com/truenas/py-netif) at:

| | |
|---|---|
| **Base commit** | `9298aa968e24c423caa35d2ea4f960d487f1bf10` |
| **Base** | truenas/13.3-stable @ 2024-05-03 |
| **Licence** | BSD-2-Clause — unchanged from upstream |

## How to read the history

Upstream history is preserved verbatim below the base commit: original commits,
original authors, original dates. Everything FreeCORE changed sits above it.

```sh
git log --oneline 9298aa968e24..HEAD      # the entire FreeCORE delta
git diff 9298aa968e24..HEAD               # ...as one diff
```

The FreeCORE commits are a compact **release history**, generated from the
reviewed source-state difference rather than copied from the development
repositories. Private commit subjects, issue references, dates, and intermediate
churn are not mirrored here. Only tagged release commits are states that were
built and tested.

## Releases

Tags mark states that were actually built, installed and validated.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to
security@freecore.org, not to the issue tracker — see [SECURITY.md](SECURITY.md).

## Licence and attribution

See [NOTICE](NOTICE) and [TRADEMARKS.md](TRADEMARKS.md). Nothing here is
relicensed; upstream copyright notices and licence texts are preserved.
