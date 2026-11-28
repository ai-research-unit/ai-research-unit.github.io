# __The Fifteen AXF Matrices of the Bosons in Detail: Every Matrix, Every Boson, Its Entries, Its Spectrum and Its Fate__

## Introduction

**This article takes the fifteen arrays one at a time, in fifteen sections, one per array.** [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html) builds them: six raw arrays halved, sixteen words minus the trace, six pairs summed and differenced. It states their properties in families. **Here each array gets its display, the entries it carries, the spectrum it has, the plane it turns or the phase it imposes, and the boson it is**.

**The frame is the same frame and is not restated.** The quartet is ordered $(t,x,y,z)$, the array of an operator is read by columns, $E_{jk}$ is the matrix unit in that order, and the multiplication is $\vec e_x\vec e_y=\vec e_z$ cyclically. [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html) owns the frame and [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html) owns the derivations. **No array below is a Pauli array, a gamma array or a Gell-Mann array**, and none is chosen: each is one of the three operations applied to the six.

**The naming rule, and the one convention in it.** The $4\times4$ grid of the quartet carries one name per cell, printed in [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). **The array $A_{jk}$ carries the boson named in the cell $(j,k)$, and the array $iS_{jk}$ of the same plane carries the other amplitude of that pair.** So the real array of the plane $\{t,x\}$ carries $\bar X^{r}$, the name of the cell $(t,x)$, and the imaginary array carries $X^{r}$. **Which of the two amplitudes takes which of the two names is a convention and no number depends on it**; the corpus states that once and this article uses it once.

**Every section is titled with the boson first and the array second**, so the table of contents reads as the boson content of the model: **the corner, the six leptoquarks with their charges, the six spatial planes, and the three frame directions.** That is the whole list.

**The diagonal is printed in the declared frame, and the corner is the sum of it.** The three diagonal arrays of the fifteen are $iM_{j}=i\bigl(E_{jj}-E_{tt}\bigr)$ with $j=x,y,z$, and **the direction the vacuum is built from is their sum and not a sixteenth array**,

$$
iD=i\sum_{j}M_{j}=i\operatorname{diag}(-3,1,1,1).
$$

**A basis that contains $iD$ is a legitimate basis**, and it is the one in which the broken phase names its bosons: $iD$ together with $d_{2}=\tfrac i2(M_y-M_x)$ and $d_{3}=\tfrac i2(M_z-M_y)$ spans the same three dimensions. **It is not the declared basis**, and the difference shows in one place: in the frame each leptoquark plane closes with a single diagonal array, $[A_{tj},iS_{tj}]=-2iM_{j}$, while in the broken-phase basis it closes with a combination. **Every other number — entries, spectra, trace norms, masses — is identical in the two bases**, because the two differ by an invertible integer rotation of a three-dimensional space.

**Why an array and not a name.** An array is a matrix; a boson is a particle. **The passage from one to the other is the article's subject, and it is short**: the entries say which cells the generator moves, the spectrum says what its exponential does to the quartet, and the mass says what the vacuum does to it — **which above $M_C$ is nothing, for all fifteen.** **Each subsection makes those three statements and stops.**

**The fifteen, indexed.**

| boson | kind | array | cells moved | $m^{2}$ above $M_C$ |
| --- | --- | --- | --- | --- |
| $B'$ | the corner direction, the sum of the three diagonal arrays | $iD=i(M_x+M_y+M_z)$ | the four diagonal cells | $0$ |
| $\bar X^{r}$ | the red leptoquark, charge $-\tfrac23$ | $A_{tx}$ | $(t,x)$ and $(x,t)$ | $0$ |
| $X^{r}$ | the red leptoquark, charge $+\tfrac23$ | $iS_{tx}$ | $(t,x)$ and $(x,t)$ | $0$ |
| $\bar X^{g}$ | the green leptoquark, charge $-\tfrac23$ | $A_{ty}$ | $(t,y)$ and $(y,t)$ | $0$ |
| $X^{g}$ | the green leptoquark, charge $+\tfrac23$ | $iS_{ty}$ | $(t,y)$ and $(y,t)$ | $0$ |
| $\bar X^{b}$ | the blue leptoquark, charge $-\tfrac23$ | $A_{tz}$ | $(t,z)$ and $(z,t)$ | $0$ |
| $X^{b}$ | the blue leptoquark, charge $+\tfrac23$ | $iS_{tz}$ | $(t,z)$ and $(z,t)$ | $0$ |
| $g_{1}$ | the red–green plane, real array | $A_{xy}$ | $(x,y)$ and $(y,x)$ | $0$ |
| $g_{2}$ | the red–green plane, imaginary array | $iS_{xy}$ | $(x,y)$ and $(y,x)$ | $0$ |
| $g_{4}$ | the red–blue plane, real array | $A_{xz}$ | $(x,z)$ and $(z,x)$ | $0$ |
| $g_{5}$ | the red–blue plane, imaginary array | $iS_{xz}$ | $(x,z)$ and $(z,x)$ | $0$ |
| $g_{6}$ | the green–blue plane, real array | $A_{yz}$ | $(y,z)$ and $(z,y)$ | $0$ |
| $g_{7}$ | the green–blue plane, imaginary array | $iS_{yz}$ | $(y,z)$ and $(z,y)$ | $0$ |
| $iM_{x}$ | the frame direction weighting the red line against the lepton line | $iM_{x}$ | $(t,t)$ and $(x,x)$ | $0$ |
| $iM_{y}$ | the frame direction weighting the green line against the lepton line | $iM_{y}$ | $(t,t)$ and $(y,y)$ | $0$ |
| $iM_{z}$ | the frame direction weighting the blue line against the lepton line | $iM_{z}$ | $(t,t)$ and $(z,z)$ | $0$ |

**One array per boson, fifteen arrays, fifteen generators, and the ledger is a bijection.** The fifteen sections below are the twelve planes and the three $iM_{j}$; **$B'$ stands above them because it is their sum and not a member**, printed first because it is the one array with an entry of modulus three. There is no name in the fifteen that is a combination of other names, and no direction of the algebra that is missing from them. **The mass column is the spectrum above $M_C$, and above $M_C$ it is zero on all sixteen rows**; the column below $M_C$ takes two values, and it is [The Restructuring of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html)'s.

