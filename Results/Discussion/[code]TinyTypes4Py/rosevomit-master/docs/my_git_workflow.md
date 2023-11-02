# My Git workflow

## Why write these down?

Why try to write down my own rules for a Git workflow?

## Workflow overview

1. Check out a personal branch `u/<initials>/<feature>` from `master`
1. Do work on that personal branch until satisfied
1. Squash and rebase `u/<initials>/<feature>` onto `master`, sometimes creating temporary branches to assist in organizing everything
1. Delete `u/<initials>/<feature>`

## A guide to branches

My permanent branches are:

- `master`
- `released/`
  - `latest`

However, you may see some of these as well.

- `rc/` is for "release candidates" - basically, a place for me to do some final checks 
- `released/`
  - `v1.x`
- `u/` is reserved for personal work branches. These branches might exist for a few hours, or a day, or even a few weeks, but they're inherently temporary and reflect whatever I'm currently tinkering with.
  - `al`
    - `future` indicates a work in progress that I've decided to shelve for now, to be included in a future version.
    - `<some identifying name>`
  - `<other initials>` - Someone else's personal work branches.

Note that `u/al/` branches **do not** need chronologically unique names. It is fine, for instance, to have a branch named `u/al/wip`, squash and rebase it into `master`, and then create another branch named `u/al/wip` a day later.

## A typical workflow

````text
u/al/feature1 --(squash and rebase onto)--> master
master --(create a temporary branch)--> rc/Major.Minor.Patch-rc1

````
