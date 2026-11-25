# __The Fifteen AXF Matrices of the Boson Rotors in Detail: Every Matrix, Every Boson, Its Entries, Its Role__

## Introduction

**The question.** [Construction of the AXF Matrices of the Rotors of the Fifteen Generators](construction-of-the-axf-matrices-of-the-rotors-of-the-fifteen-generators.html) gives one closed form per array and proves that the fifteen are elementary. **This article takes the fifteen one at a time, in the boson order, and asks of each what its matrix does**: which lines the array moves, which lines its rotor leaves alone, and what that makes the boson.

**The answer in one line.** A rotor of this model carries three kinds of nonzero entry and no more — a cosine that stays, a sine that moves, and a phase that multiplies — and **a boson's role is decided by which of the three its rotor carries and by which lines it leaves at $1$.**

**Four articles, four questions, and this is the fourth.** [The construction article](construction-of-the-axf-matrices-of-the-fifteen-generators.html) answers *what is the array*. [The rotors construction](construction-of-the-axf-matrices-of-the-rotors-of-the-fifteen-generators.html) answers *what is the closed form*. [The rotors article](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) answers *which space does the rotor turn, and why is none of them a boost*. [The bosons-in-detail article](the-15-axf-matrices-of-the-bosons-in-detail.html) answers *what is the spectrum and what is the mass*. **This article answers *what does the matrix do to the four lines, and what is the boson for*** — one section per boson, with the array and its rotor printed side by side.

**Why the rotor and not only the array, said once.** The array's entry is a vertex: it says which two lines a boson can join, and the Feynman rule reads it directly. **The rotor's entry is an amplitude**: it says how much of a line has become the other line after a finite parameter $\theta$, and it is the vertex summed to all orders. **The two are not the same object read twice**, and the distance between them is the mass — which is why the same $\sin\theta$ is an oscillation on the massless directions and a frozen amplitude on the heavy ones.

**Why "role" and not "fate".** A fate is what the vacuum does to a boson, and [the bosons-in-detail article](the-15-axf-matrices-of-the-bosons-in-detail.html) gives it in one column: $32v^{2}$ six times, zero nine times. **A role is what the boson does to the four lines**, and it is not the same list: the corner is massless and multiplies all four lines by phases, the octet is massless and leaves the lepton line untouched. **Two partitions of the same fifteen, and this article keeps them apart.**

## Conventions

**The frame, the order and the arrays are the corpus's, and only the reading is this article's.** The quartet is ordered $(t,x,y,z)$, $E_{jk}$ is the matrix unit in that order, $A_{jk}=E_{jk}-E_{kj}$ is the real plane, $iS_{jk}=i(E_{jk}+E_{kj})$ is the imaginary plane, $iD=i\operatorname{diag}(-3,1,1,1)$ is the corner, and $d_{2}=i\operatorname{diag}(0,1,-1,0)$, $d_{3}=i\operatorname{diag}(0,0,1,-1)$ are the two colour diagonals. **Every array is anti-Hermitian and traceless**, and its rotor is

$$
R_{a}(\theta)=\exp\bigl(\theta\,G_{a}\bigr),
\qquad
\theta\ \text{real},
$$

**with the parameter written $\theta$ once and never $\omega t$**, since this article is about the matrix and not about the clock.

**The reading rule, and it is the only one used below.** The $j$-th column of $R_{a}(\theta)$ is the image of the $j$-th basis vector. **A $1$ on the diagonal is a line the rotor does not touch. A $\cos\theta$ on the diagonal is a line it touches without moving. A $\sin\theta$ off the diagonal is a line it moves to its partner. A $e^{\pm i\theta}$ or a $i\sin\theta$ is a line it touches with a phase and no motion.**

**Why $\theta$ and never a half angle.** None of the fifteen is half of another array, so none of the fifteen has a half angle in its rotor. **The $\tfrac12$ appears only when a composite is exponentiated**, and §*What the Rotor Entries Say That the Array Entries Do Not* says where the composites sit.

**One comparison decides the third reading of a role, and it is the vacuum.** With $\Phi_{0}=vD$ the breaking direction, the rotor is a symmetry of the vacuum exactly when the array commutes with $D$:

$$
[A,D]=0
\quad\Longleftrightarrow\quad
R_{A}(\theta)\,\Phi_{0}\,R_{A}(\theta)^{-1}=\Phi_{0}.
$$

**Nine arrays commute with $D$ and six do not**, and the count is the count of the massless and heavy vectors. **A massless boson of this model is a rotor that leaves the vacuum exactly where it was; a heavy one is a rotor that moves it.** That is the Higgs mechanism in the language of this article, and it is checked in the table at the end.

## The Ledger of the Fifteen, Read on the Rotors

**One row per boson, and the rotor's shape is the row's middle.**

