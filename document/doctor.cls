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
\RequirePackage{xifthen}
\RequirePackage{appendix}
\RequirePackage{titletoc}
\RequirePackage{etoolbox}



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
	\hspace{-.15em}\textcolor{maindocumentcolour}{\bfseries Figure\ref{#1}}\hspace{-.4em}
}



% -------------------------------------------------------------------------------
% Graphics and helper functions
% -------------------------------------------------------------------------------

\RequirePackage[most]{tcolorbox}
\RequirePackage{tikz}
\RequirePackage{tkz-euclide}
\RequirePackage{pgfplots}

\usepgfplotslibrary{fillbetween}
\usetikzlibrary{
	intersections,
	backgrounds,
	positioning,
	calc,
	patterns,
	shapes,
}
\pgfplotsset{compat=1.12}

\pgfdeclarelayer{background}
\pgfdeclarelayer{middle}
\pgfsetlayers{background,middle,main}



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
% Title page
% -------------------------------------------------------------------------------

\gdef\@credentialtext{}
\gdef\credential#1{%
	\g@addto@macro\@credentialtext{%
		#1 \par%
	}
}

\gdef\@subtitle{}
\def\subtitle#1{\gdef\@subtitle{#1}}

\newcommand{\frontpage}{
	\pagestyle{empty}
	
	\begin{tikzpicture}[overlay, remember picture]%
		\begin{scope}%
			\clip [] ($(current page.north west)+(0.0165\paperwidth, 0.0165\paperwidth)-(0, 0.33\paperheight)$) rectangle coordinate (centerpoint) ($(current page.north east)+(-0.0165\paperwidth, -0.0165\paperwidth)$);%
			\ifx\companybanner\empty%
				\node[] at ($(current page.north)+(0\paperwidth, - 0.165\paperheight)$) {\includegraphics[width = 1\paperwidth]{example-image-a}};%
			\else%
				\fill[maindocumentcolour] (current page.north west) rectangle ([yshift=-0.33\paperheight]current page.north east);
			%
				\node[anchor = south] at ($(current page.north)+(0\paperwidth, 3pt+0.033\paperwidth-0.33\paperheight)$) {\includegraphics[width = 1\paperwidth]{\companybanner}};%
			\fi%
		\end{scope}
		%
		\draw[
			fill = none,
			draw = white,
			line width = 0.033\paperwidth,
			rounded corners = 16pt
		]
		($(current page.north west)+(0.0165\paperwidth, 0.0165\paperwidth)-(0, 0.33\paperheight)$)
		-- ($(current page.north west)+(0.0165\paperwidth, -0.0165\paperwidth)$)
		-- ($(current page.north east)+(-0.0165\paperwidth, -0.0165\paperwidth)$)
		-- ($(current page.north east)+(-0.0165\paperwidth, 0.0165\paperwidth)-(0, 0.33\paperheight)$)
		-- cycle;
		%%%
		\node[anchor = north, yshift = -1cm] (maketitle) at (current page.center) {%
			\parbox{0.4\paperwidth}{
				\def\baselinestretch{1.2}%
				\centering\bfseries%
				\Huge\@author \par%
				\vskip\baselineskip%
				\large\@credentialtext \par%
				\huge\vskip\baselineskip%
				\@title \par%
				\large\@subtitle \par%
				\vskip10\baselineskip%
				\normalsize Last updated: \@date%
			}
		};
	\end{tikzpicture}
	
	\null\newpage\pagestyle{doctor}
}



% -------------------------------------------------------------------------------
% Page animation
% -------------------------------------------------------------------------------

\RequirePackage{intcalc}
\RequirePackage{fp}
\usepackage[lastpage]{zref}

\newcommand{\totalpages}{\zref@extractdefault{LastPage}{page}{0}}

