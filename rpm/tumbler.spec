# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       tumbler

# >> macros
# << macros

Summary:    D-Bus service for thumbnailing
Version:    0.1.22
Release:    1
Group:      Applications/System
License:    GPLv2+
URL:        https://maemo.gitorious.org/maemo-af/tumbler
Source0:    maemo-af-tumbler-meego_0.1.22-1meego2.tar.gz
Source1:    flavors.conf
Source100:  tumbler.yaml
Patch0:     0001-Add-a-x-huge-thumbnail-size-512x512.patch
Patch1:     0002-Add-GStreamer-based-thumbnailer-for-video-thumbnails.patch
Patch2:     0003-fix-tumblerd-segmentfault-error.patch
Patch3:     tumbler-0.1.22-remove-gtk.patch
Patch4:     0002-Replace-python2.6-calls-with-python-calls.patch
Patch5:     tumbler-no-werror-with-debug.patch
Patch6:     0004-nemo-tests-xml-fix.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(quillimagefilter)
BuildRequires:  pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.16.0
BuildRequires:  pkgconfig(dbus-1) >= 1.0.0
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.72
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  python
BuildRequires:  python-imaging
BuildRequires:  dbus-python
BuildRequires:  pygobject2

%description
Tumbler is a D-Bus service for applications to request thumbnails for
various URI schemes and MIME types


%package tests
Summary:    Files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   python-imaging

%description tests
Tests and tests.xml file for %{name} 


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -n maemo-af-%{name}

# 0001-Add-a-x-huge-thumbnail-size-512x512.patch
%patch0 -p1
# 0002-Add-GStreamer-based-thumbnailer-for-video-thumbnails.patch
%patch1 -p1
# 0003-fix-tumblerd-segmentfault-error.patch
%patch2 -p1
# tumbler-0.1.22-remove-gtk.patch
%patch3 -p1
# 0002-Replace-python2.6-calls-with-python-calls.patch
%patch4 -p1
# tumbler-no-werror-with-debug.patch
%patch5 -p1
# 0004-nemo-tests-xml-fix.patch
%patch6 -p1
# >> setup
# << setup

%build
# >> build pre
# Force autotools to run because we patched the configure script
intltoolize --force --copy --automake
autoreconf -v -f -i -I m4
# << build pre

%configure --disable-static \
    --disable-pixbuf-thumbnailer \
    --disable-font-thumbnailer \
    --enable-quill-thumbnailer \
    --disable-xdg-cache \
    --disable-jpeg-thumbnailer \
    --disable-ffmpeg-thumbnailer \
    --disable-poppler-thumbnailer

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/thumbnails/
cp -a %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/thumbnails/


# >> install post
rm -rf %{buildroot}/%{_datadir}/gtk-doc/
# << install post

%find_lang tumbler

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f tumbler.lang
%defattr(-,root,root,-)
# >> files
%{_datadir}/dbus-1/services/org.xfce.Tumbler.Manager1.service
%{_datadir}/dbus-1/services/org.xfce.Tumbler.Cache1.service
%{_datadir}/dbus-1/services/org.xfce.Tumbler.Thumbnailer1.service
%{_libdir}/libtumbler-1.so.*
%{_libdir}/tumbler-1/plugins/tumbler*.so
%{_libdir}/tumbler-1/plugins/cache/tumbler*.so
%{_libdir}/tumbler-1/tumblerd
%{_sysconfdir}/xdg/thumbnails/*.conf
# << files

%files tests
%defattr(-,root,root,-)
# >> files tests
%{_datadir}/tumbler-tests/*
# << files tests

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/tumbler-*
%{_libdir}/libtumbler-1.so
%{_libdir}/pkgconfig/*.pc
# << files devel