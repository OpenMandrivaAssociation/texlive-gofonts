Name:		texlive-gofonts
Version:	64358
Release:	1
Summary:	GoSans and GoMono fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gofonts
License:	other-free lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gofonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gofonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the GoSans and GoMono families of fonts designed by
the Bigelow & Holmes foundry for the Go project. GoSans is
available in three weights: Regular, Medium, and Bold (with
corresponding italics). GoMono is available in regular and
bold, with italics. Notes on the design may be found at
https://blog.golang.org/go-fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gofonts
%{_texmfdistdir}/fonts/vf/bh/gofonts
%{_texmfdistdir}/fonts/type1/bh/gofonts
%{_texmfdistdir}/fonts/truetype/bh/gofonts
%{_texmfdistdir}/fonts/tfm/bh/gofonts
%{_texmfdistdir}/fonts/map/dvips/gofonts
%{_texmfdistdir}/fonts/enc/dvips/gofonts
%doc %{_texmfdistdir}/doc/fonts/gofonts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