**None of the fifteen is a gluon above $M_C$, and none carries a colour.** The group there is one simple factor and no $\mathrm{SU}(3)$ is made local, so the words *gluon* and *colour* name cells of the grid and nothing that exists. **They are held on deposit for the phase below $M_C$**, where the eight directions of the $3\times3$ block are the connections of an unbroken factor; above it the words carry no content, and [Conceptual Conventions](conceptual-conventions.html) states the rule. **What exists above $M_C$ is fifteen directions, one coupling, and no invariant that separates one direction from another.** **That is the difference the model makes**: a ledger with more names than dimensions is a ledger of a bigger algebra read in a redundant basis, and this one is neither.

## What Every Subsection Uses, and Where It Comes From

**The properties are in the family table of the construction article, and they are not printed a second time.** [The Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html) gives, for each of the six families, the entries, the number of cells, the norm $\operatorname{tr}(X^{\dagger}X)$ and the spectrum. **This article uses those numbers and adds the two things the family table does not carry**: the mass form of a single array, and the Hodge star.

**The mass form, and why it vanishes here.** Above $M_C$ there is no condensate: $Ξ_0=0$ and
$$
m^{2}(X)=\operatorname{tr}\bigl([X,Ξ_0]^{\dagger}[X,Ξ_0]\bigr)=0
$$
for each of the fifteen, because the commutator with zero vanishes. **The fifteen are exactly degenerate above $M_C$, and the degeneracy is a property of the algebra and not of a scale.** **Below $M_C$ the same trace is taken with $Ξ_0=vD$, $D=\operatorname{diag}(-3,1,1,1)$, and it gives $32v^{2}$ on six arrays and $0$ on nine**; that computation, with the coherent $\mathfrak{so}(4)$ sums that give $16v^{2}$ and the reason $16v^{2}$ is not a mass, is [The Restructuring of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html)'s and is not repeated here. **The $v$ is the $\mathrm{SU}(4)$-breaking value**, and it is the only breaking value this model has.

**The star.** On the real antisymmetric arrays the Hodge star of $\mathbb{R}^4$ acts, $\star(dt\wedge dx)=dy\wedge dz$ and cyclically, with $\star^{2}=+1$. **It gives $\star T^{L}_{a}=+T^{L}_{a}$ and $\star T^{R}_{a}=-T^{R}_{a}$** on the six $\mathfrak{so}(4)$ arrays, and on the six real planes $\star A_{tx}=+A_{yz}$, $\star A_{ty}=-A_{xz}$, $\star A_{tz}=+A_{xy}$. **The star is not defined on the nine imaginary arrays**, which are not two-forms.

## The Six Arrays That Are Not Bosons Here

**Six matrices are printed in the construction article and are absent from this one, and the absence is a statement.**

**The six.** $T^{L}_{a}=\tfrac12 L_{\mathrm{axf}}(\vec e_a)$ and $T^{R}_{a}=\tfrac12 R_{\mathrm{axf}}(\vec e_a)$, $a=x,y,z$. Each is half a sum or a difference of two planes, $T^{L}_{a}=-\tfrac12(A_{ta}+A_{bc})$ and $T^{R}_{a}=-\tfrac12(A_{ta}-A_{bc})$ with $(a,b,c)$ cyclic. **They span $\mathfrak{so}(4)$, six real dimensions inside the fifteen, and they are not independent directions of the algebra.**

**Why they get no subsection.** A subsection in this article states four things: the entries, the spectrum, the plane the array turns, and the boson it is. **The first three hold for the six and are the first three of the plane arrays they are made of. The fourth fails**, and above $M_C$ the reason is a count: $T^{L}_{a}=-\tfrac12(A_{ta}+A_{bc})$ is a sum of two of the fifteen, so it spans no direction the fifteen do not already span. **A sixteenth row in the ledger would name a combination, and a combination is not a boson.**

**Below $M_C$ a second reason appears, and it is spectral.** There the two halves of $T^{L}_{a}$ take different masses and the sum is a coherence,

$$
m^{2}\bigl(T^{L}_{a}\bigr)=\tfrac12\bigl(32v^{2}\bigr)+\tfrac12\bigl(0\bigr)=16v^{2},
$$

**and $16v^{2}$ is not a mass**, because no term of the mass matrix is diagonal in it. **That sentence belongs to the broken phase and is [The Restructuring of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html)'s**; above $M_C$ there is nothing for it to say, since all fifteen are degenerate.

**What the six do carry, and it is not nothing.** They are the arrays in which the real $\mathfrak{so}(4)$ of the quartet is visible: $T^{L}$ closes with $+\epsilon_{abc}$, $T^{R}$ with $-\epsilon_{abc}$, and the two triples commute. **That is a true statement about a subalgebra and it is not a particle content.** The corpus keeps the computation in [Construction of the AXF Matrices](construction-of-the-axf-matrices-of-the-fifteen-generators.html) and in [The Commutation Table](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html).

## The Corner Direction, Before the Fifteen

### $B'$: $iD=iM_x+iM_y+iM_z$, the corner, the sum of three of the fifteen and the one array with an entry of modulus three

$$
iD=i\bigl(W_{xx}+W_{yy}+W_{zz}\bigr)=\begin{pmatrix}-3i & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & i\end{pmatrix}
$$

**The entries.** Four diagonal cells, and the only entry of modulus $\ne1$ in the whole fifteen: $-3i$ at the corner. **The display is the sum of the three frame arrays**, $iD=iM_x+iM_y+iM_z$, so its entries are sums of $\pm i$ and its norm is the norm of a sum, not of a member. **Trace zero because $-3+1+1+1=0$**, norm $12$ because $9+1+1+1=12$, spectrum $-3i,i,i,i$. **The corner cell carries minus the sum of the other three**, and that is the only way a diagonal with three equal entries can be traceless. **The same equation read as charges is $3\cdot(+1)+(-3)=0$** — and the $-3$ is the count of spatial lines, the same number that appears as $N-1$ in the charge quantum $e/(N-1)$. **The number is not "the trace removed"**: removing the trace is deleting the word $W_{tt}$ from the sixteen to reach fifteen, which is a count of arrays, while $-3$ is an eigenvalue of the sum of three of the fifteen.