\newcommand\hourglassAnimation[1]{
	\tikz\node (pic) at (0,-1in) {
		\rotatebox{180}{
			\resizebox{26pt}{28pt}{
				\pgfmathparse{1 - (#1 / (\totalpages+.1))}
				\edef\perc{\pgfmathresult}
				\hourglass{1}{1.5}{\perc}{}
			}
		}
	};
}

\newcommand\hourglass[4]{
	\begin{tikzpicture}
		\tikzset{
			corners/.style={
				rounded corners = 6pt
			},
			line/.style={
				draw = black,
				corners
			},
		}
	%
		\coordinate (center) at (#1/2, #2/2);
	%	
		\begin{scope}
			\clip[corners] (center) -- (#1, #2) -- (0, #2) -- (center);
			\fill[maindocumentcolour] (0, #2/2 * #3) rectangle ++(#1, #2/2);
		\end{scope}
	%
		\draw[densely dotted, thick, maindocumentcolour!50, #4] (center) -- ++(0,-#2/2);
	%
		\begin{scope}
			\clip[corners] (center) -- (0,0) -- (#1,0) -- (center);
			\fill[maindocumentcolour] (0, 0) rectangle ++(#1,{#2/2*(1-#3)});
		\end{scope}
	%
		\draw[line] (center) -- (0,0) -- (#1,0) -- (center);
		\draw[line] (center) -- (#1,#2) -- (0,#2) -- (center);
	\end{tikzpicture}
}



% -------------------------------------------------------------------------------
% Page styling
% -------------------------------------------------------------------------------

\RequirePackage{assoccnt}
\RequirePackage{totcount}
\newtotcounter{totalchapters}
\regtotcounter{chapter}
\DeclareAssociatedCounters{chapter}{totalchapters} % Associate the driven counter `totalchapters` to the master counter `chapter`

\renewcommand{\headrulewidth}{0pt}
\setlength{\headheight}{15pt}
\setlength{\footskip}{50pt}

\fancypagestyle{plain}{\fancyhf{}}
% \renewcommand\chaptermark[1]{\markboth{\textcolor{white}{#1}}{}}

\fancypagestyle{doctor}{%
	\fancyfoot{\draw@footer}%
	\fancyhead{\draw@header}%
}%

\def\@makechapterhead#1{%
	\hypertarget{chapter \thetotalchapters}{}%
	\parindent 0pt%
	\draw@chapterheader{#1}%
	\draw@footer%
}%



\newcommand{\doctorsection}{}
\renewcommand{\section}[1]{
	\addtocounter{section}{1}
	\addcontentsline{toc}{section}{\thesection \; #1}
	\vskip 1cm
	\flushleft{
		\Large\bfseries\thesection\;#1
		\vskip -3mm
		\textcolor{black!50}{\hrule}
		\vskip 3mm
	}
	\vskip 3mm
	\renewcommand{\doctorsection}{#1}
	\setcounter{doctorsubsection}{0}
	\justify
}



\newcounter{doctorsubsection}[subsection]
\setcounter{doctorsubsection}{1}

\renewcommand{\subsection}[1]{
	\stepcounter{doctorsubsection}
	\addcontentsline{toc}{subsection}{\color{black!50} \thesection.\thedoctorsubsection \; #1}
	\vspace{3mm}
	\flushleft{
		\begin{tikzpicture}[overlay]
			\node[anchor = east, rectangle, rounded corners = 1pt, inner sep = 3.5pt, fill = maindocumentcolour] at (-0.45, 0.45) {\normalfont\sffamily\large\bfseries\color{white} \thesection.\thedoctorsubsection};
		%
			\draw[color = maindocumentcolour, anchor=west] (-0.15, 0.45) node {\large\bfseries#1};
		\end{tikzpicture}
	}
	\justify
	\vspace{0mm}
}



\newcommand{\ellschaptertitle}{}
\newcommand{\draw@chapterheader}[1]{% Regular chapters header
	\renewcommand{\ellschaptertitle}{#1}
	\begin{tikzpicture}[overlay, remember picture]
		\node[anchor = north west] at (current page.north west) {
			\begin{tikzpicture}[overlay, remember picture]
				\fill[ons-grey-900] (current page.north west) rectangle ([yshift = -0.1\paperheight]current page.north east);
			%
				\draw[color = black, thick] ([yshift = -0.1\paperheight]current page.north west) -- ([yshift = -0.1\paperheight]current page.north east);
			\end{tikzpicture}
		};
	%
		\node[
			rectangle,
			rounded corners = 4pt,
			inner sep = 11pt,
			draw = black,
			fill = maindocumentcolour,
			line width = 0.25mm,
			yshift = -0.1\paperheight
		] at (current page.north){
			\Large\color{white}\bfseries\MakeUppercase{#1}
		};
	\end{tikzpicture}
	\vskip 0cm
}

\newcommand{\draw@chaptersheader}[1]{% Table of Contents header etc
	\begin{textblock}{1}(0,0)
		\begin{tikzpicture}[x=1.0cm,y=1.0cm]%
			\clip(0,0) rectangle (\paperwidth,.105\paperwidth);
			\fill[maindocumentcolour] (0,.0333\paperwidth) rectangle (\paperwidth,.105\paperwidth);
			\node[red,right] at (.05\paperwidth,.07\paperwidth) {\Large\color{white}\bfseries\MakeUppercase{#1}};
		\end{tikzpicture}
	\end{textblock}
}

\newcommand{\draw@chaptersfooter}{%
	\pagestyle{empty}
}

\def\@makeschapterhead#1{%
	\parindent 0pt%
	\draw@chaptersheader{#1}%
	\draw@chaptersfooter%
}%



\newcommand{\draw@header}[1]{% Regular page headers
	\ifodd\value{page}%
		\begin{tikzpicture}[overlay, remember picture]
			\draw[thick] ([yshift = -0.1\paperheight]current page.north west) -- ([xshift = -\marginparwidth, yshift = -0.1\paperheight]current page.north east);
		%
			\node[anchor = base west, xshift = -4mm, yshift = 2mm-0.1\paperheight] at (current page.north west){
				\Large\phantom{Gg}\color{black!50}\doctorsection
			};
		%
			\node[anchor = south east, xshift = 4mm-\marginparwidth, yshift = -0.1\paperheight]  at (current page.north east){
				\raggedleft
				\Large\color{black!80}\thepage\phantom{Gg}
			};
		\end{tikzpicture}
	\else
		\begin{tikzpicture}[overlay, remember picture]
			\draw[thick] ([xshift = \marginparwidth, yshift = -0.1\paperheight]current page.north west) -- ([yshift = -0.1\paperheight]current page.north east);
		%
			\node[anchor = base east, xshift = 4mm, yshift = 2mm-0.1\paperheight] at (current page.north east){
				\Large\color{black!80}\ellschaptertitle\phantom{Gg}
			};
		%
			\node[anchor = south west, xshift = \marginparwidth-4mm, yshift = -0.1\paperheight]  at (current page.north west){
				\raggedleft
				\Large\phantom{Gg}\color{black!80}\thepage
			};
		\end{tikzpicture}
	\fi
}



\newlength{\miniframemodule}
\setlength{\miniframemodule}{0.02\paperwidth}%

\newcommand{\draw@footer}{%
	\pagestyle{fancy}
%
	\ifodd\value{page}%
		\begin{tikzpicture}[overlay, remember picture]
			\draw[thick] ([xshift = \marginparwidth, yshift = 0.066\paperheight]current page.south west) -- ([xshift = -\marginparwidth, yshift = 0.066\paperheight]current page.south east);
		%
			\ifhourglass%
				\node[anchor = north east, xshift = 1.5mm-\marginparwidth, yshift = 0.066\paperheight]  at (current page.south east){%
					\scalebox{0.66}{%
						\rotatebox{180}{%
							\hourglassAnimation{\thepage}%
						}%
					}%
				};%
			\else%
				\node[anchor = north east, xshift = -1mm-\marginparwidth, yshift = 0.066\paperheight-0.66mm]  at (current page.south east){%
					\includegraphics[height = 0.04\textwidth]{example-image-b}
				};%
			\fi%
		\end{tikzpicture}
	\else
		\begin{tikzpicture}[overlay, remember picture]
			\draw[thick] ([xshift = \marginparwidth, yshift = 0.066\paperheight]current page.south west) -- ([xshift = -\marginparwidth, yshift = 0.066\paperheight]current page.south east);
		%
			\ifx\companylogo\empty%
				\node[anchor = north west, xshift = 2mm+\marginparwidth, yshift = 0.066\paperheight-0.66mm]  at (current page.south west){%
					\includegraphics[height = 0.04\textwidth]{example-image-a}
				};
			\else%
				\node[anchor = north west, xshift = 2mm+\marginparwidth, yshift = 0.066\paperheight-0.66mm]  at (current page.south west){%
					\includegraphics[height = 0.04\textwidth]{\companylogo}
				};
			\fi%
		\end{tikzpicture}
	\fi
%
	\begin{tikzpicture}[overlay, remember picture]
		\node[anchor = south] at ([yshift = 0.033\paperheight]current page.south) {
			\begin{tikzpicture}%
				\clip(-0.01\paperwidth, -0.01\paperwidth) rectangle (\totvalue{totalchapters}\miniframemodule + 0.01\paperwidth, 0.11\paperwidth);
			%
				\foreach[evaluate=\y using \x-1,evaluate=\z using \x-.5] \x in {1,...,\totvalue{totalchapters}} {
					% Draw the rectangles in the footer
					\ifthenelse{
						% Condition: if \x is current chapter
						\equal{\thetotalchapters}{\x}
					}{%
						%%% IF CURRENT CHAPTER
						\draw[fill=maindocumentcolour, draw = none, line width = 0.05mm] (\z\miniframemodule, 0.005\paperwidth) circle (0.005\paperwidth);
					%
						\node at (\z\miniframemodule, -0.25\miniframemodule) {\hyperlink{chapter \x}{\XeTeXLinkBox{\phantom{\rule{\miniframemodule}{0.5\miniframemodule}}}}};
						
					}{%
						%%% OTHER CHAPTERS
						\draw[fill=black!5, draw = none, line width = 0.05mm] (\z\miniframemodule, 0.005\paperwidth) circle (0.005\paperwidth);
					%
						\node at (\z\miniframemodule, -0.25\miniframemodule) {\hyperlink{chapter \x}{\XeTeXLinkBox{\phantom{\rule{\miniframemodule}{0.5\miniframemodule}}}}};
					}
				}
			\end{tikzpicture}
		};
	\end{tikzpicture}
	%
	%
	%
		\begin{tikzpicture}[overlay, remember picture]
%			\node[anchor = south] (DRAFTVERSION) at ([yshift = 0.033\paperheight]current page.south) {\bfseries\color{red}DRAFT VERSION};
	%
%		\draw[red, thick] ([xshift=-3mm-\marginparwidth]current page.south east) -- ([xshift=-3mm-\marginparwidth]current page.north east);
%	%
%		\draw[red, thick] ([xshift=3mm+\marginparwidth]current page.south west) -- ([xshift=3mm+\marginparwidth]current page.north west);
		\end{tikzpicture}
}



\pagestyle{doctor}



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

\definecolor{ons-green}{RGB}{168, 189, 58} % #a8bd3a
\definecolor{ons-blue}{RGB}{0, 61, 89} % #003d59
\definecolor{ons-pink}{RGB}{206, 53, 135} % #ce3587
\definecolor{ons-orange}{RGB}{216, 66, 39} % #d84227
\definecolor{ons-yellow}{RGB}{226, 188, 34} % #e2bc22

\definecolor{ons-grey-900}{RGB}{245, 245, 245}
\definecolor{ons-grey-700}{RGB}{230, 230, 230}
\definecolor{ons-gray-100}{RGB}{100, 100, 100}
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



\tikzset{
	dlbuttonfill/.cd,
	data/.style={draw=maindocumentcolour,fill=maindocumentcolour,text=white},
	image/.style={draw=maindocumentcolour,fill=none,text=maindocumentcolour},
	error/.style={draw=red,fill=none,text=red},
	paint/.code={%
		\ifthenelse{\isin{#1}{image}}{\tikzset{dlbuttonfill/image}}{
			\ifthenelse{\isin{#1}{data}}{\tikzset{dlbuttonfill/data}}{
				\tikzset{dlbuttonfill/error}
			}
		}
	},
}

\newcommand{\button}[2][data]{%
	\noindent\href{#2}{%
		\begin{tikzpicture}%
			\node[%
			dlbuttonfill/paint=#1,
			rectangle,
			inner sep = 6pt,
			rounded corners = 2pt,
			] {%
				\small\bfseries\MakeUppercase{#1}%
			};%
		\end{tikzpicture}%
	}%
}



% -------------------------------------------------------------------------------
% Environments
% -------------------------------------------------------------------------------

\RequirePackage{enumitem}
\RequirePackage{environ}

\newenvironment{downloads}{%
	\noindent Download the data:\newline%
	\vskip-.5\baselineskip%
}{
	\newline%
}



\newtcolorbox{main-points-wrapper}{
	enhanced,
	breakable,
	rounded corners,
	arc = 4pt,
	boxrule = 0pt,
	colback = ons-grey-900,
	boxsep=12pt,
}

\newenvironment{main-points}{%
	% ---------------------------------------------------------------------------
	% Boxed section to summarise the main document's points as an enumerated
	% list. Expand the list through the \item macro.
	% 
	% Parameters
	% ----------
	% None.
	% 
	% Demo
	% ----
	% \begin{main-points}
	%     \item Point 1
	%     \item Point 2
	%     \item ...
	%     \item Point n
	% \end{main-points}
	% ---------------------------------------------------------------------------
	\begin{main-points-wrapper}%
		{%
			\vskip.25\baselineskip\Large\bfseries Main points%
			\vskip.5\baselineskip\color{black!50}\hrule%
		}
		\justify%
		\begin{enumerate}[%
			label=\bfseries\color{maindocumentcolour}\theenumi.\:,
			wide,
			labelwidth=!,
			labelindent=0pt,
		]%
}{%
		\end{enumerate}%
	\end{main-points-wrapper}%
}



\newenvironment{doctor-table}[5]{
	% ---------------------------------------------------------------------------
	% Flexible tabular environment based on pd.DataFrame input. Source code is 
	% beautifully typeset, alternating rows are highlighted and page breaks are 
	% handled automatically
	% 
	% Parameters
	% ----------
	% #1: Column count
	% #2: Column format
	% #3: Column headers
	% #4: Caption
	% #5: Label
	% 
	% Demo
	% ----
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



\newenvironment{doctor-plot}[1]{
	% ---------------------------------------------------------------------------
	% Flexible plotting environment based on pd.DataFrame input. Line plots, 
	% difference quiver plots and regions hatch-shading are supported. Set the  
	% axis labels and title and allow Doctor to automatically populate the rest.
	% 
	% Parameters
	% ----------
	% #1: 
	% 
	% Demo
	% ----
	% \begin{doctor-plot}
	% \end{doctor-plot}
	% ---------------------------------------------------------------------------
	#1
	\noindent\begin{tikzpicture}[
		hatch distance/.store in=\hatchdistance,
		hatch distance=10pt,
		hatch thickness/.store in=\hatchthickness,
		hatch thickness=2pt
	]
	%
		\begin{axis}[%
		% Abstract
			set layers,
			axis x line=bottom,
			axis y line=middle,
			axis line style={-stealth, shorten >=-2mm},
			hide obscured x ticks=false,
			x label style={at={(axis description cs:.5,-.1)},anchor=north},
			y label style={at={(axis description cs:-.075,.5)},rotate=90,anchor=south},
			axis on top,
			width=.975\textwidth,
			height=\axisdefaultheight,
			legend style={at={(1,1)},anchor=north east,font=\small,line width=1pt,mark size=.6pt,rounded corners=1pt},
		% Fitting data to boundaries
			clip mode=individual,
			enlarge y limits={abs=0.4pt},
		% Variables
			xlabel={Time (weeks)},
			ylabel={Independent variable},
			xmin=0,
		]
}{
		\end{axis}
	\end{tikzpicture}
}



% -------------------------------------------------------------------------------
% Table of Contents
% -------------------------------------------------------------------------------

\renewcommand\chaptermark[1]{\markboth{\textcolor{white}{#1}}{}}

% Avoid badbox for >100 page documents
\renewcommand{\@pnumwidth}{3em}%
\contentsmargin{-0mm}%

\dottedcontents{section}[2.3em]{}{2.3em}{5pt}
\dottedcontents{subsection}[5.5em]{}{3.2em}{5pt}

% Start title contents formatting
%
% TOC Chapter
%
	\titlecontents{chapter}[3.3pc]
	{%
		\addvspace{30pt}%
%		\stepcounter{charpitre}
		\begin{tikzpicture}[remember picture, overlay]%
			\fill[
				rounded corners = 4pt,
				inner sep = 11pt,
				maindocumentcolour,
				text=white
			] (-4.5,-.2) rectangle (-.8,.6);%
		%
			\node at (-2.5,0.2) {%
				\hyperlink{chapter\thechapter}{%
					\XeTeXLinkBox{\phantom{\rule{3.4cm}{.6cm}}}
				}
			};
			\node[xshift=-2.5cm, yshift=0.2cm]{%
				\raggedright\bfseries\color{white}\large\sc%
				Chapter\ \thecontentslabel%
			};%
		\end{tikzpicture}%
		\large\bfseries\color{black}}%
	{}
	{}
	{%
		\;\titlerule\;\large\bfseries Page\ \thecontentspage%
		\begin{tikzpicture}[remember picture, overlay]
			\draw[black] (2pt,0) rectangle (6,0.1pt);
		\end{tikzpicture}%
	}%
	[\addvspace{.2cm}]%
%
% TOC Section
%
	\titlecontents{section}[3.3pc]
	{\addvspace{5pt}}
	{%
		\color{black}\contentslabel[\thecontentslabel]{2pc}\color{black}}
	{}
	{\mdseries\titlerule*[0.75em]{$\cdotp$}\bfseries
		\small\color{black}\thecontentspage\color{black}}
	[\addvspace{3pt}]
%
% TOC Subsection
%
	\titlecontents{subsection}[5.1pc]
	{\addvspace{5pt}}
	{%
		\color{black!50}\contentslabel[\thecontentslabel]{2pc}\color{black}}
	{}
	{\hfill\small\color{black!50}\thecontentspage\color{black}}
	[\addvspace{0pt}]
%
% TOC Figure
%
	\titlecontents{figure}
	[0em]
	{}
	{\fbox{\thecontentslabel}\hspace*{1.5em}}
	{}
	{\ \titlerule*[8pt]{$\cdot$}\contentspage}
%
% End title contents formatting

% Correct spacing between page header and TOC
\renewcommand{\tableofcontents}{%
	\chapter*{\contentsname}%
	\markboth{\contentsname}{}
%	\def\@leftmark{\contentsname}%
	\vspace{-30pt}%
	\@starttoc{toc}
}



% -------------------------------------------------------------------------------
% Optional class parameters
% -------------------------------------------------------------------------------

\RequirePackage{xkeyval}

\def\companylogo{}
\def\companybanner{}

\def\maincolour{}

\newif\ifhourglass

\DeclareOptionX{theme}{\colorlet{maindocumentcolour}{#1}}
\DeclareOptionX{logo}{\IfFileExists{#1}{\def\companylogo{#1}}{}}
\DeclareOptionX{banner}{\IfFileExists{#1}{\def\companybanner{#1}}{}}
\DeclareOptionX{hourglass}{\hourglasstrue}
\DeclareOptionX*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptionsX \relax



%% End of file `doctor.cls'.