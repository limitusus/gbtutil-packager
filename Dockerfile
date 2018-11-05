FROM centos:7

RUN yum groupinstall -y "Development Tools"
RUN yum install -y unzip less vim rpmdevtools
RUN mkdir /rpmbuild
RUN mkdir /rpmbuild/{BUILD,SOURCES,SPECS,RPMS,SRPMS}
RUN mkdir /build/

# tmp
WORKDIR /build
ADD server_utility_command_line_utility_2.0.zip /build/
RUN unzip server_utility_command_line_utility_2.0.zip

ADD rpmmacros /root/.rpmmacros
ADD server_utility_command_line_utility_2.0.zip /rpmbuild/SOURCES
ADD gbt.spec /rpmbuild/SPECS
WORKDIR /rpmbuild/SPECS
RUN rpmbuild -ba gbt.spec