| boson | array | the rotor | fixed lines | $m^{2}$ | role |
| --- | --- | --- | --- | --- | --- |
| $B'$ | $iD$ | four phases, one at triple rate | none | $0$ | the vacuum direction, and the only rotor that reaches the centre |
| $\bar X^{r}$ | $A_{tx}$ | real turn of the lepton–red plane | $y$, $z$ | $32v^{2}$ | lepton into red and back |
| $X^{r}$ | $iS_{tx}$ | the same plane, phased | $y$, $z$ | $32v^{2}$ | the second amplitude of the same pair |
| $\bar X^{g}$ | $A_{ty}$ | real turn of the lepton–green plane | $x$, $z$ | $32v^{2}$ | lepton into green and back |
| $X^{g}$ | $iS_{ty}$ | the same plane, phased | $x$, $z$ | $32v^{2}$ | the second amplitude |
| $\bar X^{b}$ | $A_{tz}$ | real turn of the lepton–blue plane | $x$, $y$ | $32v^{2}$ | lepton into blue and back |
| $X^{b}$ | $iS_{tz}$ | the same plane, phased | $x$, $y$ | $32v^{2}$ | the second amplitude |
| $g_{1}$ | $A_{xy}$ | real turn of the red–green plane | $t$, $z$ | $0$ | colour rotation |
| $g_{2}$ | $iS_{xy}$ | the same plane, phased | $t$, $z$ | $0$ | the second colour amplitude |
| $g_{4}$ | $A_{xz}$ | real turn of the red–blue plane | $t$, $y$ | $0$ | colour rotation |
| $g_{5}$ | $iS_{xz}$ | the same plane, phased | $t$, $y$ | $0$ | the second colour amplitude |
| $g_{6}$ | $A_{yz}$ | real turn of the green–blue plane | $t$, $x$ | $0$ | colour rotation |
| $g_{7}$ | $iS_{yz}$ | the same plane, phased | $t$, $x$ | $0$ | the second colour amplitude |
| $T^{c}_{3}$ | $d_{2}$ | two opposite phases | $t$, $z$ | $0$ | colour phase, red against green |
| $T^{c}_{8}$ | $d_{3}$ | two opposite phases | $t$, $x$ | $0$ | colour phase, green against blue |

**Fixed lines: fourteen rotors fix exactly two lines, and one fixes none.** The corner is the only rotor of the fifteen that touches all four lines, **and that is why it is the only one that can be central**: a rotor with a fixed line cannot be a multiple of the identity.

**The lepton line separates the fifteen into eight and seven.** Eight arrays annihilate $e_{t}$ — the six off-diagonal colour arrays and the two colour diagonals — and their rotors fix the lepton line for every $\theta$. **Those eight are the octet**, and they are the whole answer to "what is colour": the set of rotors that turn the colour triple and leave the lepton alone. The other seven are the corner, which multiplies $e_{t}$ by a phase, and the six leptoquarks, which move it into a colour line. **$8+7$ is the partition the ledger of the spectrum does not show.**

**Reality separates them into six and nine, and the split is the one the SU(4)–SO(4) note proves.** The six real planes give real matrices for every $\theta$; the nine complex arrays give complex matrices except at $\theta\in\pi\mathbb{Z}$. **At the half-turn the nine become real, and at $\theta=\pi$ every one of the fifteen is a diagonal of $\pm1$.**

## The Corner: $B'$, the Array the Vacuum Is Built From

$$
iD=i\begin{pmatrix}-3&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
\qquad
\exp\bigl(\theta\,iD\bigr)=
\begin{pmatrix}
e^{-3i\theta}&0&0&0\\
0&e^{i\theta}&0&0\\
0&0&e^{i\theta}&0\\
0&0&0&e^{i\theta}
\end{pmatrix}.
$$

**The entries.** Four phases, and the only rotor of the fifteen with no off-diagonal entry at all. **Three entries are $e^{i\theta}$ and one is $e^{-3i\theta}$**, and the corner cell is the one the array's $-3$ decides: the four exponents sum to zero, $(-3)+1+1+1=0$, which is the tracelessness of the array read on the rotor. **A rotor whose exponents sum to zero has determinant one**, and that is the whole of the reason the fifteen sit in $\mathrm{SU}(4)$.

**The reading.** The rotor multiplies the lepton line by a phase that runs three times as fast and backwards, and each colour line by a phase that runs forwards. **In the frame where the colour phase is removed the lepton runs at four times the rate**, $\exp(\theta iD)=e^{i\theta}\operatorname{diag}(e^{-4i\theta},1,1,1)$, which is the display [the charge-quantisation article](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html) prints from a different starting point.

**The role.** This is the array the vacuum is built from: $\Phi_{0}=vD$ with $D$ the same diagonal and $i$ removed, and $B-L=\tfrac13D$ on the quartet. **Its rotor is the only one of the fifteen that reaches the centre, and it reaches it four times a turn**:

$$
\exp\Bigl(k\tfrac{\pi}{2}\,iD\Bigr)=i^{k}\,\mathbb{1},
\qquad k=0,1,2,3,
$$

