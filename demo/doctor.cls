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

\RequirePackage[]{helvet}
\fontfamily{phv}\selectfont
\renewcommand{\familydefault}{\sfdefault}



% -------------------------------------------------------------------------------
% 3rd party packages
% -------------------------------------------------------------------------------

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{textcomp}
\RequirePackage{gensymb}
\RequirePackage[english]{babel}
\RequirePackage[document]{ragged2e}
\RequirePackage{float}
\RequirePackage{bm}
\RequirePackage{amsfonts}
\RequirePackage{cancel}
\RequirePackage{varwidth}
\RequirePackage{blindtext}
\RequirePackage{underscore}
\RequirePackage{lipsum}

\RequirePackage[
	a4paper,
	left=2.5cm,
	right=2.5cm,
	bottom=3cm,
	top=4cm
]{geometry}

\RequirePackage{graphicx}
\RequirePackage{caption}
\RequirePackage{fp}
\RequirePackage{epstopdf}
\RequirePackage{framed}
\RequirePackage{amsmath}
\RequirePackage[absolute]{textpos}
\RequirePackage{fancyhdr}
\RequirePackage{xkeyval}
\RequirePackage{alphalph}
\RequirePackage{ifthen}
\RequirePackage{appendix}
\RequirePackage{titletoc}
\RequirePackage{etoolbox}

%\RequirePackage{assoccnt}
%\RequirePackage{totcount}
%\newtotcounter{totalchapters}
%\regtotcounter{chapter}
%\DeclareAssociatedCounters{chapter}{totalchapters}



\RequirePackage{emptypage}
\RequirePackage{afterpage}

\newcommand\blankpage{%
	\null
	\thispagestyle{empty}%
	\addtocounter{page}{0}% change to -1 if you don't want page numbers additive
	\newpage
}



% -------------------------------------------------------------------------------
% Hyperlink configuration
% -------------------------------------------------------------------------------

\RequirePackage[verbose]{hyperref}

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

\RequirePackage[]{tcolorbox}
\RequirePackage{tikz}
\RequirePackage{tkz-euclide}
\RequirePackage{pgfplots}

\usepgfplotslibrary{fillbetween}
\usetikzlibrary{intersections}
\pgfplotsset{compat=1.12}



% -------------------------------------------------------------------------------
% Tables and helper functions
% -------------------------------------------------------------------------------

\RequirePackage{collcell}
\RequirePackage{booktabs}
\RequirePackage{longtable}
\RequirePackage{multirow}
\RequirePackage{multicol}
\RequirePackage{colortbl}
\RequirePackage{hhline}
\RequirePackage{dcolumn}
\RequirePackage{tabularx}
\RequirePackage{ctable}