**The exponential.** Four phases and no rotation,
$$
\exp(\theta\, iD)=\operatorname{diag}\bigl(e^{-3i\theta},\,e^{i\theta},\,e^{i\theta},\,e^{i\theta}\bigr).
$$
At $\theta=0.4$ the lepton phase is $0.3624-0.9320i$ and each strong phase is $0.9211+0.3894i$. **The array moves no index and turns no plane**; it multiplies the four lines by four phases.

**The boson.** $B'$ is the $B-L$ boson, and **the array is the one the vacuum is built from**. With the $i$ removed, $D=\operatorname{diag}(-3,1,1,1)$ is the Hermitian direction of the breaking, $Ξ_0=vD$, and $B-L=\tfrac13D$ on the $\mathbf4$: the charge is this array divided by three, which in charges reads $(-1,\tfrac13,\tfrac13,\tfrac13)$ with the lepton first.

**What the vacuum does not see.** $[iD,Ξ_0]=0$, so this array is invisible to the first breaking — and it is not alone: nine directions commute with $D$, the eight of the spatial block and $B'$ itself. **The unique statement is narrower and it is the one that matters here**: of the nine arrays that involve the $t$ line, six move it and three weight it, and **$B'$ is the one combination of the three that is blind to which spatial line it weights** — the three weights are equal, and that equality is what makes the corner entry $-3$.

**Its mass depends on which vacuum is assumed, and the two descriptions differ.** If the first breaking is by a direction that commutes with it — an adjoint-type vev along the lepton line — $B'$ stays massless down to $v$. On the minimal content of the corpus, one breaking at $v_C$ carrying the line and a right doublet, it does not: [The Weak Sector Below $M_C$](the-weak-sector-below-m-c-three-neutrals-a-diagonal-charged-pair-and-the-bidoublet.html) gives it a diagonal entry $\tfrac38g^2v_C^2$ and a share $\tfrac35$ of the $Z_R$, whose mass is $\tfrac58g^2v_C^2$. **So "massless until the weak breaking" is true in the first description and false in the second, and the corpus uses the second.**

**Downstream, after a mixing this model does not contain, it is one of the three ingredients of $\gamma$, $Z$ and $Z_R$**, with the share $\tfrac16$ that $Q$ gives it in the basis where $Q=T_3+\tfrac16D$, and it supplies the hypercharge coupling $g_{\mathrm Y}$. [The Matching at $M_C$](matching-at-m-c.html) has the stabilisers and [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html) has the ledger.

**The address.** The corner weighs the three spatial lines equally, and that equality is what the entry $-3$ means; **no letter is singled out here**, so the address is the three rows at once.

## The Fifteen, One Array at a Time

### $\bar X^{r}$, the red leptoquark of charge $-\tfrac23$: $A_{tx}$, the real plane through the lepton line

$$
A_{tx}=E_{tx}-E_{xt}=\begin{pmatrix}0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, $+1$ at $(t,x)$ and $-1$ at $(x,t)$, and nothing on the other eight off-diagonal cells or on the diagonal. **Real antisymmetric, so anti-Hermitian as it stands**, trace zero, norm $2$, spectrum $0,0,\pm i$.

**The exponential.** A rotation of the lepton–red plane by the full angle,
$$
\exp(\theta A_{tx})e_t=\cos\theta\,e_t-\sin\theta\,e_x,\qquad \exp(\theta A_{tx})e_y=e_y,\qquad \exp(\theta A_{tx})e_z=e_z ,
$$
and at $\theta=0.4$ the image of $e_t$ is $(0.9211,\,-0.3894,\,0,\,0)$. **Real and orthogonal, so it is a rotation of the quartet** and not a boost: [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators.html) proves that no exponential of the fifteen arrays is a boost. **The star carries it to the spatial plane**, $\star A_{tx}=+A_{yz}$, and that is why the self-dual combination $A_{tx}+A_{yz}=-2T^{L}_{x}$ is a half.

**The boson.** $\bar X^{r}$ is a leptoquark: **the array moves the lepton line into the red line and back**, which is the definition of a leptoquark and the reason the cell $(t,x)$ sits in the mixed band. Charge $-\tfrac23$, $B-L=-\tfrac43$, the red line. **Mass $0$ above $M_C$**, as for all fifteen: no condensate exists there to give the plane a mass. **Below $M_C$ it takes $32v^{2}=2v^{2}(1-(-3))^{2}$**, twice the square of the lepton-minus-spatial difference of $D$, and that value is [The Restructuring of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html)'s. **The bracket with its partner is exact**, $[A_{tx},iS_{tx}]=2i(E_{tt}-E_{xx})=-2iM_{x}$, so the plane's two arrays and one frame direction close into an $\mathfrak{su}(2)$, with no combination needed. [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html) owns the sector.

**The address.** The two cells are $\ell\bar r$ and $r\bar\ell$: **red is the row $x$**, a coordinate of the table and not a property of the array.

### $X^{r}$, the red leptoquark of charge $+\tfrac23$: $iS_{tx}$, the imaginary amplitude on the same plane

$$
iS_{tx}=i\bigl(E_{tx}+E_{xt}\bigr)=\begin{pmatrix}0 & i & 0 & 0 \\ i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, both $+i$, and the same two cells as $A_{tx}$. **Imaginary symmetric, and anti-Hermitian because $i$ times a real symmetric array is**, trace zero, norm $2$, spectrum $0,0,\pm i$.

**The exponential.** A complex rotation of the same plane,
$$
\exp(\theta\, iS_{tx})e_t=\cos\theta\,e_t+i\sin\theta\,e_x ,
$$
giving $(0.9211,\,0.3894i,\,0,\,0)$ at $\theta=0.4$. **Unitary and not orthogonal**: the image of a real unit vector has an imaginary component, so this exponential does not act on the real quartet at all. **That is the $6+9$ split read on one plane**, and it is why the article separates the arrays that rotate from the arrays that phase.