**so the statement "$B-L$ is exact at every scale" has a rotor form: the one rotor that can be a multiple of the identity is the one whose array the vacuum is made of.** No other rotor of the fifteen is ever central inside a turn: the twelve plane rotors and the two colour diagonals are central only at $\theta\in2\pi\mathbb{Z}$, and the value there is $+1$.

## The Six Leptoquarks: The Rotors That Move the Lepton Line

**One plane, two amplitudes, and the same rotor up to a factor of $i$.** Each of the three colour lines gives a plane with the lepton line, and each plane carries two arrays: the real one, whose rotor turns the plane by the full angle, and the imaginary one, whose rotor turns the same plane and multiplies the moved amplitude by $i$. **The first moves a real vector to a real vector; the second does not, and that is the whole difference between the two amplitudes of one complex field.**

### $\bar X^{r}$: $A_{tx}$, the real turn of the lepton–red plane

$$
A_{tx}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta A_{tx}\bigr)=
\begin{pmatrix}
\cos\theta&\sin\theta&0&0\\
-\sin\theta&\cos\theta&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
$$

**The entries.** Four nonzero entries and two fixed lines. **The $\cos\theta$ pair sits on the two lines the plane uses; the $\pm\sin\theta$ pair sits off the diagonal, with the $+$ at $(t,x)$ and the $-$ at $(x,t)$**; the $y$ and $z$ lines carry a $1$ and are untouched. **Real, with the off-diagonal pair antisymmetric, so the matrix is orthogonal**, and at $\theta=0.4$ the image of $e_{t}$ is $(0.9211,\,-0.3894,\,0,\,0)$.

**The reading.** The rotor takes the lepton line into the red line and keeps its length: **$\sin\theta$ is the amplitude that has become colour after a finite parameter, and $\cos\theta$ is the amplitude that has stayed leptonic.** The two are one circle, and **the entry never exceeds one**, which is the difference between this rotor and a boost.

**The role.** $\bar X^{r}$ is the leptoquark amplitude of the red plane: **the boson whose rotor moves the lepton line into the red line and back**, which is the definition of a leptoquark read on the matrix rather than on the charges. **It is heavy, $32v^{2}$, and the mass has a rotor form: this is one of the six rotors that do not leave the vacuum alone**, since $[A_{tx},D]\ne0$ and the rotor conjugates $D$ into a different diagonal.

**The plane closes.** $[A_{tx},iS_{tx}]=2i(E_{tt}-E_{xx})=-\tfrac23\bigl(iD+2d_{2}+d_{3}\bigr)$, **so the plane's two rotors and one diagonal combination generate an $\mathfrak{su}(2)$** — which is why the two amplitudes are one doublet and why no third amplitude sits on the same plane.

### $X^{r}$: $iS_{tx}$, the same plane with a phase on the moved amplitude

$$
iS_{tx}=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta\,iS_{tx}\bigr)=
\begin{pmatrix}
\cos\theta&i\sin\theta&0&0\\
i\sin\theta&\cos\theta&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
$$

**The entries.** The same four cells and the same two fixed lines, with the off-diagonal pair now $+i\sin\theta$ on both sides. **Symmetric instead of antisymmetric, and imaginary instead of real**, so the matrix is unitary and not orthogonal: at $\theta=0.4$ the image of $e_{t}$ is $(0.9211,\,0.3894i,\,0,\,0)$.

**The reading.** The $\cos\theta$ entries are the same as the real plane's; **the difference is entirely in the off-diagonal pair, and it is one factor of $i$.** So the rotor does not turn the real plane — it rotates the *complexified* plane, and on the circular lines $e_{t}\pm ie_{x}$ it is a pure phase, $e^{\pm i\theta}$.

**The role.** $X^{r}$ is the second amplitude of the same complex leptoquark field. **Its rotor coincides with $\bar X^{r}$'s at exactly the half-turns**, $\exp(\pi iS_{tx})=\exp(\pi A_{tx})=\operatorname{diag}(-1,-1,1,1)$, because there $\sin\pi=0$ and the $i$ has nothing to multiply. **Away from those points the two rotors differ, and the difference is what makes the pair a complex field rather than two real ones.**

### $\bar X^{g}$: $A_{ty}$, the real turn of the lepton–green plane

$$
A_{ty}=\begin{pmatrix}0&0&1&0\\0&0&0&0\\-1&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta A_{ty}\bigr)=
\begin{pmatrix}
\cos\theta&0&\sin\theta&0\\
0&1&0&0\\
-\sin\theta&0&\cos\theta&0\\
0&0&0&1
\end{pmatrix}.
$$

**The entries.** The same pattern one line over: $+\sin\theta$ at $(t,y)$, $-\sin\theta$ at $(y,t)$, $\cos\theta$ on the lepton and green lines, $1$ on $x$ and $z$. **The $y$ line is now turned where it was fixed before, and the $x$ line is now fixed where it was turned**, and that exchange is the whole difference from the red plane.

