import argparse
import git


def get_version():
    repo = git.Repo('.')
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    if len(tags) == 0:
        return '0.0.0'
    else:
        latest_tag = tags[-1]
        return latest_tag.name


def update_version(new_version=None):
    if not new_version:
        version = get_version()
        version_list = version.split('.')
        version_list[-1] = str(int(version_list[-1]) + 1)
        new_version = '.'.join(version_list)
    repo = git.Repo('.')
    new_tag = repo.create_tag(new_version, message='Updated version "{0}"'.format(new_version))
    repo.remotes.origin.push(new_tag)

    if not new_version:
        print('from {} to {}'.format(version, new_version))
    else:
        print('set {}'.format(new_version))


def main():
    parser = argparse.ArgumentParser(description='Versioning Utilities')
    parser.add_argument('-v', '--version', dest='show_version', action='store_true', help='show version')
    parser.add_argument('-umv', '--update-minor-version', dest='update_minor_version', action='store_true',
                        help='update the minor version on git repository')
    parser.add_argument('-uv', '--update-version', dest='new_version', action='store', type=str,
                        help='update the version on git repository')

    args = parser.parse_args()
    if args.show_version:
        print(get_version())

    if args.update_minor_version:
        update_version()

    if args.new_version:
        update_version(new_version=args.new_version)


if __name__ == '__main__':
    main()