**The boson.** $X^{r}$ is the other amplitude of the same complex leptoquark field as $\bar X^{r}$. **Charge $+\tfrac23$, $B-L=+\tfrac43$, mass $0$ above $M_C$**, from the same plane and the same degeneracy. **The pair is one complex field and the two arrays are its real and imaginary parts**, which the corpus states as a convention: calling the real array the particle and the imaginary one the antiparticle is the $i$ convention and not a physical distinction. **What is not a convention is that both arrays are supported on the same two cells**, and therefore that the particle and the antiparticle of a plane come in one pair of mirrored cells.

**The address.** The same address as $\bar X^{r}$: **the second amplitude of one cell pair**, and the letter names a row for the pair and not for the amplitude.

### $\bar X^{g}$, the green leptoquark of charge $-\tfrac23$: $A_{ty}$, the real plane through the lepton line

$$
A_{ty}=E_{ty}-E_{yt}=\begin{pmatrix}0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, $+1$ at $(t,y)$ and $-1$ at $(y,t)$. **Real antisymmetric, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{ty})e_t=\cos\theta\,e_t-\sin\theta\,e_y$, with $e_x$ and $e_z$ fixed. **The star gives $\star A_{ty}=-A_{xz}$**, the minus being the orientation of the complementary pair $(x,z)$ against the order of the quartet, and the same minus appears in the recombination $A_{xz}=+(T^{L}_{y}-T^{R}_{y})$.

**The boson.** $\bar X^{g}$, charge $-\tfrac23$, $B-L=-\tfrac43$, triplet $\bar{\mathbf3}$ in the green line. **Mass $0$ above $M_C$, and the same bracket structure**: $[A_{ty},iS_{ty}]=2i(E_{tt}-E_{yy})=-2iM_{y}$. **The three mixed planes are three copies of one computation**, and the sign differences between them are the $\epsilon$ of the pair resolution, not three physics.

**The address.** $\ell\bar g$ and $g\bar\ell$: **green is the row $y$**, a coordinate and not a charge.

### $X^{g}$, the green leptoquark of charge $+\tfrac23$: $iS_{ty}$, the imaginary amplitude on the same plane

$$
iS_{ty}=i\bigl(E_{ty}+E_{yt}\bigr)=\begin{pmatrix}0 & 0 & i & 0 \\ 0 & 0 & 0 & 0 \\ i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, both $+i$, on the green leptoquark plane. **Norm $2$, spectrum $0,0,\pm i$, unitary exponential and not orthogonal.**

**The exponential.** $\exp(\theta\, iS_{ty})e_t=\cos\theta\,e_t+i\sin\theta\,e_y$, the same form as the red plane with $y$ in place of $x$.

**The boson.** $X^{g}$, charge $+\tfrac23$, the particle of the green plane, mass $0$ above $M_C$. **All six mixed planes are degenerate with the other nine directions and with each other**, and the reason is the same one: above $M_C$ there is one mass, zero, so no spatial line can split anything. **Below $M_C$ the six share one value because $D$ is a multiple of the identity on the spatial triple**, and that is the breaking article's sentence.

**The address.** The same address as $\bar X^{g}$, the second amplitude; **one letter, two amplitudes, one address**.

### $\bar X^{b}$, the blue leptoquark of charge $-\tfrac23$: $A_{tz}$, the real plane through the lepton line

$$
A_{tz}=E_{tz}-E_{zt}=\begin{pmatrix}0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, $+1$ at $(t,z)$ and $-1$ at $(z,t)$. **Real antisymmetric, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{tz})e_t=\cos\theta\,e_t-\sin\theta\,e_z$, with $e_x$ and $e_y$ fixed. **The star gives $\star A_{tz}=+A_{xy}$**, so the self-dual completion of this plane is the half $-2T^{L}_{z}$.

**The boson.** $\bar X^{b}$, charge $-\tfrac23$, triplet $\bar{\mathbf3}$ in the blue line, mass $0$ above $M_C$. **The bracket is $[A_{tz},iS_{tz}]=2i(E_{tt}-E_{zz})=-2iM_{z}$**, the third of the three ways a leptoquark plane closes on a frame direction.

**The address.** $\ell\bar b$ and $b\bar\ell$: **blue is the row $z$**, and the three leptoquark planes are the three addresses of the mixed band.

### $X^{b}$, the blue leptoquark of charge $+\tfrac23$: $iS_{tz}$, the imaginary amplitude on the same plane

$$
iS_{tz}=i\bigl(E_{tz}+E_{zt}\bigr)=\begin{pmatrix}0 & 0 & 0 & i \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ i & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, both $+i$, on the blue leptoquark plane. **Norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta\, iS_{tz})e_t=\cos\theta\,e_t+i\sin\theta\,e_z$, complex and not orthogonal.

**The boson.** $X^{b}$, charge $+\tfrac23$, the particle of the blue plane, mass $0$ above $M_C$. **With it the mixed band is complete**: six arrays, six cells, one mass — zero — three spatial lines, and the six charges sum to zero. **Below $M_C$ these six take one common value and are the only set that does**, and that is where the scale enters at which the spatial lines stop being the whole story: [The Matching at $M_C$](matching-at-m-c.html).

**The address.** The same address as $\bar X^{b}$, the second amplitude; **the mixed band has three addresses and six amplitudes**, which is the $6$ of $15=6+6+3$.

### $g_{1}$, the red–green plane: $A_{xy}$, the real rotation

$$
A_{xy}=E_{xy}-E_{yx}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells inside the spatial block, $+1$ at $(x,y)$ and $-1$ at $(y,x)$, and nothing on the lepton line or the blue line. **Real antisymmetric, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** A rotation of the red–green plane that fixes the other two lines,
$$
\exp(\theta A_{xy})e_x=\cos\theta\,e_x-\sin\theta\,e_y,\qquad \exp(\theta A_{xy})e_t=e_t,\qquad \exp(\theta A_{xy})e_z=e_z .
$$
At $\theta=0.4$ the image of $e_x$ is $(0,\,0.9211,\,-0.3894,\,0)$. **The array is a rotation of the quartet that leaves the lepton line alone**, which is the geometric content of the statement that the strong group is a stabiliser, and it is the reason [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators.html) counts it among the three that turn space.