**The reading.** $\exp(\theta A_{ty})e_{t}=\cos\theta\,e_{t}-\sin\theta\,e_{y}$, **the same circle with a different partner.** The star carries the array to a colour plane with a minus, $\star A_{ty}=-A_{xz}$, and **the minus is the orientation of the pair $(x,z)$ against the order of the quartet** — it reappears in the recombination $A_{xz}=+(T^{L}_{y}-T^{R}_{y})$, the one plus sign among the six.

**The role.** $\bar X^{g}$ is the green leptoquark amplitude, with the same charge $-\tfrac23$, the same colour $\bar{\mathbf3}$ and the same mass $32v^{2}$. **The mass is identical in the three colours because the vacuum's three colour eigenvalues are equal**: the rotor's $\cos$ and $\sin$ are the same functions of $\theta$ on all six leptoquark planes, and colour enters only through which line is named.

### $X^{g}$: $iS_{ty}$, the same plane with the phase

$$
iS_{ty}=\begin{pmatrix}0&0&i&0\\0&0&0&0\\i&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta\,iS_{ty}\bigr)=
\begin{pmatrix}
\cos\theta&0&i\sin\theta&0\\
0&1&0&0\\
i\sin\theta&0&\cos\theta&0\\
0&0&0&1
\end{pmatrix}.
$$

**The entries.** $+i\sin\theta$ at $(t,y)$ and $(y,t)$, $\cos\theta$ on the two turned lines, $1$ on the other two. **Unitary, not orthogonal; real at the half-turn and nowhere else in a turn.**

**The reading.** $\exp(\theta\,iS_{ty})e_{t}=\cos\theta\,e_{t}+i\sin\theta\,e_{y}$: **the moved amplitude has gained a quarter turn**, so the lepton line does not become green — it becomes green with a phase, and a real apparatus cannot see that direction.

**The role.** $X^{g}$ completes the green pair exactly as $X^{r}$ completes the red one. **The reading worth keeping is the negative one**: nothing in the rotor of $X^{g}$ is new relative to $X^{r}$ except the name of a line, **so the six leptoquark rotors are one rotor read on three planes and in two amplitudes**, and the model has one leptoquark mass and not six.

### $\bar X^{b}$: $A_{tz}$, the real turn of the lepton–blue plane

$$
A_{tz}=\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\-1&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta A_{tz}\bigr)=
\begin{pmatrix}
\cos\theta&0&0&\sin\theta\\
0&1&0&0\\
0&0&1&0\\
-\sin\theta&0&0&\cos\theta
\end{pmatrix}.
$$

**The entries.** $+\sin\theta$ at $(t,z)$, $-\sin\theta$ at $(z,t)$, $\cos\theta$ on the lepton and blue lines, $1$ on $x$ and $y$. **The last of the three mixed planes, and its star image is the colour plane that shares its label**, $\star A_{tz}=+A_{xy}$.

**The reading.** $\exp(\theta A_{tz})e_{t}=\cos\theta\,e_{t}-\sin\theta\,e_{z}$, with both colour lines $x$ and $y$ fixed. **The rotor is a rotation of the pair (lepton, blue) and the identity on the other pair** — the sharpest single example of "a plane rotor is a rotation in two lines and nothing elsewhere".

**The role.** $\bar X^{b}$ is the blue leptoquark amplitude, charge $-\tfrac23$, mass $32v^{2}$, and its plane's bracket closes the third way, $[A_{tz},iS_{tz}]=-\tfrac23 iD+\tfrac23 d_{2}+\tfrac43 d_{3}$. **The three closures are the three independent diagonal combinations of the corner and the two colour phases**, so each leptoquark plane closes with the diagonal sector and no leptoquark plane closes with another.

### $X^{b}$: $iS_{tz}$, the last of the six

$$
iS_{tz}=\begin{pmatrix}0&0&0&i\\0&0&0&0\\0&0&0&0\\i&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta\,iS_{tz}\bigr)=
\begin{pmatrix}
\cos\theta&0&0&i\sin\theta\\
0&1&0&0\\
0&0&1&0\\
i\sin\theta&0&0&\cos\theta
\end{pmatrix}.
$$

**The entries.** $+i\sin\theta$ at $(t,z)$ and $(z,t)$, $\cos\theta$ on the turned pair, $1$ on the two colour lines it does not use. **The sixth and last of the heavy rotors.**

**The reading.** $\exp(\theta\,iS_{tz})e_{t}=\cos\theta\,e_{t}+i\sin\theta\,e_{z}$. **With this rotor the six are complete and the count of heavy vectors is six**, and the count is the number of arrays that move the lepton line without being the corner.

