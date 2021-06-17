%% Start of file `doctor.cls'.
%% Copyright 2021 Elliott Phillips <elliott.phillips@ons.gov.uk>
%

% -------------------------------------------------------------------------------
% Class options
% -------------------------------------------------------------------------------

\ProvidesClass{doctor}[%
	2021/01/25 Documentation standard for automated monthly report generation
]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption{draft}{\setlength\overfullrule{5pt}}
\DeclareOption{final}{\setlength\overfullrule{0pt}}
\DeclareOption*{
	\PassOptionsToClass{\CurrentOption}{book}
}
\ProcessOptions\relax

\PassOptionsToPackage{table}{xcolor}

\LoadClass[11pt,oneside]{book}



% -------------------------------------------------------------------------------
% Directory locations configuration
% -------------------------------------------------------------------------------
% Configure a directory location for fonts(default: 'fonts/')
\newcommand*{\fontdir}[1][fonts/]{\def\@fontdir{#1}}
\fontdir

\usepackage[]{helvet}
\fontfamily{phv}\selectfont
\renewcommand{\familydefault}{\sfdefault}



% -------------------------------------------------------------------------------
% 3rd party packages
% -------------------------------------------------------------------------------

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{textcomp}
\usepackage{gensymb}
\usepackage[english]{babel}
\usepackage[document]{ragged2e}
\usepackage{float}
\usepackage{bm}
\usepackage{amsfonts}
\usepackage{cancel}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{fp}
\usepackage{epstopdf}
\usepackage{varwidth}
\usepackage{blindtext}
\usepackage[
	a4paper,
	left=2.5cm,
	right=2.5cm,
	bottom=3cm,
	top=4cm
]{geometry}

\usepackage{framed}

\RequirePackage{amsmath}
\RequirePackage[absolute]{textpos}
\RequirePackage{fancyhdr}
\RequirePackage{xkeyval}
\RequirePackage{alphalph}
\RequirePackage{ifthen}
\RequirePackage{appendix}
\RequirePackage{titletoc}
\RequirePackage{etoolbox}



\usepackage{underscore}
\usepackage{lipsum}

%\RequirePackage{assoccnt}
%\RequirePackage{totcount}
%\newtotcounter{totalchapters}
%\regtotcounter{chapter}
%\DeclareAssociatedCounters{chapter}{totalchapters}



\usepackage{emptypage}
\usepackage{afterpage}

\newcommand\blankpage{%
	\null
	\thispagestyle{empty}%
	\addtocounter{page}{0}% change to -1 if you don't want page numbers additive
	\newpage
}



% -------------------------------------------------------------------------------
% Hyperlink configuration
% -------------------------------------------------------------------------------

\usepackage[verbose]{hyperref}

\hypersetup{hidelinks}
\addto\extrasenglish{
	\def\sectionautorefname{Section}
	\def\chapterautorefname{Chapter}
}
\setlength{\XeTeXLinkMargin}{-1pt}

\newcommand{\refer}[1]{
	\hspace{-.15em}\textcolor{ONSblue}{\bfseries Figure\ref{#1}}\hspace{-.4em}
}



% -------------------------------------------------------------------------------
% Graphics and helper functions
% -------------------------------------------------------------------------------

\usepackage[]{tcolorbox}
\RequirePackage{tikz}
\usepackage{tkz-euclide}
\usepackage{pgfplots}

\usepgfplotslibrary{fillbetween}
\usetikzlibrary{intersections}
\pgfplotsset{compat=1.12}



% -------------------------------------------------------------------------------
% Tables and helper functions
% -------------------------------------------------------------------------------

\usepackage{collcell}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{multicol}
\usepackage{colortbl}
\usepackage{hhline}
\usepackage{dcolumn}
\usepackage{tabularx}
\usepackage{ctable}
\usepackage{xltabular}

\newcommand{\dashrule}[1][black]{%
	\color{#1}\rule[\dimexpr.5ex-.2pt]{4pt}{.4pt}\xleaders\hbox{\rule{4pt}{0pt}\rule[\dimexpr.5ex-.2pt]{4pt}{.4pt}}\hfill\kern0pt%
}
\newcommand{\rulecolor}[1]{%
	\def\CT@arc@{\color{#1}}%
}

\usepackage{silence}
\WarningFilter{ctable}{Transparency disabled:}



% -------------------------------------------------------------------------------
% Colour schema
% -------------------------------------------------------------------------------

\definecolor{ONSgreen}{RGB}{168, 189, 58} % #a8bd3a
\definecolor{ONSblue}{RGB}{0, 61, 89} % #003d59
\definecolor{ONSpink}{RGB}{206, 53, 135} % #ce3587
\definecolor{ONSorange}{RGB}{216, 66, 39} % #d84227
\definecolor{ONSyellow}{RGB}{226, 188, 34} % #e2bc22

\definecolor{XLSpeach}{RGB}{252, 228, 214} % #fce4d6

\definecolor{LightGrey}{RGB}{245, 245, 245}
\definecolor{MidGrey}{RGB}{230, 230, 230}
\definecolor{DarkGrey}{RGB}{100, 100, 100}
\definecolor{LightBlue}{RGB}{206, 225, 255} 
\definecolor{LightGreen}{RGB}{210, 255, 206}
\definecolor{ExeterBlue}{RGB}{37, 85, 158} 
\definecolor{ExeterGreen}{RGB}{0, 155, 15}
\definecolor{ExeterPurple}{RGB}{167, 66, 244} 
\definecolor{LightPurple}{RGB}{240, 221, 255}
\definecolor{ExeterOrange}{RGB}{255, 165, 30}
\definecolor{LightOrange}{RGB}{255, 235, 206}
\definecolor{ExeterRed}{RGB}{191, 30, 30}



% -------------------------------------------------------------------------------
% Envrionments
% -------------------------------------------------------------------------------

\newenvironment{doctor-table}[5]{
	% ---------------------------------------------------------------------------
	% Flexible tabular environment based on pd.DataFrame input. Source code is 
	% beautifully typeset, alternating rows are highlighted and page breaks are 
	% handled automatically
	% 
	% Parameters
	% ----------
	% 
	% #1: Column count
	% #2: Column format
	% #3: Column headers
	% #4: Caption
	% #5: Label
	% 
	% Demo
	% ----
	% 
	% \begin{doctor-table}{4}
	%   {% Column format
	%     >{{\raggedleft\arraybackslash\hsize=\hsize}}X
	%   >{{\raggedleft\arraybackslash\hsize=\hsize}}X
	%     >{{\raggedleft\arraybackslash\hsize=\hsize}}X
	%     >{{\raggedleft\arraybackslash\hsize=\hsize}}X
	%   }{% Column headers
	%     \bfseries Numbers &
	%     \bfseries More numbers &
	%     \bfseries Text &
	%     \bfseries Mash \\
	%   }{% Caption
	%     Example table generated by Python
	%   }{% Label
	%     test
	%   }
	%   25 & 43 &       Lorem & iswdufvbouwesdbnvg \\
	%   82 & 71 &       ipsum &                abc \\
	%   23 & 52 &       dolor &            sdvcsdv \\
	%   82 & 85 &         sit &       sdvdssdvdvvn \\
	%   93 & 63 &        amet &          yumyumyum \\
	%   83 & 35 & consectetur &               wqoe \\
	%   87 & 51 &  adipiscing &            qphjpgh \\
	%   79 & 41 &        elit & owperjgpowegjwjggg \\
	%   84 & 88 &   Curabitur &        wepogjwpeog \\
	%   60 &  7 &         nec &                 oi \\
	% \end{doctor-table}
	% ---------------------------------------------------------------------------
	\small
	\rowcolors{3}{gray!5}{}
	\renewcommand{\arraystretch}{1.25}
	\xltabular{\linewidth}{#2}
	\rowcolor{white}\caption{#4}\label{table:#5} \\%
	\toprule%
	\rowcolor{white}#3%
	\specialrule{.05em}{.05em}{.05em}%
	\endfirsthead%
	
	\rowcolor{white}\caption[]{#4 (cont.)} \\%
	\rowcolor{white}\multicolumn{#1}{c}{
		\raisebox{.15em}{\resizebox{0.95\textwidth}{!}{
			\makebox[\textwidth]{\dashrule[black]}
		}}
	} \\%
	\rowcolor{white}#3%
	\specialrule{.05em}{.05em}{.05em}
	\endhead%
	
	\rowcolor{white}\multicolumn{#1}{r}{%
		\multirow{2}{*}{%
			\parbox{0.95\textwidth}{%
				\raisebox{.15em}{\resizebox{0.95\textwidth}{!}{
					\makebox[\textwidth]{\dashrule[black]}
				}}
				\raggedleft\footnotesize\textit{Continued on next page}
			}
		}
	}
	\endfoot%
	
	\bottomrule%
	\endlastfoot%
}{
	\endxltabular
}



% -------------------------------------------------------------------------------
% Environment macros
% -------------------------------------------------------------------------------

\makeatletter
\pgfdeclarepatternformonly[\hatchdistance,\hatchthickness]{flexible hatch}
{\pgfqpoint{0pt}{0pt}}
{\pgfqpoint{\hatchdistance}{\hatchdistance}}
{\pgfpoint{\hatchdistance-1pt}{\hatchdistance-1pt}}%
{
	\pgfsetcolor{\tikz@pattern@color}
	\pgfsetlinewidth{\hatchthickness}
	\pgfpathmoveto{\pgfqpoint{0pt}{0pt}}
	\pgfpathlineto{\pgfqpoint{\hatchdistance}{\hatchdistance}}
	\pgfusepath{stroke}
}



%% End of file `doctor.cls'.