**The name, and the mass.** $g_{1}$ is a cell of the red–green plane, and **above $M_C$ it is a direction and not a particle**: no $\mathrm{SU}(3)$ is local there, so *gluon* is a name held on deposit for the phase below. **Its mass is zero at every step of the chain, exactly**, because $D$ is a multiple of the identity on the three spatial lines: the plane's two eigenvalues of $D$ are equal, the difference is zero, and the mass form above vanishes. **The same computation in the array language is one line**, $[A_{xy},D]=0$.

**The star.** $\star A_{xy}=+A_{tz}$: the red–green spatial plane and the blue leptoquark plane are one pair under the star, and that pairing is why the six planes split into three spatial and three mixed.

**The address.** The address is $r\bar g$ on one cell and $g\bar r$ on the other, **and the two writings are the two signs of one entry**: a pair of rows and not an ordered pair.

### $g_{2}$, the red–green plane: $iS_{xy}$, the complex rotation

$$
iS_{xy}=i\bigl(E_{xy}+E_{yx}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** The same two cells, both $+i$, and nothing else. **Imaginary symmetric, anti-Hermitian, trace zero, norm $2$, spectrum $0,0,\pm i$** — the spectrum of its real partner, entry for entry.

**The exponential.** $\exp(\theta\, iS_{xy})e_x=\cos\theta\,e_x+i\sin\theta\,e_y$, giving $(0,\,0.9211,\,0.3894i,\,0)$ at $\theta=0.4$, with $e_t$ and $e_z$ fixed. **Unitary and not orthogonal**: the image of a real unit vector has an imaginary part, so this exponential does not act on the real quartet.

**The mass.** $g_{2}$ is the second cell of the red–green plane, and its mass is zero for the same reason as $g_{1}$'s, $[iS_{xy},D]=0$. **The pair $\{g_{1},g_{2}\}$ is one complex strong field**, because the two arrays are conjugates under transpose-and-$i$: a spatial plane contributes one real strong field and not two independent phases, and that is why the octet is real.

**The address.** The same address again, with $i$ on both cells: **one complex field has one address and two phases**, so the block's six planes are three addresses with two phases each.

### $g_{4}$, the red–blue plane: $A_{xz}$, the real rotation

$$
A_{xz}=E_{xz}-E_{zx}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0\end{pmatrix}
$$

**The entries.** $+1$ at $(x,z)$ and $-1$ at $(z,x)$, and nothing on the other cells. **Real antisymmetric, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{xz})e_x=\cos\theta\,e_x-\sin\theta\,e_z$, fixing $e_t$ and $e_y$; at $\theta=0.4$ the image of $e_x$ is $(0,\,0.9211,\,0,\,-0.3894)$.

**The mass.** $g_{4}$, the real cell of the red–blue plane, massless by the same equality of diagonal entries. **Its bracket with its own imaginary partner is the one that ties the spatial block to its Cartan**, $[A_{xz},iS_{xz}]=2i(E_{xx}-E_{zz})=2i(M_{x}-M_{z})$, and it is the middle of the spatial block's three brackets.

**The star.** $\star A_{xz}=-A_{ty}$. One of the three spatial planes carries a minus in this pairing and the other two do not, because the sign is the orientation of the plane and not a choice of naming.

**The address.** $r\bar b$ and $b\bar r$, with **green the row the array does not touch**: the absence is part of the address and part of why this plane's bracket needs both Cartan directions.

### $g_{5}$, the red–blue plane: $iS_{xz}$, the complex rotation

$$
iS_{xz}=i\bigl(E_{xz}+E_{zx}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i \\ 0 & 0 & 0 & 0 \\ 0 & i & 0 & 0\end{pmatrix}
$$

**The entries.** Both cells $+i$. **Anti-Hermitian, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta\, iS_{xz})e_x=\cos\theta\,e_x+i\sin\theta\,e_z$, complex and not orthogonal, as in the red–green plane.

**The mass.** $g_{5}$, the second cell of the red–blue plane, massless. **A reader who expects eight rotation angles in a octet finds three rotations, three complex rotations and two diagonal phases instead**: three real planes, three imaginary planes and two strong phases, and only the first three are rotations of the quartet.

**The address.** The same address as $g_{4}$, the second phase; **the pair is one field and one address**.

### $g_{6}$, the green–blue plane: $A_{yz}$, the real rotation

$$
A_{yz}=E_{yz}-E_{zy}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0\end{pmatrix}
$$

**The entries.** $+1$ at $(y,z)$ and $-1$ at $(z,y)$. **Real antisymmetric, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{yz})e_y=\cos\theta\,e_y-\sin\theta\,e_z$, fixing $e_t$ and $e_x$; at $\theta=0.4$ the image of $e_y$ is $(0,\,0,\,0.9211,\,-0.3894)$.

**The mass.** $g_{6}$, the real cell of the green–blue plane, massless. **The bracket is $[A_{yz},iS_{yz}]=2i(E_{yy}-E_{zz})=2i(M_{y}-M_{z})$**, the third of the three, and the three together are the whole diagonal content of the spatial block.

**The star.** $\star A_{yz}=+A_{tx}$, the inverse of the assignment on the red–green plane.

**The address.** $g\bar b$ and $b\bar g$, with **red the row the array does not touch**.

### $g_{7}$, the green–blue plane: $iS_{yz}$, the complex rotation

$$
iS_{yz}=i\bigl(E_{yz}+E_{zy}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i \\ 0 & 0 & i & 0\end{pmatrix}
$$

**The entries.** Both cells $+i$. **Anti-Hermitian, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta\, iS_{yz})e_y=\cos\theta\,e_y+i\sin\theta\,e_z$, complex and not orthogonal.

**The mass.** $g_{7}$, the second cell of the green–blue plane, massless. **The six off-diagonal arrays $g_{1},g_{2},g_{4},g_{5},g_{6},g_{7}$ plus the two diagonal directions of the spatial block are the eight**: the grid's $3\times3$ block has nine cells, the trace is removed, and eight derived directions remain. **Below $M_C$ those eight are the connections of an unbroken $\mathrm{SU}(3)$ and the word for them is gluon; above it the eight is a set of directions and no group is local.**

