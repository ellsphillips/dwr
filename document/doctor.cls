%% Start of file `doctor.cls'.
%% Copyright 2021 Elliott Phillips <ellsphillipsuni@gmail.com>
%
% ------------------------------------------------------------------------------

\ProvidesClass{doctor}[%
	2021/01/25 Documentation standard for automated monthly report generation
]
\NeedsTeXFormat{LaTeX2e}

%\DeclareOption{draft}{\setlength\overfullrule{5pt}}
%\DeclareOption{final}{\setlength\overfullrule{0pt}}
%\DeclareOption*{
%	\PassOptionsToClass{\CurrentOption}{book}
%}
%\ProcessOptions\relax

\PassOptionsToPackage{table}{xcolor}

\LoadClass[11pt,oneside]{book}

% ------------------------------------------------------------------------------

\usepackage{%
	lib/colour/monokai-theme,
	lib/colour/languages,
}

\usepackage{%
	lib/fonts,
	lib/graphics,
	lib/page,
	lib/refs,
}

\usepackage{lib/code-blocks/init}

\usepackage{lib/xltabular}

\usepackage{%
	lib/components/plot,
	lib/components/table,
	lib/components/frontpage,
	lib/components/hourglass,
	lib/components/button,
	lib/components/main-points,
	lib/components/toc,
}

\usepackage{lib/theme/init}

% ------------------------------------------------------------------------------

\makeatletter
\providecommand*{\input@path}{}
\g@addto@macro\input@path{{img/}{figures/}}
\makeatother

\RequirePackage{xkeyval}



\DeclareOptionX{theme}{\colorlet{clr-accent}{#1}}

\DeclareOptionX{logo}{\IfFileExists{#1}{\def\companylogo{#1}}{\def\companylogo{}}}

\newif\ifrandombanner
\DeclareOptionX{banner}{%
	\ifthenelse{\equal{\detokenize{#1}}{\detokenize{random}}}{%
		\randombannertrue%
	}{%
		\randombannerfalse
		\IfFileExists{#1}{\def\companybanner{#1}}{\def\companybanner{}}%
	}%
}

\newif\ifhourglass
\DeclareOptionX{hourglass}{\hourglasstrue}

\DeclareOptionX{lightmode}{\monokailightmode}
\DeclareOptionX{darkmode}{\monokaidarkmode}
\ExecuteOptionsX{lightmode}



\DeclareOptionX*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptionsX \relax

% ------------------------------------------------------------------------------
%
%% End of file `doctor.cls'.