**The role.** $X^{b}$ is the blue amplitude, and **the sextet it completes is the only coloured massive set of the model**: six rotors, one mass, three colour lines, two amplitudes, and six charges that sum to zero. **The rotor language adds one fact to the ledger's**: all six have the same $\cos$ and the same $\sin$, so the sextet is degenerate at the symmetric point by the shape of the rotor and not by a symmetry of the potential.

## The Six Off-Diagonal Gluons: The Rotors That Leave the Lepton Line Alone

**The complement of the previous section, and its statement is negative and exact: these six rotors fix $e_{t}$ for every $\theta$, and $e_{t}$ is the one line they all leave alone.** Each turns a colour plane; each has a real and an imaginary amplitude; **none of them moves the lepton line, which is what "colour is the stabiliser" means when it is written on a rotor.**

### $g_{1}$: $A_{xy}$, the real turn of the red–green plane

$$
A_{xy}=\begin{pmatrix}0&0&0&0\\0&0&1&0\\0&-1&0&0\\0&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta A_{xy}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&\sin\theta&0\\
0&-\sin\theta&\cos\theta&0\\
0&0&0&1
\end{pmatrix}.
$$

**The entries.** Two $1$s on the lines outside the plane, the $\cos\theta$ pair on red and green, and the $\pm\sin\theta$ pair between them. **The lepton line carries a $1$ and so does the blue line**, and those two $1$s are the article's statement that colour leaves the lepton alone.

**The reading.** $\exp(\theta A_{xy})e_{x}=\cos\theta\,e_{x}-\sin\theta\,e_{y}$ with $e_{t}=e_{t}$ and $e_{z}=e_{z}$: **a rotation of the colour triple read inside the quartet.** At $\theta=\pi$ the rotor is the sign flip on the red–green plane, $\operatorname{diag}(1,-1,-1,1)$, **which is an involution of the group and not only a rotation of a plane: applied twice it gives the identity, and it is the element of order two a reader meets again at the centre.**

**The role.** $g_{1}$ is a gluon, and its rotor is a symmetry of the vacuum in the exact sense of the comparison above: $[A_{xy},D]=0$, so $R_{A_{xy}}(\theta)\Phi_{0}R_{A_{xy}}(\theta)^{-1}=\Phi_{0}$ for every $\theta$. **The rotor is the gauge transformation of the unbroken colour group**, and the zero mass is that sentence and not a separate computation.

### $g_{2}$: $iS_{xy}$, the same plane with the phase

$$
iS_{xy}=\begin{pmatrix}0&0&0&0\\0&0&i&0\\0&i&0&0\\0&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta\,iS_{xy}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&i\sin\theta&0\\
0&i\sin\theta&\cos\theta&0\\
0&0&0&1
\end{pmatrix}.
$$

**The entries.** The same four cells, one $i$ on each off-diagonal entry, and the same two $1$s. **Unitary and complex; real at the half-turns, where it equals $g_{1}$'s rotor.**

**The reading.** $\exp(\theta\,iS_{xy})e_{x}=\cos\theta\,e_{x}+i\sin\theta\,e_{y}$: **the same rotation with the moved amplitude phased**, and the circular lines $e_{x}\pm ie_{y}$ are multiplied by $e^{\mp i\theta}$.

**The role.** $g_{2}$ is the second gluon of the red–green plane, and **the pair $\{g_{1},g_{2}\}$ is one complex colour field**: the two rotors differ by the $i$ on the off-diagonal pair, which is the statement that the two arrays are the two amplitudes of one cell pair. **A colour plane contributes one complex field and not two real ones**, which is why the six off-diagonal colour arrays carry three complex colour fields, one per plane.

### $g_{4}$: $A_{xz}$, the real turn of the red–blue plane

$$
A_{xz}=\begin{pmatrix}0&0&0&0\\0&0&0&1\\0&0&0&0\\0&-1&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta A_{xz}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&0&\sin\theta\\
0&0&1&0\\
0&-\sin\theta&0&\cos\theta
\end{pmatrix}.
$$

**The entries.** $+\sin\theta$ at $(x,z)$, $-\sin\theta$ at $(z,x)$, $\cos\theta$ on red and blue, $1$ on the lepton and green lines. **The middle of the three colour planes, and the one whose star carries the minus**, $\star A_{xz}=-A_{ty}$.

**The reading.** $\exp(\theta A_{xz})e_{x}=\cos\theta\,e_{x}-\sin\theta\,e_{z}$ with the lepton and green lines fixed. **At $\theta=0.4$ the image of $e_{x}$ is $(0,\,0.9211,\,0,\,-0.3894)$**, real, orthogonal, and confined to the colour block.

**The role.** $g_{4}$, a gluon of the red–blue plane, massless by the same commutator. **Its bracket with its own imaginary partner gives a diagonal combination and not a single diagonal**, $[A_{xz},iS_{xz}]=2i(E_{xx}-E_{zz})=2(d_{2}+d_{3})$: **the middle colour plane sees both Cartan directions**, which is why the colour block's three brackets are $2d_{2}$, $2(d_{2}+d_{3})$ and $2d_{3}$ and not three copies of one.