**The address.** The same address as $g_{6}$, the second phase; **with it the block's three addresses are complete**.

### $iM_{x}$: $i(E_{xx}-E_{tt})$, the frame direction that weights the red line against the lepton line

$$
iM_{x}=i\bigl(E_{xx}-E_{tt}\bigr)=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two diagonal cells, $-i$ at $(t,t)$ and $+i$ at $(x,x)$, and nothing on the green or blue line. **Imaginary diagonal, anti-Hermitian, trace zero, norm $2$, spectrum $0,0,+i,-i$.**

**The exponential.** Two opposite phases and two fixed lines,
$$
\exp(\theta\,iM_{x})=\operatorname{diag}\bigl(e^{-i\theta},\,e^{i\theta},\,1,\,1\bigr),
$$
giving $0.9211-0.3894i$ on the lepton line and $0.9211+0.3894i$ on red at $\theta=0.4$. **On its own it does not map the real quartet to itself**: it is two opposite phases on two of the four lines and two fixed lines on the others, and it turns no plane. **Its partner is the plane**: $A_{tx}$, $iS_{tx}$ and $iM_{x}$ span an $\mathfrak{su}(2)$, the rotations of that $\mathfrak{su}(2)$ act on the real pair, and $iM_{x}$ is its phase direction.

**The name, and the mass.** $iM_{x}$ is one of the three diagonal arrays of the fifteen, and **it is the direction the red leptoquark plane closes on**: $[A_{tx},iS_{tx}]=-2iM_{x}$, so that plane's two arrays and this one diagonal close into an $\mathfrak{su}(2)$. **It is massless at every step**, $[iM_{x},D]=0$ being the commutator of two diagonals, and the mass form vanishes for the same reason. **It multiplies the corner by $-1$ and the red line by $+1$**, and that single difference is the whole content of the array.

**The address.** The array weighs the red row against the lepton row: **the letter names a row**, and $iM_{x}$ is a difference of two rows and not a property of red.

### $iM_{y}$: $i(E_{yy}-E_{tt})$, the same weighting on the green line

$$
iM_{y}=i\bigl(E_{yy}-E_{tt}\bigr)=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** $-i$ at $(t,t)$ and $+i$ at $(y,y)$. **Norm $2$, spectrum $0,0,+i,-i$**, and every statement of the previous section holds with red replaced by green.

**The exponential.** $\exp(\theta\,iM_{y})=\operatorname{diag}\bigl(e^{-i\theta},\,1,\,e^{i\theta},\,1\bigr)$.

**The name, and the mass.** Massless, and the direction the green leptoquark plane closes on, $[A_{ty},iS_{ty}]=-2iM_{y}$.

**The address.** The same difference on the green row, and the letter again names a row.

### $iM_{z}$: $i(E_{zz}-E_{tt})$, the third of the frame

$$
iM_{z}=i\bigl(E_{zz}-E_{tt}\bigr)=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i\end{pmatrix}
$$

**The entries.** $-i$ at $(t,t)$ and $+i$ at $(z,z)$. **Norm $2$, spectrum $0,0,+i,-i$.**

**The exponential.** $\exp(\theta\,iM_{z})=\operatorname{diag}\bigl(e^{-i\theta},\,1,\,1,\,e^{i\theta}\bigr)$.

**The name, and the mass.** Massless, and the direction the blue leptoquark plane closes on, $[A_{tz},iS_{tz}]=-2iM_{z}$.

**The three together, and the four facts the frame hands over.** **They are one orbit of the permutation of $x,y,z$**, and no member is fixed by it; **they are not mutually orthogonal**, $\operatorname{tr}(M_{j}M_{k})=2\delta_{jk}+(1-\delta_{jk})$, so a canonical kinetic term needs one integer rotation, to $A_{j}=\sum_{k}M_{k}-2M_{j}$ with $\operatorname{tr}(A_{j}A_{k})=4\delta_{jk}$; **their sum is the vacuum direction**, $D=M_{x}+M_{y}+M_{z}$, which is the only diagonal combination the permutation leaves fixed and the array $B'$ is built from; and **the sum is orthogonal to the two directions of the spatial block's Cartan**, because $\operatorname{tr}(DM_{j})=4$ for all three $j$ and therefore $\operatorname{tr}\bigl(D(M_{j}-M_{k})\bigr)=0$. [The Symmetric Diagonal Frame](the-symmetric-diagonal-frame-of-the-fifteen.html) proves that arithmetic and the impossibility of the same construction in $\mathfrak{su}(3)$; [The Commutation Table](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html) has the brackets.

**The address.** The same difference on the blue row; **the three frame directions are the three rows, each weighed once against the lepton row**.


## The Checks

Nineteen recomputations, at $\operatorname{tr}$ in the fundamental, the quartet ordered $(t,x,y,z)$, $i$ the imaginary unit and $\star$ the Euclidean star.

