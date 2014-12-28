Summary:	A GNOME Security Camera
Summary(pl.UTF-8):	Kamera bezpieczeństwa GNOME
Name:		gspy
Version:	0.1.8
Release:	0.2
License:	GPL v2
Group:		Applications
Source0:	http://gspy.sourceforge.net/%{name}-%{version}-src.tar.gz
# Source0-md5:	b8cdf73e0e11f0294bf979e195e66d32
Patch0:		%{name}-asm_prog.patch
URL:		http://gspy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtkxmhtml-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gspy retrieves images from a video4linux device and processes these
into a daily MPEG movie on the disk drive. Each image is recorded with
a time stamp. Special motion detection algorithms are used to reduce
the size of the daily movies by eliminating pictures with similar
content The result is a time lapse video per day with nonlinear time
compression using only the images of interest. Recent versions include
a user defined command that is executed on each alarm. Typical uses 
would be to copy the alarm picture to a remote site using ftp or scp, 
email the picture to someone, play a sound annoucement... 

%description -l pl.UTF-8
Gspy pobiera obrazy z urządzenia video4linux i przetwarza je na
dzienne filmy MPEG archiwizowane na dysku. Każdy obraz jest nagrywany
ze znacznikiem czasu. Specjalne algorytmy wykrywania ruchu są
wykorzystywane aby zredukować wielkość filmów przez eliminowanie
obrazów z podobną zawartością. Efektem jest spowolniony obraz wideo z
nieliniową kompresją czasu tylko na podstawie obrazów wartych uwagi.
Ostatnie wersje potrafią uruchamiać komendy zdefiniowane przez użytkownika
Typowe zastosowania to kopiowanie alarmującego zdjęcia przez ftp/scp, 
wysłanie e-mailem czy odtworzenie komunikatu... 

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
