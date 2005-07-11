#
# Conditional build:
#
Summary:	-
Summary(pl):	-
Name:		gspy
Version:	0.1.8
Release:	0.1
License:	GPL v2
Group:		Applications
#Icon:		-
Source0:	http://gspy.sourceforge.net/%{name}-%{version}-src.tar.gz
#Patch0:		%{name}-what.patch
URL:		http://gspy.sourceforge.net/
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	libtool
#BuildRequires:	-
#PreReq:		-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gspy retrieves images from a video4linux device and processes these
into a daily mpeg movie on the disk drive. Each image is recorded with
a time stamp to insure accurate real world correlation. Special motion
detection algorithms are used to reduce the size of the daily movies
by eliminating pictures with similar content as well as the normal
compression obtained via the mpeg process. The result is a time lapse
video per day with nonlinear time compression using only the images of
interest. This program will only run on Linux machines which support a
video4linux-device in 640x480 capture size. This software has been
tested with the 2.4.0-test1 kernel, 2.4.0-test4 and the 2.2.16 kernel
with the usb backport patch. You should have the Berkeley MPEG Tools
installed if you wish to generate the MPEG files. Gspy can be used
without the MPEG tools, as it will fill a directory with jpg images
that can be processed or viewed at a later time. Versions from 0.1.6
include a user defined command that is executed on each alarm. This
command string can include a token(s) "%f%" that will get replaced
with the alarm picture filename. Typical uses would be to copy the
alarm picture to a remote site using ftp or scp, email the picture to
someone, play a sound annoucement... "Step away from the keyboard!",
turn on lights using a parallel port or X10 interface, or ???. Have
FUN

%description -l pl

%prep
%setup -q -n %{name}
#%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
#%post	-p /sbin/ldconfig

%preun

%postun
#%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and its config