\newcommand{\dashrule}[1][black]{%
	\color{#1}\rule[\dimexpr.5ex-.2pt]{4pt}{.4pt}\xleaders\hbox{\rule{4pt}{0pt}\rule[\dimexpr.5ex-.2pt]{4pt}{.4pt}}\hfill\kern0pt%
}
\newcommand{\rulecolor}[1]{%
	\def\CT@arc@{\color{#1}}%
}

\RequirePackage{silence}
\WarningFilter{ctable}{Transparency disabled:}



% -------------------------------------------------------------------------------
% Page styling
% -------------------------------------------------------------------------------

\fancypagestyle{plain}{\fancyhf{}}
% \renewcommand\chaptermark[1]{\markboth{\textcolor{white}{#1}}{}}

\fancypagestyle{doctor}{%
	\fancyfoot{\draw@footer}%
	\fancyhead{\draw@header}%
}%



\newlength{\miniframemodule}
\setlength{\miniframemodule}{0.02\paperwidth}%

\newcommand{\draw@footer}{%
	\pagestyle{fancy}
%
	\ifodd\value{page}%
		\begin{tikzpicture}[overlay, remember picture]
			\draw[thick] ([xshift = \marginparwidth, yshift = 0.066\paperheight]current page.south west) -- ([xshift = -\marginparwidth, yshift = 0.066\paperheight]current page.south east);
		%
			\node[anchor = north east, xshift = 3mm-\marginparwidth, yshift = 0.066\paperheight]  at (current page.south east){
				\scalebox{0.66}{
					\rotatebox{180}{
						\hourglassAnimation{\thepage}
					}
				}
			};
		\end{tikzpicture}
	\else
		\begin{tikzpicture}[overlay, remember picture]
			\draw[thick] ([xshift = \marginparwidth, yshift = 0.066\paperheight]current page.south west) -- ([xshift = -\marginparwidth, yshift = 0.066\paperheight]current page.south east);
		%
			\node[anchor = north west, xshift = 2mm+\marginparwidth, yshift = 0.066\paperheight-0.66mm]  at (current page.south west){
				\includegraphics[height = 0.04\textwidth]{figures/logos/ons-english.pdf}
			};
		\end{tikzpicture}
	\fi
%
	\ifFinalVersion
		\begin{tikzpicture}[overlay, remember picture]
			\node[anchor = south] at ([yshift = 0.033\paperheight]current page.south) {
				\begin{tikzpicture}%
					%
					% Select the color corresponding to the current chapter
					\ch@ngecolors{\thetotalchapters}
					%   
					\clip(-0.01\paperwidth, -0.01\paperwidth) rectangle (\totvalue{totalchapters}\miniframemodule + 0.01\paperwidth, 0.11\paperwidth);
					%    
					\foreach[evaluate=\y using \x-1,evaluate=\z using \x-.5] \x in {1,...,\totvalue{totalchapters}} {
						\ch@ngecolors{\x}
						%         
						% Draw the rectangles in the footer
						\ifthenelse{
							% Condition: if \x is current chapter
							\equal{\thetotalchapters}{\x}
						}{%
							%%% IF CURRENT CHAPTER
							%							\draw[fill=\ch@p, rounded corners=1pt] (\y\miniframemodule, 0) rectangle (\x\miniframemodule, 0.015\paperwidth);
							\draw[fill=\ch@p, draw = none, line width = 0.05mm] (\z\miniframemodule, 0.005\paperwidth) circle (0.005\paperwidth);
							%
							\node at (\z\miniframemodule, -0.25\miniframemodule) {\hyperlink{chapter \x}{\XeTeXLinkBox{\phantom{\rule{\miniframemodule}{0.5\miniframemodule}}}}};
							
						}{%
							%%% OTHER CHAPTERS
							%							\draw[fill=black!10, rounded corners=1pt] (\y\miniframemodule, 0) rectangle (\x\miniframemodule, 0.015\paperwidth);
							\draw[fill=black!5, draw = none, line width = 0.05mm] (\z\miniframemodule, 0.005\paperwidth) circle (0.005\paperwidth);
							%
							\node at (\z\miniframemodule, -0.25\miniframemodule) {\hyperlink{chapter \x}{\XeTeXLinkBox{\phantom{\rule{\miniframemodule}{0.5\miniframemodule}}}}};
						}
					}
					%
				\end{tikzpicture}
			};
		\end{tikzpicture}
	\else
		\begin{tikzpicture}[overlay, remember picture]
			\node[anchor = south] (DRAFTVERSION) at ([yshift = 0.033\paperheight]current page.south) {\bfseries\color{red}DRAFT VERSION};
		\end{tikzpicture}
	\fi
}



% -------------------------------------------------------------------------------
% XLTabular: Herbert Voss, Rolf Niepraschk
% -------------------------------------------------------------------------------

\let\XLT@i@tabularx=\tabularx
\let\XLT@i@endtabularx=\endtabularx
\let\XLT@i@TX@endtabularx=\TX@endtabularx
%
\RequirePackage{ltablex}
\keepXColumns% xltabular behaves like tabularx
%
\let\XLT@ii@tabularx=\tabularx
\let\XLT@ii@TX@endtabularx=\TX@endtabularx
\let\XLT@longtable=\longtable
\let\XLT@LT@start=\LT@start
\let\XLT@LT@array=\LT@array
\@ifundefined{scr@LT@array}{%
	\AtBeginDocument{%
		\@ifundefined{adl@LT@array}{}{\let\XLT@adl@LT@array=\adl@LT@array}
	}
}{\let\XLT@scr@LT@array=\scr@LT@array}%

%
% restore original tabularx
\renewenvironment{tabularx}%
{\let\TX@endtabularx=\XLT@i@TX@endtabularx\XLT@i@tabularx}
{\XLT@i@endtabularx}
%
% define a new tabularx like the one from "ltablex" 
%
\newenvironment{xltabular}[1][x]%
{%
	\par
	\if l#1%
	\LTleft\z@ \LTright\fill
	\else\if r#1%
	\LTleft\fill \LTright\z@
	\else\if c#1%
	\LTleft\fill \LTright\fill
	\fi\fi\fi
	\let\TX@endtabularx=\XLT@ii@TX@endtabularx
	\let\endtabularx\endxltabular
	\XLT@ii@tabularx}
{\def\@currenvir{tabularx}}

\def\LT@caption{%
	\noalign\bgroup
	\@ifnextchar[{\XLT@LT@caption}{\XLT@@LT@caption}
}
\def\XLT@LT@caption[#1]{%
	% increasing the counter only if opt. parameter is not empty
	\ifx\relax#1\relax\@tempswafalse\else\@tempswatrue\fi
	\XLT@@@LT@caption[#1]
}
\def\XLT@@LT@caption{% allways increasing the counter
	\@tempswatrue
	\XLT@@@LT@caption
}
\def\XLT@@@LT@caption{%
	% Eventually increasing the counter
	\if@tempswa\refstepcounter{\LTcaptype}\fi
	% global assignments because we are inside a group
	\global\let\@currentlabel=\@currentlabel
	\@ifundefined{cref@currentlabel}{}{% from package "cleveref"
		\global\let\cref@currentlabel=\cref@currentlabel
	}
	\ifXLT@HypRef
	% revert to the patched version
	\global\let\LT@start=\XLT@Hy@LT@start
	\hyper@makecurrent{\LTcaptype}%
	\global\let\Hy@LT@currentHref\@currentHref
	\fi
	% continue with the original definition of \LT@caption 
	\@ifnextchar[{\egroup\LT@c@ption\@firstofone}\LT@capti@n
}

%
\providecommand*\LTcaptype{table}% support of package "caption"
\def\longtable{%
	\ifXLT@HypRef
	% revert to the unpatched version if \caption is not used
	\global\let\LT@start=\XLT@LT@start
	\fi
	\XLT@longtable
}

\newif\ifXLT@HypRef
\AtBeginDocument{%
	\let\XLT@refstepcounter=\refstepcounter
	\@ifpackageloaded{hyperref}{\XLT@HypReftrue}{\XLT@HypReffalse}%
	\ifXLT@HypRef
	% save the patched version
	\let\XLT@Hy@LT@start=\LT@start
	% revert to the unpatched versions
	\@ifundefined{scr@LT@array}{%
		\@ifundefined{adl@LT@array}{%
			% hyperref has \LT@array patched directly
			\let\LT@array=\XLT@LT@array
		}{%
			% hyperref has \adl@LT@array patched, not \LT@array
			\let\adl@LT@array=\XLT@adl@LT@array
		}%
	}{%
		% hyperref has \scr@LT@array patched, not \LT@array
		\let\scr@LT@array=\XLT@scr@LT@array
	}%
	\fi
	\def\LT@array{%
		% make the call of \refstepcounter inside of \XLT@LT@array ineffective
		\renewcommand*\refstepcounter[2][]{%
			% make next calls effective again
			\let\refstepcounter=\XLT@refstepcounter
		}%
		\XLT@LT@array
	}%
}



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