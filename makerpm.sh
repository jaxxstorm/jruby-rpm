#!/usr/bin/env sh

VERSION="1.7.9-1"

echo "running rpmlint"
rpmlint SPECS/jruby.spec
echo "running spectool"
spectool -C SOURCES -g SPECS/jruby.spec
echo "running rpmbuild"
rpmbuild --define "_topdir `pwd`" -bs SPECS/jruby.spec
rpmlint SRPMS/jruby-${VERSION}.el6.src.rpm
mock --resultdir `pwd`/RPMS `pwd`/SRPMS/jruby-${VERSION}.el6.src.rpm
rpmlint -f .rpmlint RPMS/*.rpm