### $g_{5}$: $iS_{xz}$, the same plane with the phase

$$
iS_{xz}=\begin{pmatrix}0&0&0&0\\0&0&0&i\\0&0&0&0\\0&i&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta\,iS_{xz}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&0&i\sin\theta\\
0&0&1&0\\
0&i\sin\theta&0&\cos\theta
\end{pmatrix}.
$$

**The entries.** $+i\sin\theta$ at $(x,z)$ and $(z,x)$, $\cos\theta$ on the two turned lines, $1$ on the lepton and green lines. **Unitary, and real at $\theta=\pi$.**

**The reading.** $\exp(\theta\,iS_{xz})e_{x}=\cos\theta\,e_{x}+i\sin\theta\,e_{z}$: **the phasing of the red–blue plane**, and the second of the three complex colour rotations.

**The role.** $g_{5}$ is the second gluon of the red–blue plane, massless and unbroken. **The octet's rotor content is therefore three real rotations, three complex rotations and two diagonal phases**, and only the first three are rotations of the quartet — **a reader who expects eight rotation angles finds six turns and two phases.**

### $g_{6}$: $A_{yz}$, the real turn of the green–blue plane

$$
A_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
\qquad
\exp\bigl(\theta A_{yz}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&\cos\theta&\sin\theta\\
0&0&-\sin\theta&\cos\theta
\end{pmatrix}.
$$

**The entries.** $+\sin\theta$ at $(y,z)$, $-\sin\theta$ at $(z,y)$, $\cos\theta$ on green and blue, and the $1$s on the lepton and red lines. **The only plane of the six that leaves the red line and the lepton line as $1$s**, and $\star A_{yz}=+A_{tx}$.

**The reading.** $\exp(\theta A_{yz})e_{y}=\cos\theta\,e_{y}-\sin\theta\,e_{z}$. **The rotor is a rotation of the last colour pair**, and its half-turn is the sign flip on that pair.

**The role.** $g_{6}$, a gluon of the green–blue plane, massless. **Its bracket with its partner is the third single diagonal**, $[A_{yz},iS_{yz}]=2i(E_{yy}-E_{zz})=2d_{3}$, and **the three brackets together are the whole diagonal content of the octet.**

### $g_{7}$: $iS_{yz}$, the last of the octet

$$
iS_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&i\\0&0&i&0\end{pmatrix},
\qquad
\exp\bigl(\theta\,iS_{yz}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&\cos\theta&i\sin\theta\\
0&0&i\sin\theta&\cos\theta
\end{pmatrix}.
$$

**The entries.** $+i\sin\theta$ at $(y,z)$ and $(z,y)$, $\cos\theta$ on green and blue, $1$ on the lepton and red lines. **The sixth and last off-diagonal colour rotor.**

**The reading.** $\exp(\theta\,iS_{yz})e_{y}=\cos\theta\,e_{y}+i\sin\theta\,e_{z}$. **With it the six off-diagonal colour rotors are complete**, three planes and two amplitudes each, and the count is the nine cells of the colour block minus the trace.

**The role.** $g_{7}$ is a gluon, and **the six off-diagonal rotors plus the two diagonals below are the octet**: eight rotors, each fixing the lepton line, each commuting with $D$, each massless at every step of the chain.

## The Two Colour Diagonals: The Rotors That Phase Two Colour Lines

### $T^{c}_{3}$: $d_{2}$, red against green

$$
d_{2}=i\begin{pmatrix}0&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&0\end{pmatrix},
\qquad
\exp\bigl(\theta d_{2}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&e^{i\theta}&0&0\\
0&0&e^{-i\theta}&0\\
0&0&0&1
\end{pmatrix}.
$$

**The entries.** Four diagonal entries and no off-diagonal entry: **two $1$s, one $e^{i\theta}$ and one $e^{-i\theta}$.** The two phases are opposite, and their product is one, so the determinant is one.

**The reading.** Nothing moves; **two lines are multiplied by opposite phases and two are left alone.** The rotor is diagonal, so it commutes with every diagonal rotor, and **that is the whole reason the Cartan of the octet is abelian**.

**The role.** $T^{c}_{3}$ is one of the two Cartan directions of the colour group, massless and unbroken because $[d_{2},D]=0$. **It is one of the eight rotors that fix the lepton line**, and among the eight it is one of the two that turn nothing: it fixes blue, and multiplies red and green by opposite phases.

### $T^{c}_{8}$: $d_{3}$, green against blue

$$
d_{3}=i\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix},
\qquad
\exp\bigl(\theta d_{3}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&e^{i\theta}&0\\
0&0&0&e^{-i\theta}
\end{pmatrix}.
$$

**The entries.** One $e^{i\theta}$ on green, one $e^{-i\theta}$ on blue, and $1$ on the lepton and red lines. **The second and last colour phase.**

**The reading.** $\exp(\theta d_{3})$ fixes the lepton line and the red line, **so the two colour diagonals fix the lepton line and one colour line each** — $d_{2}$ fixes blue, $d_{3}$ fixes red — and between them they give the two independent colour phase directions, with the third colour line playing the role of the trace.

**The role.** $T^{c}_{8}$ is the second Cartan direction, massless, and **its one exceptional property is the trace form**: $\operatorname{tr}(d_{2}d_{3})=+1$, so the two diagonals are not orthogonal. **That is a statement about the basis and not about the group** — any two independent combinations of the two phases would serve — **and it is the only pair of the $105$ whose Gram entry is nonzero.** The rotors still commute, and the two parameters compose into a two-angle torus with no correction:

$$
\exp\bigl(\beta d_{2}+\gamma d_{3}\bigr)
=\operatorname{diag}\bigl(1,\,e^{i\beta},\,e^{-i\beta+i\gamma},\,e^{-i\gamma}\bigr),
$$

**and the corner can be added to it**, because it commutes with both:

$$
\exp\bigl(\alpha iD+\beta d_{2}+\gamma d_{3}\bigr)
=\operatorname{diag}\Bigl(e^{-3i\alpha},\,e^{i(\alpha+\beta)},\,e^{i(\alpha-\beta+\gamma)},\,e^{i(\alpha-\gamma)}\Bigr),
$$

**four phases with one relation among them, which is rank three.** That is the only multi-parameter rotor of the model written in closed form, and it is closed for the reason the Cartan is abelian.

## What the Rotor Entries Say That the Array Entries Do Not

**Three statements, and each is a comparison of the two matrices in one subsection.**

**First, a vertex is not an amplitude.** The array's entry is $1$ or $i$ and says which two lines the boson can join; **the rotor's entry is $\sin\theta$ and says how much of one line has become the other after a finite parameter.** For a massless boson the two agree in the only way they can — the vertex is unsuppressed and the amplitude is a circle — while for a heavy one the circle is no longer free: **$\theta$ is then a field and not a symmetry parameter, the vacuum sits at one value of it, and the oscillation about that value is the $32v^{2}$.**

**Second, the mass is a statement about the vacuum and the rotor makes it visible.** Nine rotors leave $\Phi_{0}$ fixed and six move it, and the six are exactly the six with $32v^{2}$:

$$
[A,D]=0\ \text{for the nine}\ \Longleftrightarrow\ R_{A}(\theta)\Phi_{0}R_{A}(\theta)^{-1}=\Phi_{0},
$$

**so "massless" and "the rotor is a symmetry of the vacuum" are one statement and not two.** **The corner is in the nine and fixes no line; the octet is in the nine and fixes the lepton line** — which is why the ledger of the mass and the ledger of what the rotors do are two different partitions of the same fifteen.

**Third, the two amplitudes of a plane are not two bosons.** The rotor of $iS_{jk}$ is the rotor of $A_{jk}$ with one factor of $i$ on the off-diagonal pair, **so the pair is one plane, one angle, and two phases of one field.** The count that follows is the corpus's: **fifteen arrays and fifteen rotors, eight of them the colour octet and seven the corner and the sextet** — and the redundancy the corpus warns about is not in this list: the six composites are products of two of these rotors and not rotors of their own.

**And the composites, said once so that they are not smuggled in.** $T^{L}_{a}$ and $T^{R}_{a}$ are halves of sums and differences of the plane arrays, so their rotors are products of the rotors printed here, at half the parameter:

$$
\exp\bigl(\theta A_{ta}\bigr)=\exp\bigl(-\theta T^{L}_{a}\bigr)\exp\bigl(-\theta T^{R}_{a}\bigr),
\qquad
\bigl[T^{L}_{a},T^{R}_{b}\bigr]=0 ,
$$

**and the half angle of a composite is the full angle of the plane it is half of.** **No rotor in this article has a half angle**, because no array in this article is half of another; the fifteen are independent, and the rank of the fifteen as $4\times4$ matrices is fifteen.

## The Checks

Sixteen recomputations, with the quartet ordered $(t,x,y,z)$ and $\theta$ one real parameter.

| check | computation | result |
| --- | --- | --- |
| the closed forms | each rotor against the eigen-decomposition at $\theta=0.37$, $0.4$, $1.1$, $2.3$ | maximum deviation $2.2\times10^{-16}$ |
| the determinant | $\exp(\theta\operatorname{tr}G)$, all fifteen traceless | $1$ on all fifteen |
| real for every $\theta$ | $\max\lvert\operatorname{Im}R\rvert$ at three parameters | $6$ arrays at $2.1\times10^{-17}$, $9$ arrays at $0.93$ |
| real at the half-turn | $R(\pi)$ for the nine complex arrays | real, a diagonal of $\pm1$, on all nine |
| the period | $\lVert R(2\pi)-\mathbb{1}\rVert$ | $\le 7.4\times10^{-16}$ on all fifteen |
| the half-turn of a plane | $R_{A_{jk}}(\pi)$, $R_{iS_{jk}}(\pi)$ | the sign flip on the plane, $+1$ elsewhere; the two agree |
| the corner at the quarter turns | $\exp(k\tfrac{\pi}{2}iD)$ | $i^{k}\mathbb{1}$, $k=0,1,2,3$ |
| centrality | the parameter at which $R$ is a multiple of $\mathbb{1}$ | $k\tfrac{\pi}{2}$ for the corner only; $2\pi$ for the fourteen |
| the fixed lines | $\dim\ker(R-\mathbb{1})$ | $2$ for fourteen rotors, $0$ for $iD$ |
| the lepton line | arrays with $G e_{t}=0$ | $8$: the six colour planes and the two diagonals |
| the moved lepton line | arrays with $G e_{t}\ne0$ | $7$: the corner and the six leptoquarks |
| the vacuum comparison | $R_{A}\Phi_{0}R_{A}^{-1}$ against $\Phi_{0}$ | equal for the nine, displaced by $1.13$ at $\theta=0.3$ for the six |
| the masses | $\operatorname{tr}([G,\Phi_{0}]^{\dagger}[G,\Phi_{0}])$ with $v=1$ | $32$ six times, $0$ nine times |
| the plane brackets | $[A_{jk},iS_{jk}]$ | $2d_{2}$, $2(d_{2}+d_{3})$, $2d_{3}$, and one diagonal combination per leptoquark plane |
| the Gram of the diagonals | $\operatorname{tr}(d_{2}d_{3})$ | $+1$, the only nonzero off-diagonal entry of the fifteen |
| the torus | $\exp(\alpha iD+\beta d_{2}+\gamma d_{3})$ | four phases, one relation, no correction term |

## Summary

**Fifteen matrices, fifteen rotors, one per boson, and every rotor is elementary because every array squares to a diagonal.** One corner, six leptoquarks, six off-diagonal gluons and two colour diagonals.

**Three kinds of nonzero entry and no more.** A cosine that stays, a sine that moves, a phase that multiplies. **The six real planes carry the first two and are real for every $\theta$; the six imaginary planes carry the same pair with an $i$ and are real only at the half-turns; the corner and the two diagonals carry phases and no motion.**

**The role of a boson is read off its rotor in two comparisons.** Eight rotors fix the lepton line and are the octet; seven do not, and they are the corner, which phases it, and the six leptoquarks, which move it into colour. **Nine rotors leave the vacuum exactly where it was and are massless; six move it and are the $32v^{2}$.**

**The corner is the only rotor that reaches the centre**, four times a turn with values $i^{k}$, and it is the only one that can be central because it is the only one with no fixed line. **That is the rotor form of "$B-L$ is exact at every scale", and it is one line: the array the vacuum is made of is the array whose rotor can be a multiple of the identity.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $R_{a}(\theta)$ | $\exp(\theta G_{a})$, the rotor of the array $G_{a}$ |
| $A_{jk}$ | the real plane $E_{jk}-E_{kj}$ |
| $iS_{jk}$ | the imaginary plane $i(E_{jk}+E_{kj})$ |
| $iD$ | the corner $i\operatorname{diag}(-3,1,1,1)$ |
| $d_{2}$, $d_{3}$ | the two colour diagonals |
| $\Phi_{0}=vD$ | the breaking direction, with $D=\operatorname{diag}(-3,1,1,1)$ |
| fixed line | a line whose column in the rotor is that line itself, a $1$ on the diagonal |
| role | what the rotor does to the four lines: which it fixes, which it moves, and whether it leaves the vacuum alone |
| $8+7$ | rotors that fix the lepton line, and rotors that do not |
| $9+6$ | rotors that leave the vacuum alone, and rotors that move it |

## Further Reading

- [Construction of the AXF Matrices of the Rotors of the Fifteen Generators](construction-of-the-axf-matrices-of-the-rotors-of-the-fifteen-generators.html). The fifteen closed forms this article reads entry by entry.
- [The Fifteen AXF Matrices of the Bosons in Detail](the-15-axf-matrices-of-the-bosons-in-detail.html). The same fifteen as arrays: the spectrum, the mass, the Hodge star and the fate.
- [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html). Where the fifteen come from, in three steps.
- [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html). Which space each rotor turns, and the proofs that none of them is a boost.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). Every bracket quoted in the sections above, with its five rules.
- [Classification of the Bosons in the $\mathrm{SU}(4)$ Model](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The grid that names the cells, and the ledger the rows above are written in.
- [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). The corner's relative phase, which the first section's display reproduces.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-the-id-condensate-and-the-six-carriers-it-makes-heavy.html). The mass form, the nine zeros, and the vacuum that decides which rotors are symmetries.
