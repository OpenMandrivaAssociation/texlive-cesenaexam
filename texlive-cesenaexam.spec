Name:		texlive-cesenaexam
Version:	44960
Release:	2
Summary:	A class file to typeset exams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cesenaexam
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cesenaexam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cesenaexam.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cesenaexam.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX document class has been designed to typeset exams.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cesenaexam
%{_texmfdistdir}/tex/latex/cesenaexam
%doc %{_texmfdistdir}/doc/latex/cesenaexam

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