| check | computation | result |
| --- | --- | --- |
| the fifteen are anti-Hermitian and traceless | $X^{\dagger}=-X$, $\operatorname{tr}X=0$ | $15/15$ |
| the norms | $\operatorname{tr}(X^{\dagger}X)$ | $2$ on all fifteen; $12$ on their sum $iD$ |
| the cells | nonzero entries | $2$ on all fifteen; $4$ on the sum $iD$ |
| the spectra | eigenvalues | $0,0,+i,-i$ on all fifteen; $-3i,i,i,i$ on the sum $iD$ |
| the lepton rotation | $\exp(0.4A_{tx})e_t$ | $(0.9211,-0.3894,0,0)$ |
| the complex lepton rotation | $\exp(0.4\,iS_{tx})e_t$ | $(0.9211,\,0.3894i,\,0,\,0)$, unitary, not orthogonal |
| the corner's phases | $\exp(0.4\,iD)$ | $0.3624-0.9320i$ once and $0.9211+0.3894i$ three times |
| the frame phase, red | $\exp(0.4\,iM_{x})$ | $e^{-0.4i}$, $e^{0.4i}$, $1$, $1$ |
| the frame phase, green | $\exp(0.4\,iM_{y})$ | $e^{-0.4i}$, $1$, $e^{0.4i}$, $1$ |
| the frame phase, blue | $\exp(0.4\,iM_{z})$ | $e^{-0.4i}$, $1$, $1$, $e^{0.4i}$ |
| the group rotation | $\exp(0.4A_{xy})e_x$ | $(0,0.9211,-0.3894,0)$ |
| the star on the real planes | $\star A_{tx}$, $\star A_{ty}$, $\star A_{tz}$ | $+A_{yz}$, $-A_{xz}$, $+A_{xy}$ |
| the plane bracket | $[A_{jk},iS_{jk}]$ against $2i(E_{jj}-E_{kk})$ | $6/6$ exact |
| the leptoquark bracket in the frame | $[A_{tj},iS_{tj}]$ against $-2iM_{j}$ | $3/3$ exact |
| the masses | $\operatorname{tr}([X,Ξ_0]^{\dagger}[X,Ξ_0])$ at $Ξ_0=0$ | $0$ on all fifteen |
| the six $\mathfrak{so}(4)$ arrays | their coordinates on the fifteen | inside the span, no new direction |
| the six arrays in the fifteen | their coordinates | $0$ entries outside the span |
| the Gram of the fifteen | $105$ pairs | $102$ zero, three at $\operatorname{tr}(M_{j}M_{k})=+1$ |
| the sum's norm | $\operatorname{tr}(D^{2})$ | $12$ |

## Summary

**Fifteen arrays, one per boson, and the index at the top is the whole table of contents.** One corner direction that is the sum of three, six leptoquarks, six spatial planes and three frame directions.

**Two behaviours and not fifteen.** A real plane array has a real orthogonal exponential and turns its plane; an imaginary one has a unitary exponential and phases its lines. **Only the six real planes rotate the quartet**, and the two halves of the article follow that split.

**Two spectra.** $0,0,+i,-i$ on all fifteen, and $-3i,i,i,i$ on their sum, the corner. **Nothing else appears**, and that is why every exponential in the article has a closed form.

**One mass, and it is zero.** $0$ on all fifteen above $M_C$, and on the corner that is their sum, because there is no condensate to break the degeneracy. **Below $M_C$ six take $32v^{2}$ and nine take $0$**, and the $32$ is twice the square of the lepton-minus-spatial difference of $D$; **that column, with the $16v^{2}$ that is not a mass, is [The Restructuring of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html)'s.**

**Every plane closes with its partner, and in the frame the closure is exact and single.** $[A_{jk},iS_{jk}]=2i(E_{jj}-E_{kk})$ holds on all six planes: in the spatial block it gives $2i(M_{x}-M_{y})$, $2i(M_{x}-M_{z})$ and $2i(M_{y}-M_{z})$, and each leptoquark plane gives one frame direction with no combination, $[A_{tj},iS_{tj}]=-2iM_{j}$. **Nothing closes at the corner**, which is the sum and not a member.

**The six absent matrices are absent because they are sums.** Each is a combination of two of the fifteen, so it spans nothing new above $M_C$; below $M_C$ each is half heavy and half massless, and the coherence argument is the breaking article's. **A ledger of coherences would have fifteen more rows and no more particles.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $E_{jk}$ | the matrix unit in the order $(t,x,y,z)$ |
| $A_{jk}$ | $E_{jk}-E_{kj}$, the real array of the plane $\{j,k\}$ |
| $iS_{jk}$ | $i(E_{jk}+E_{kj})$, the imaginary array of the same plane |
| $iD$ | $i\operatorname{diag}(-3,1,1,1)=i(M_{x}+M_{y}+M_{z})$, the corner, the sum of the three frame arrays |
| $M_{j}$ | $E_{jj}-E_{tt}$, $j=x,y,z$: the three diagonal arrays of the fifteen, the symmetric frame |
| $A_{j}$ | $\sum_{k}M_{k}-2M_{j}$, the orthogonal sibling, $\operatorname{tr}(A_{j}A_{k})=4\delta_{jk}$ |
| $d_{2}$, $d_{3}$ | the broken phase's two spatial differences, $\tfrac i2(M_{y}-M_{x})$ and $\tfrac i2(M_{z}-M_{y})$ |
| $T^{L}_{a}$, $T^{R}_{a}$ | $\tfrac12L_{\mathrm{axf}}(\vec e_a)$ and $\tfrac12R_{\mathrm{axf}}(\vec e_a)$; the six $\mathfrak{so}(4)$ arrays, not bosons here |
| $\star$ | the Hodge star of $\mathbb{R}^4$ with the Euclidean metric, $\star^2=+1$ |
| $m^{2}(X)$ | $\operatorname{tr}([X,Ξ_0]^{\dagger}[X,Ξ_0])$, the diagonal entry of the mass matrix |
| $X^{a}$, $\bar X^{a}$ | the two leptoquark amplitudes on line $a$ |
| $g_{1}\dots g_{7}$ | the six spatial-plane arrays, named by the cell they occupy: gluons below $M_C$ and directions above it |
| $T^{c}_{3}$, $T^{c}_{8}$ | the broken phase's names for the spatial block's two Cartan directions |
| $v$ | the $\mathrm{SU}(4)$-breaking value, the only breaking value of this model |

## The Three Letters, and the Colour Word

**Everything above was written with four line names and no further argument, and the word enters here for one reason: it is the literature's word for what a letter would name, and a reader will meet it.** **This article is one of exactly three places in the corpus where it is discussed.** [Conceptual Conventions](conceptual-conventions.html) states the rule and the ground it stands on; here the letters are read on the matrices; [The Eight AXF Matrices of the Gluons in Detail](the-eight-axf-matrices-of-the-gluons-in-detail-every-matrix-every-gluon-its-entries-its-spectrum-and-its-fate.html) reads them on the octet. **Every other article uses *the strong group*, *the triplet index*, *the spatial block* or *the count*.**

**The carrier and its letters.**

$$
(t,x,y,z)\;\longleftrightarrow\;(\ell,r,g,b),\qquad E_{ij}\;\longleftrightarrow\;i\bar j .
$$

Four lines, four letters, one object. **$E_{ij}$ moves line $j$ into line $i$, and its label reads *line $i$ on line anti-$j$***; columns are sources and rows are targets, so the grid is the table of the array's entries.

**A letter is a coordinate of the table, and a colour is what the word would name if a letter named a property.** The table has sixteen cells, the trace removes one direction, and fifteen remain. **The letters name rows and columns. They are not eigenvalues, not conserved numbers, and not observables**, and each of the sixteen remarks above says which two rows of that array the letters address.

**Why four.** Because the carrier is four-dimensional and the group is one factor acting on it. **Three-line language belongs to the strong phase, and no $\mathrm{SU}(3)$ is a factor of the theory above $M_C$**: a subalgebra of a simple group is not a factor, and nothing makes it local there. **The count of spatial letters is three because one of the four lines is the lepton line**, not because a group carries three members. That is declaration (A), and it is the model's one input about which line is which.

**Three tests, and a charge fails all three.**

| test | what it asks | result |
| --- | --- | --- |
| relabelling | does the sentence survive a permutation of $x,y,z$? | the letters do not; the count $12+3$ does |
| basis rotation | is the label invariant under a local transformation? | no — the components rotate among the fifteen |
| degeneracy | does anything distinguish one label above $M_C$? | no — all fifteen are massless there |

**So no charge follows from the letters.** To read one is to hear a group with four members where there is one simple group on four lines. **The correct sentence is: fifteen directions of one simple group, of which twelve move a line and three weight the lines.** *The fourth line* is a shorter phrase with a narrower status: it is shorthand for the one declaration of the model, and it is written with the word *declaration* beside it or not at all.

**The empirical ground, and it is the strongest of the three.** **A colour is never observed in nature.** Confinement, imported as standard physics, keeps every non-singlet state out of the asymptotic spectrum: no isolated quark and no isolated gluon is observed, and every particle that comes back from a detector is a singlet. **So no measurement returns a colour**: the measurements fix the count, three, and the dimension of the group below $M_C$, eight, and nothing else. **The word is a name for an address, and an address is not a property that a detector can report.** [Confinement and the Loss of Partonic Information](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) states the same fact as the reason the asymptotic algebra is the singlet projection.

**What the letters buy, and it is real.** They make the grid readable in one glance: **the six leptoquarks are the cells that touch the lepton row, the six spatial planes are the cells of the $3\times3$ block, and the three frame directions weight one spatial line against the lepton line.** That is the picture of $15=6+6+3$, and it is the fastest way to see which array does what. **A picture is not a charge.**

**Below $M_C$ the letters acquire a group, and still not a charge.** The first breaking leaves $\mathrm{SU}(3)\times\mathrm U(1)$ local, so the eight directions of the $3\times3$ block are the connections of a real factor, and *gluon* is a fair name for them there. **Even there a letter pair is a coordinate on the adjoint of $\mathrm{SU}(3)$: what is physical is the group, its dimension eight, its rank two, the exclusion of the singlet, and the rates computed from them.** [The Eight AXF Matrices of the Gluons in Detail](the-eight-axf-matrices-of-the-gluons-in-detail-every-matrix-every-gluon-its-entries-its-spectrum-and-its-fate.html) prints the eight one at a time; [The Three Lines in $\mathrm{SU}(3)$](the-three-lines-in-su3-a-coordinate-label-on-the-eight-not-a-charge.html) carries the argument to the end.

**The ledger of the letters.**

| object | status |
| --- | --- |
| the four lines | the carrier, invariant |
| the letters $\ell,r,g,b$ | notation |
| a cell label $i\bar j$ | a coordinate |
| the twelve-and-three split | invariant: twelve roots, rank three |
| the eight below $M_C$ | the adjoint of a group factor |
| a colour as a property | never observed, and not claimed |
| the phrase "four colours" | a misnomer: four lines of one multiplet, not four group members |

**One sentence to carry away.** **A colour is a coordinate on a table, a coordinate is bookkeeping, and nothing of the kind is ever observed in nature; what survives a relabelling of the four lines is physics.** [Conceptual Conventions](conceptual-conventions.html) states the rule that admits the word here and in two other articles, and [The Symmetric Diagonal Frame](the-symmetric-diagonal-frame-of-the-fifteen.html) proves the one place where the fourth line does real work: it is what lets three diagonal directions be symmetric in the three spatial lines.

## Further Reading

- [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html), which builds every array printed here in three steps.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html), for the frame and the reading by columns.
- [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators.html), for each exponential and the proof that none of them is a boost.
- [The Fifteen AXF Matrices of the Boson Rotors in Detail](the-15-axf-matrices-of-the-boson-rotors-in-detail-every-matrix-every-boson-its-entries-its-role.html). The same closed forms read one boson at a time: the entries, the fixed lines, and the role of each matrix.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). Every bracket of every array with every other, which is where each fate in the last column of the family table comes from.
- [The Restructuring of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html), for the operator behind the $32v^{2}$, the nine zeros, and the general vacuum.
- [The Weak Sector Below $M_C$](the-weak-sector-below-m-c-three-neutrals-a-diagonal-charged-pair-and-the-bidoublet.html), for the charged block and the mixing the two weak triples undergo.
- [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html), for the grid that names the cells and the ledger.
- [Classification of the Bosons in the $\mathrm{SU}(4)$ Model](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html), which joins this article's fifteen subsections to the classification's cells in one ledger, names every array printed here, and reads the ledger three ways.
- [Charge Quantisation from the Fourth Line](charge-quantisation-from-the-fourth-line-one-trace-one-third.html), which reads the corner entry of $iD$ as the quark–lepton relation: $-3+1+1+1=0$, and where *the fourth line* is read as the declaration it is.
- [The Three Lines in $\mathrm{SU}(4)$: A Coordinate Label on the Fifteen, Not a Charge](the-three-lines-in-su4-a-coordinate-label-on-the-fifteen-not-a-charge.html), the argument behind the last section, and [The Symmetric Diagonal Frame](the-symmetric-diagonal-frame-of-the-fifteen.html), for the frame printed in the diagonal sections.
- [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html) and [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$](quantum-chromodynamics-as-the-residual-of-su4.html), for the two sectors the third part supplies.
