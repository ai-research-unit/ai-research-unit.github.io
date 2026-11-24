# __The 21 AXF Matrices of the Bosons in Detail: Every Matrix, Every Boson, Its Entries, Its Spectrum and Its Fate__

## Introduction

**This article takes the twenty-one arrays one at a time, in twenty-one sections, one per array.** [Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html) builds them: six raw arrays halved, sixteen words minus the trace, six pairs summed and differenced. It states their properties in families. **Here each array gets its display, the entries it carries, the spectrum it has, the plane it turns or the phase it imposes, and the boson it is**.

**The frame is the same frame and is not restated.** The quartet is ordered $(t,x,y,z)$, the array of an operator is read by columns, $E_{jk}$ is the matrix unit in that order, and the multiplication is $\vec e_x\vec e_y=\vec e_z$ cyclically. [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html) owns the frame and [Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html) owns the derivations. **No array below is a Pauli array, a gamma array or a Gell-Mann array**, and none is chosen: each is one of the three operations applied to the six.

**The naming rule, and the one convention in it.** The $4\times4$ grid of the quartet carries one name per cell, printed in [Classification of the Bosons](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html). **The array $A_{jk}$ carries the boson named in the cell $(j,k)$, and the array $iS_{jk}$ of the same plane carries the other amplitude of that pair.** So the real array of the plane $\{t,x\}$ carries $\bar X^{r}$, the name of the cell $(t,x)$, and the imaginary array carries $X^{r}$. **Which of the two amplitudes takes which of the two names is a convention and no number depends on it**; the corpus states that once and this article uses it once.

**Every section is titled with the boson first and the array second**, so the table of contents reads as the boson content of the model: the two charged bosons and the neutral boson of each weak triple, the fifteenth gauge boson, the six leptoquarks with their charges, and the eight gluons.

**Why an array and not a name.** An array is a matrix; a boson is a particle. **The passage from one to the other is the article's subject, and it is short**: the entries say which cells the generator moves, the spectrum says what its exponential does to the quartet, and the mass says what the vacuum does to it. **Each subsection makes those three statements and stops.**

**The twenty-one, indexed.**

| boson | kind | array | cells moved | mass |
| --- | --- | --- | --- | --- |
| $W^{+}_{L}$ | the left charged boson, first array | $T^{L}_{x}$ | $\{t,x\}$ and $\{y,z\}$, four cells | light eigenvalue of the charged block |
| $W^{-}_{L}$ | the left charged boson, second array | $T^{L}_{y}$ | $\{t,y\}$ and $\{x,z\}$, four cells | light eigenvalue of the charged block |
| $W^{3}_{L}$ | the left neutral boson | $T^{L}_{z}$ | $\{t,z\}$ and $\{x,y\}$, four cells | mixes into $\gamma$ and $Z$ |
| $W^{+}_{R}$ | the right charged boson, first array | $T^{R}_{x}$ | $\{t,x\}$ and $\{y,z\}$, four cells | the other eigenvalue of that block |
| $W^{-}_{R}$ | the right charged boson, second array | $T^{R}_{y}$ | $\{t,y\}$ and $\{x,z\}$, four cells | the other eigenvalue of that block |
| $W^{3}_{R}$ | the right neutral boson | $T^{R}_{z}$ | $\{t,z\}$ and $\{x,y\}$, four cells | mixes into $\gamma$, $Z$, $Z_R$ |
| $B'$ | the fifteenth gauge boson, the corner | $iD$ | the four diagonal cells | $0$ at the first breaking |
| $\bar X^{r}$ | the red leptoquark, charge $-\tfrac23$ | $A_{tx}$ | $(t,x)$ and $(x,t)$ | $32v^{2}$ |
| $X^{r}$ | the red leptoquark, charge $+\tfrac23$ | $iS_{tx}$ | $(t,x)$ and $(x,t)$ | $32v^{2}$ |
| $\bar X^{g}$ | the green leptoquark, charge $-\tfrac23$ | $A_{ty}$ | $(t,y)$ and $(y,t)$ | $32v^{2}$ |
| $X^{g}$ | the green leptoquark, charge $+\tfrac23$ | $iS_{ty}$ | $(t,y)$ and $(y,t)$ | $32v^{2}$ |
| $\bar X^{b}$ | the blue leptoquark, charge $-\tfrac23$ | $A_{tz}$ | $(t,z)$ and $(z,t)$ | $32v^{2}$ |
| $X^{b}$ | the blue leptoquark, charge $+\tfrac23$ | $iS_{tz}$ | $(t,z)$ and $(z,t)$ | $32v^{2}$ |
| $g_{1}$ | a gluon of the red–green plane, real array | $A_{xy}$ | $(x,y)$ and $(y,x)$ | $0$ |
| $g_{2}$ | a gluon of the red–green plane, imaginary array | $iS_{xy}$ | $(x,y)$ and $(y,x)$ | $0$ |
| $g_{4}$ | a gluon of the red–blue plane, real array | $A_{xz}$ | $(x,z)$ and $(z,x)$ | $0$ |
| $g_{5}$ | a gluon of the red–blue plane, imaginary array | $iS_{xz}$ | $(x,z)$ and $(z,x)$ | $0$ |
| $g_{6}$ | a gluon of the green–blue plane, real array | $A_{yz}$ | $(y,z)$ and $(z,y)$ | $0$ |
| $g_{7}$ | a gluon of the green–blue plane, imaginary array | $iS_{yz}$ | $(y,z)$ and $(z,y)$ | $0$ |
| $T^{c}_{3}$ | a colour gluon, the red–green phase | $d_{2}$ | two colour diagonal cells | $0$ |
| $T^{c}_{8}$ | a colour gluon, the green–blue phase | $d_{3}$ | two colour diagonal cells | $0$ |

**One array per boson, twenty-one arrays, fifteen directions.** The six weak arrays are two-term sums of the fifteen, $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$ and $A_{bc}=-\epsilon_{abc}(T^{L}_{a}-T^{R}_{a})$, so the twenty-one print twenty-one distinct matrices over fifteen independent ones. **That is why the ledger has twenty-one names and the algebra has fifteen dimensions**, and it is the reason the same boson can be met twice, once as a weak array and once as a pair of plane arrays.

## What Every Subsection Uses, and Where It Comes From

**The properties are in the family table of the construction article, and they are not printed a second time.** [The Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html) gives, for each of the six families, the entries, the number of cells, the norm $\operatorname{tr}(X^{\dagger}X)$ and the spectrum. **This article uses those numbers and adds the two things the family table does not carry**: the mass form of a single array, and the Hodge star.

**The mass form.** With $\Phi_0=vD$, $D=\operatorname{diag}(-3,1,1,1)$ and $X$ one array,
$$
m^{2}(X)=\operatorname{tr}\bigl([X,\Phi_0]^{\dagger}[X,\Phi_0]\bigr)=v^{2}\operatorname{tr}\bigl(X^{\dagger}[D,[D,X]]\bigr),
$$
which is the diagonal entry $M^{2}_{XX}$ of [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html). **It gives $32v^{2}$ on the six leptoquark arrays, $0$ on the nine colour and corner arrays, and $8v^{2}$ on the six weak arrays, which is not a mass**: the weak masses come from the bidoublet and not from $D$, and that article says why $8v^{2}$ is the artefact of reading a weak generator on the carrier. **The $v$ here is the $\mathrm{SU}(4)$-breaking value**; the charged block of Part I uses the bidoublet's, $v^{2}=\kappa^{2}+\kappa'^{2}$, and the two are different scales.

**The star.** On the real antisymmetric arrays the Hodge star of $\mathbb{R}^4$ acts, $\star(dt\wedge dx)=dy\wedge dz$ and cyclically, with $\star^{2}=+1$. **It gives $\star T^{L}_{a}=+T^{L}_{a}$ and $\star T^{R}_{a}=-T^{R}_{a}$**, and on the six real planes $\star A_{tx}=+A_{yz}$, $\star A_{ty}=-A_{xz}$, $\star A_{tz}=+A_{xy}$. **The star is not defined on the nine imaginary arrays**, which are not two-forms.

## Part I. The Three of $\mathfrak{su}(2)_L$

### $W^{+}_{L}$, the left charged boson: $T^{L}_{x}$, the first of its two arrays, the planes $\{t,x\}$ and $\{y,z\}$ turned together

$$
T^{L}_{x}=\tfrac12\ell_x=\begin{pmatrix}0 & -\tfrac12 & 0 & 0 \\ \tfrac12 & 0 & 0 & 0 \\ 0 & 0 & 0 & -\tfrac12 \\ 0 & 0 & \tfrac12 & 0\end{pmatrix}
$$

**The entries.** Four cells in two planes. The block $\{t,x\}$ carries $-\tfrac12$ at $(t,x)$ and $+\tfrac12$ at $(x,t)$; the block $\{y,z\}$ carries the same pair of signs. **Trace zero, norm $1$, spectrum $\pm\tfrac i2$ twice.**

**The exponential.** It is a real rotation, and it turns both planes by the half-angle in the same sense,
$$
\exp(\theta T^{L}_{x})e_t=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,e_x,\qquad
\exp(\theta T^{L}_{x})e_y=\cos\tfrac{\theta}{2}\,e_y+\sin\tfrac{\theta}{2}\,e_z .
$$
At $\theta=0.4$ the first gives $(0.9801,\,0.1987,\,0,\,0)$. **The array is self-dual, $\star\omega=+\omega$**, and that is the property that separates it from its right partner.

**The boson.** $W^{+}_{L}$ is charged and it couples to the left doublet. **The array is the real part of a complex generator**: the physical charged field is $W^{\pm}_{L}=(T^{L}_{x}\mp iT^{L}_{y})/\sqrt2$, so neither of the two arrays is charged by itself and the pair is one complex boson. **The two planes are why the generator is four cells wide.** A weak generator is not a plane of the quartet but a pair of planes, one leptoquark and one colour, and that is the structural fact the whole construction rests on. **Its mass is not its own.** $T^{L}_{x}$ and $T^{R}_{x}$ of the same label form one $2\times2$ charged block, and the block's two eigenvalues at equal couplings are $M^{2}_{\pm}=\tfrac14g^{2}v^{2}(1\mp\sin2\beta)$ with $v^{2}=\kappa^{2}+\kappa'^{2}$ and $\tan\beta=\kappa'/\kappa$. **The light eigenvalue is the Standard Model's $W$ and the heavy one is its right-handed partner**, and at $\beta=\tfrac\pi4$ the light one is exactly zero, which is a bound on the scalar sector and not a curiosity. The block is in [The Mass Matrix of the Twenty-One Gauge Bosons](the-mass-matrix-of-the-twenty-one-gauge-bosons-four-blocks-one-mixing-and-the-nine-zeros.html).

### $W^{-}_{L}$, the left charged boson: $T^{L}_{y}$, the second of the same two arrays, the same planes in the cyclic order

$$
T^{L}_{y}=\tfrac12\ell_y=\begin{pmatrix}0 & 0 & -\tfrac12 & 0 \\ 0 & 0 & 0 & \tfrac12 \\ \tfrac12 & 0 & 0 & 0 \\ 0 & -\tfrac12 & 0 & 0\end{pmatrix}
$$

**The entries.** The planes are $\{t,y\}$ and $\{x,z\}$, the complement of $y$ being the pair $(x,z)$ in cyclic order. **The signs are the ones of $T^{L}_{x}$ read on the cyclic triple**, and the difference from $T^{L}_{x}$ is which colour line the lepton line is paired with.

**The exponential.** The same form with $y$ in place of $x$,
$$
\exp(\theta T^{L}_{y})e_t=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,e_y,
$$
and the colour plane $\{x,z\}$ turns in the same sense. **Self-dual, norm $1$, spectrum $\pm\tfrac i2$ twice.**

**The boson.** $W^{-}_{L}$ is the other real component of the same complex field. **The two arrays have a bracket that is the third one**, $[T^{L}_{x},T^{L}_{y}]=T^{L}_{z}$, so the triple closes with $\epsilon_{abc}$ and the three labels are one algebra and not three unrelated matrices. **Nothing in the array distinguishes $+$ from $-$**: the sign of the charge is the sign of $i$ in the complex combination, which is a convention of the doublet and not a property of the quartet.

### $W^{3}_{L}$, the left neutral boson: $T^{L}_{z}$, the third of the triple and the one that mixes

$$
T^{L}_{z}=\tfrac12\ell_z=\begin{pmatrix}0 & 0 & 0 & -\tfrac12 \\ 0 & 0 & -\tfrac12 & 0 \\ 0 & \tfrac12 & 0 & 0 \\ \tfrac12 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** The planes are $\{t,z\}$ and $\{x,y\}$. **The block $\{x,y\}$ is the one the colour rotation $A_{xy}$ uses**, and that overlap is the reason this generator mixes into the photon.

**The exponential.** $\exp(\theta T^{L}_{z})e_t=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,e_z$, and the colour plane turns in step. **Self-dual, norm $1$, spectrum $\pm\tfrac i2$ twice.**

**The boson.** $W^{3}_{L}$ is the neutral of the left triple, and **which of the three arrays is called the neutral is the choice of Cartan**, the same choice that names $T^{c}_{3}$ and $T^{c}_{8}$ among the colour diagonals. **Its fate is the one difference between the three.** The charged pair acquires a mass at $v$ and nothing else; the neutral does not, because it shares the vacuum's neutrality, and it survives to mix with $B'$ and $W^{3}_{R}$ into the photon, the $Z$ and the $Z_R$. **The three neutral directions are the ones whose $3\times3$ block has a null vector**, and the null vector is the photon: [The Unbroken Subgroup](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html).

## Part II. The Three of $\mathfrak{su}(2)_R$

### $W^{+}_{R}$, the right charged boson: $T^{R}_{x}$, the first of its two arrays, the same planes turned oppositely

$$
T^{R}_{x}=\tfrac12 r_x=\begin{pmatrix}0 & -\tfrac12 & 0 & 0 \\ \tfrac12 & 0 & 0 & 0 \\ 0 & 0 & 0 & \tfrac12 \\ 0 & 0 & -\tfrac12 & 0\end{pmatrix}
$$

**The entries.** The block $\{t,x\}$ is identical to the one of $T^{L}_{x}$ and the block $\{y,z\}$ carries the opposite signs. **One sign per plane, and that is the whole difference between the two triples.**

**The exponential.** The lepton plane turns as before and the colour plane turns the other way,
$$
\exp(\theta T^{R}_{x})e_t=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,e_x,\qquad
\exp(\theta T^{R}_{x})e_y=\cos\tfrac{\theta}{2}\,e_y-\sin\tfrac{\theta}{2}\,e_z .
$$
At $\theta=0.4$ the image of $e_y$ is $(0,\,0,\,0.9801,\,-0.1987)$. **The array is anti-self-dual, $\star\omega=-\omega$.**

**The boson.** $W^{+}_{R}$ is the right-handed charged boson, and it is the reason the model is left–right symmetric rather than the Standard Model with a relabelled index. **Its mass is the second eigenvalue of the block it shares with $T^{L}_{x}$**, so the right-handed charged boson takes its mass from the mixing and not from a separate scale. **The weak masses are absent from the fifteen for that reason**: they come from the bidoublet, and the bidoublet is a different carrier from the quartet. **The anti-self-duality is what makes the two triples commute**: a self-dual and an anti-self-dual two-form are orthogonal, and $[T^{L}_{a},T^{R}_{b}]=0$ is that orthogonality read as an algebra.

### $W^{-}_{R}$, the right charged boson: $T^{R}_{y}$, the second of the same two arrays, the anti-self-dual partner

$$
T^{R}_{y}=\tfrac12 r_y=\begin{pmatrix}0 & 0 & -\tfrac12 & 0 \\ 0 & 0 & 0 & -\tfrac12 \\ \tfrac12 & 0 & 0 & 0 \\ 0 & \tfrac12 & 0 & 0\end{pmatrix}
$$

**The entries.** The planes are $\{t,y\}$ and $\{x,z\}$, with the colour block reversed as in $T^{R}_{x}$. **Norm $1$, spectrum $\pm\tfrac i2$ twice, anti-self-dual.**

**The exponential.** $\exp(\theta T^{R}_{y})e_t=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}e_y$ and $\exp(\theta T^{R}_{y})e_x=\cos\tfrac{\theta}{2}e_x-\sin\tfrac{\theta}{2}e_z$.

**The boson.** $W^{-}_{R}$ completes the right-handed charged pair. **The bracket in the right triple carries a minus**, $[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}T^{R}_{c}$, and that minus is the anti-homomorphism of right multiplication and not a different algebra: the set $\{-T^{R}_{a}\}$ closes with $+\epsilon_{abc}$. **A reader who compares the two triples sees one sign**, and should read it as the plane $\{y,z\}$ being turned backwards, which is also what the anti-self-dual star says.

### $W^{3}_{R}$, the right neutral boson: $T^{R}_{z}$, the neutral of the right triple

$$
T^{R}_{z}=\tfrac12 r_z=\begin{pmatrix}0 & 0 & 0 & -\tfrac12 \\ 0 & 0 & \tfrac12 & 0 \\ 0 & -\tfrac12 & 0 & 0 \\ \tfrac12 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** The planes are $\{t,z\}$ and $\{x,y\}$, the colour block reversed. **Norm $1$, spectrum $\pm\tfrac i2$ twice, anti-self-dual.**

**The exponential.** $\exp(\theta T^{R}_{z})e_t=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}e_z$ and $\exp(\theta T^{R}_{z})e_x=\cos\tfrac{\theta}{2}e_x-\sin\tfrac{\theta}{2}e_y$.

**The boson.** $W^{3}_{R}$ is the right-handed neutral. **It is the array that makes the neutral block rank two**, and the third neutral direction is the null one: the photon is a combination of $W^{3}_{L}$, $W^{3}_{R}$ and $B'$ with coefficients the vacuum fixes. **The mixing of the three is computed once, in [The Mass Matrix of the Twenty-One Gauge Bosons](the-mass-matrix-of-the-twenty-one-gauge-bosons-four-blocks-one-mixing-and-the-nine-zeros.html)**, and it is the only place in the boson sector where an angle other than a coupling ratio appears.

## Part III. The Fifteen of $\mathfrak{su}(4)$

### $B'$, the fifteenth gauge boson: $iD$, the corner, the one array with an entry of modulus three

$$
iD=i\bigl(W_{xx}+W_{yy}+W_{zz}\bigr)=\begin{pmatrix}-3i & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & i\end{pmatrix}
$$

**The entries.** Four diagonal cells, and the only entry of modulus $\ne1$ in the whole twenty-one: $-3i$ at the corner. **Trace zero because $-3+1+1+1=0$**, norm $12$ because $9+1+1+1=12$, spectrum $-3i,i,i,i$. **The corner cell carries minus the sum of the other three**, and that is the only way a diagonal with three equal entries can be traceless. **The same equation read as charges is $3\cdot(+1)+(-3)=0$**, which is [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html) — and the $-3$ is the count of colour lines, the same number that appears as $N-1$ in the charge quantum $e/(N-1)$. **The number is not "the trace removed"**: removing the trace is deleting the word $W_{tt}$ from the sixteen to reach fifteen, which is a count of arrays, while $-3$ is an eigenvalue of one of the fifteen.

**The exponential.** Four phases and no rotation,
$$
\exp(\theta\, iD)=\operatorname{diag}\bigl(e^{-3i\theta},\,e^{i\theta},\,e^{i\theta},\,e^{i\theta}\bigr).
$$
At $\theta=0.4$ the lepton phase is $0.3624-0.9320i$ and each colour phase is $0.9211+0.3894i$. **The array moves no index and turns no plane**; it multiplies the four lines by four phases.

**The boson.** $B'$ is the $B-L$ boson, and **the array is the one the vacuum is built from**. With the $i$ removed, $D=\operatorname{diag}(-3,1,1,1)$ is the Hermitian direction of the breaking, $\Phi_0=vD$, and $B-L=\tfrac13D$ on the $\mathbf4$: the charge is this array divided by three, which in charges reads $(-1,\tfrac13,\tfrac13,\tfrac13)$ with the lepton first.

**What the vacuum does not see.** $[iD,\Phi_0]=0$, so this array is invisible to the first breaking — and it is not alone: nine of the twenty-one commute with $D$, the eight gluons and $B'$ itself. **The unique statement is narrower and it is the one that matters here**: of the seven arrays that touch the $t$ line, $B'$ is the only one that leaves it in place.

**Its mass depends on which vacuum is assumed, and the two descriptions differ.** If the first breaking is by a direction that commutes with it — an adjoint-type vev along the lepton line — $B'$ stays massless down to $v$. On the minimal content of the corpus, one breaking at $v_R$ carrying the line and a right doublet, it does not: [The Neutral Sector](the-neutral-sector-of-the-four-colours-left-right-model-three-ingredients-rank-two-one-null-direction.html) gives it a diagonal entry $\tfrac38g^2v_R^2$ and a share $\tfrac35$ of the $Z_R$, whose mass is $\tfrac58g^2v_R^2$. **So "massless until the weak breaking" is true in the first description and false in the second, and the corpus uses the second.**

**After the mixing it is one of the three ingredients of $\gamma$, $Z$ and $Z_R$**, with the share $\tfrac16$ that $Q$ gives it in the basis where $Q=T_3+\tfrac16D$, and it supplies the hypercharge coupling $g_{\mathrm Y}$. [The Breaking Chain](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html) has the stabilisers and [Classification of the Bosons](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html) has the ledger.

### $\bar X^{r}$, the red leptoquark of charge $-\tfrac23$: $A_{tx}$, the real plane through the lepton line

$$
A_{tx}=E_{tx}-E_{xt}=\begin{pmatrix}0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, $+1$ at $(t,x)$ and $-1$ at $(x,t)$, and nothing on the other eight off-diagonal cells or on the diagonal. **Real antisymmetric, so anti-Hermitian as it stands**, trace zero, norm $2$, spectrum $0,0,\pm i$.

**The exponential.** A rotation of the lepton–red plane by the full angle,
$$
\exp(\theta A_{tx})e_t=\cos\theta\,e_t-\sin\theta\,e_x,\qquad \exp(\theta A_{tx})e_y=e_y,\qquad \exp(\theta A_{tx})e_z=e_z ,
$$
and at $\theta=0.4$ the image of $e_t$ is $(0.9211,\,-0.3894,\,0,\,0)$. **Real and orthogonal, so it is a rotation of the quartet** and not a boost: [The Rotors of the Twenty-One Generators](the-rotors-of-the-twenty-one-generators-in-the-four-colours-left-right-model-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) proves that no exponential of the twenty-one is a boost. **The star carries it to the colour plane**, $\star A_{tx}=+A_{yz}$, and that is why the self-dual combination $A_{tx}+A_{yz}=-2T^{L}_{x}$ is a weak array.

**The boson.** $\bar X^{r}$ is a leptoquark: **the array moves the lepton line into the red line and back**, which is the definition of a leptoquark and the reason the cell $(t,x)$ sits in the mixed band. Charge $-\tfrac23$, $B-L=-\tfrac43$, colour $\bar{\mathbf3}$. **Mass $32v^{2}=2v^{2}(1-(-3))^{2}$**, twice the square of the difference between the lepton eigenvalue and the colour eigenvalue of the vacuum: colour is unbroken because $D$ is a multiple of the identity on the colour triple, and the leptoquark is massive because the lepton line is not. **The bracket with its partner is exact**, $[A_{tx},iS_{tx}]=2i(E_{tt}-E_{xx})=-\tfrac23(iD+2d_{2}+d_{3})$, so the plane's two arrays and one diagonal close into an $\mathfrak{su}(2)$. [The Leptoquarks of the Four Colours Left–Right Model](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html) owns the sector.

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

**The boson.** $X^{r}$ is the other amplitude of the same complex leptoquark field as $\bar X^{r}$. **Charge $+\tfrac23$, $B-L=+\tfrac43$, mass $32v^{2}$** from the same plane and the same difference of eigenvalues. **The pair is one complex field and the two arrays are its real and imaginary parts**, which the corpus states as a convention: calling the real array the particle and the imaginary one the antiparticle is the $i$ convention and not a physical distinction. **What is not a convention is that both arrays are supported on the same two cells**, and therefore that the particle and the antiparticle of a plane come in one pair of mirrored cells.

### $\bar X^{g}$, the green leptoquark of charge $-\tfrac23$: $A_{ty}$, the real plane through the lepton line

$$
A_{ty}=E_{ty}-E_{yt}=\begin{pmatrix}0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, $+1$ at $(t,y)$ and $-1$ at $(y,t)$. **Real antisymmetric, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{ty})e_t=\cos\theta\,e_t-\sin\theta\,e_y$, with $e_x$ and $e_z$ fixed. **The star gives $\star A_{ty}=-A_{xz}$**, the minus being the orientation of the complementary pair $(x,z)$ against the order of the quartet, and the same minus appears in the recombination $A_{xz}=+(T^{L}_{y}-T^{R}_{y})$.

**The boson.** $\bar X^{g}$, charge $-\tfrac23$, $B-L=-\tfrac43$, colour $\bar{\mathbf3}$ in the green line. **Mass $32v^{2}$ and the same bracket structure**: $[A_{ty},iS_{ty}]=2i(E_{tt}-E_{yy})=-\tfrac23(iD-d_{2}+d_{3})$. **The three leptoquark planes are three copies of one computation**, and the sign differences between them are the $\epsilon$ of the pair resolution, not three physics.

### $X^{g}$, the green leptoquark of charge $+\tfrac23$: $iS_{ty}$, the imaginary amplitude on the same plane

$$
iS_{ty}=i\bigl(E_{ty}+E_{yt}\bigr)=\begin{pmatrix}0 & 0 & i & 0 \\ 0 & 0 & 0 & 0 \\ i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, both $+i$, on the green leptoquark plane. **Norm $2$, spectrum $0,0,\pm i$, unitary exponential and not orthogonal.**

**The exponential.** $\exp(\theta\, iS_{ty})e_t=\cos\theta\,e_t+i\sin\theta\,e_y$, the same form as the red plane with $y$ in place of $x$.

**The boson.** $X^{g}$, charge $+\tfrac23$, the particle of the green plane, mass $32v^{2}$. **The mass is the same for all six leptoquark arrays because $D$ is blind to which colour line the plane uses**: all three colour eigenvalues are $+1$ and the lepton eigenvalue is $-3$, so every mixed plane gets the same difference and colour never splits the sextet.

### $\bar X^{b}$, the blue leptoquark of charge $-\tfrac23$: $A_{tz}$, the real plane through the lepton line

$$
A_{tz}=E_{tz}-E_{zt}=\begin{pmatrix}0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, $+1$ at $(t,z)$ and $-1$ at $(z,t)$. **Real antisymmetric, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{tz})e_t=\cos\theta\,e_t-\sin\theta\,e_z$, with $e_x$ and $e_y$ fixed. **The star gives $\star A_{tz}=+A_{xy}$**, so the self-dual completion of this plane is the weak array $-2T^{L}_{z}$.

**The boson.** $\bar X^{b}$, charge $-\tfrac23$, colour $\bar{\mathbf3}$ in the blue line, mass $32v^{2}$. **The bracket is $[A_{tz},iS_{tz}]=2i(E_{tt}-E_{zz})=-\tfrac23 iD+\tfrac23 d_{2}+\tfrac43 d_{3}$**, the third of the three ways a leptoquark plane closes with the diagonal sector.

### $X^{b}$, the blue leptoquark of charge $+\tfrac23$: $iS_{tz}$, the imaginary amplitude on the same plane

$$
iS_{tz}=i\bigl(E_{tz}+E_{zt}\bigr)=\begin{pmatrix}0 & 0 & 0 & i \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ i & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells, both $+i$, on the blue leptoquark plane. **Norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta\, iS_{tz})e_t=\cos\theta\,e_t+i\sin\theta\,e_z$, complex and not orthogonal.

**The boson.** $X^{b}$, charge $+\tfrac23$, the particle of the blue plane, mass $32v^{2}$. **With it the sextet is complete**: six arrays, six bosons, one mass, three colours, and the six charges sum to zero. **The sextet is the only coloured massive set of the model**, and it fixes the scale $M_C$ at which colour stops being the whole story: [The Breaking Chain](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html).

### $g_{1}$, a gluon of the red–green plane: $A_{xy}$, the real rotation

$$
A_{xy}=E_{xy}-E_{yx}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two cells inside the colour block, $+1$ at $(x,y)$ and $-1$ at $(y,x)$, and nothing on the lepton line or the blue line. **Real antisymmetric, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** A rotation of the red–green plane that fixes the other two lines,
$$
\exp(\theta A_{xy})e_x=\cos\theta\,e_x-\sin\theta\,e_y,\qquad \exp(\theta A_{xy})e_t=e_t,\qquad \exp(\theta A_{xy})e_z=e_z .
$$
At $\theta=0.4$ the image of $e_x$ is $(0,\,0.9211,\,-0.3894,\,0)$. **The array is a rotation of the quartet that leaves the lepton line alone**, which is the geometric content of "colour is a stabiliser", and it is the reason [The Rotors of the Twenty-One Generators](the-rotors-of-the-twenty-one-generators-in-the-four-colours-left-right-model-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) counts it among the three that turn space.

**The boson.** $g_{1}$ is a gluon. **Its mass is zero at every step of the chain, exactly**, because $D$ is a multiple of the identity on the colour triple: the plane's two eigenvalues of $D$ are equal, the difference is zero, and the mass form above vanishes. **The same computation in the array language is one line**, $[A_{xy},D]=0$.

**The star.** $\star A_{xy}=+A_{tz}$: the red–green colour plane and the blue leptoquark plane are one pair under the star, and that pairing is why the six planes split into three colour and three mixed.

### $g_{2}$, a gluon of the red–green plane: $iS_{xy}$, the complex rotation

$$
iS_{xy}=i\bigl(E_{xy}+E_{yx}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** The same two cells, both $+i$, and nothing else. **Imaginary symmetric, anti-Hermitian, trace zero, norm $2$, spectrum $0,0,\pm i$** — the spectrum of its real partner, entry for entry.

**The exponential.** $\exp(\theta\, iS_{xy})e_x=\cos\theta\,e_x+i\sin\theta\,e_y$, giving $(0,\,0.9211,\,0.3894i,\,0)$ at $\theta=0.4$, with $e_t$ and $e_z$ fixed. **Unitary and not orthogonal**: the image of a real unit vector has an imaginary part, so this exponential does not act on the real quartet.

**The boson.** $g_{2}$ is the second gluon of the red–green plane, and its mass is zero for the same reason as $g_{1}$'s, $[iS_{xy},D]=0$. **The pair $\{g_{1},g_{2}\}$ is one complex colour field**, because the two arrays are conjugates under transpose-and-$i$: a colour plane contributes one real colour field and not two independent phases, and that is why the octet is real.

### $g_{4}$, a gluon of the red–blue plane: $A_{xz}$, the real rotation

$$
A_{xz}=E_{xz}-E_{zx}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0\end{pmatrix}
$$

**The entries.** $+1$ at $(x,z)$ and $-1$ at $(z,x)$, and nothing on the other cells. **Real antisymmetric, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{xz})e_x=\cos\theta\,e_x-\sin\theta\,e_z$, fixing $e_t$ and $e_y$; at $\theta=0.4$ the image of $e_x$ is $(0,\,0.9211,\,0,\,-0.3894)$.

**The boson.** $g_{4}$, a gluon of the red–blue plane, massless by the same equality of colour eigenvalues. **Its bracket with its own imaginary partner is the one that ties the octet to its Cartan**, $[A_{xz},iS_{xz}]=2i(E_{xx}-E_{zz})=2(d_{2}+d_{3})$, and it is the middle of the three colour brackets.

**The star.** $\star A_{xz}=-A_{ty}$. One of the three colour planes carries a minus in this pairing and the other two do not, because the sign is the orientation of the plane and not a choice of naming.

### $g_{5}$, a gluon of the red–blue plane: $iS_{xz}$, the complex rotation

$$
iS_{xz}=i\bigl(E_{xz}+E_{zx}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i \\ 0 & 0 & 0 & 0 \\ 0 & i & 0 & 0\end{pmatrix}
$$

**The entries.** Both cells $+i$. **Anti-Hermitian, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta\, iS_{xz})e_x=\cos\theta\,e_x+i\sin\theta\,e_z$, complex and not orthogonal, as in the red–green plane.

**The boson.** $g_{5}$, the second gluon of the red–blue plane, massless. **A reader who expects eight rotation angles in the octet finds three rotations, three complex rotations and two diagonal phases instead**: three real planes, three imaginary planes and two colour phases, and only the first three are rotations of the quartet.

### $g_{6}$, a gluon of the green–blue plane: $A_{yz}$, the real rotation

$$
A_{yz}=E_{yz}-E_{zy}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0\end{pmatrix}
$$

**The entries.** $+1$ at $(y,z)$ and $-1$ at $(z,y)$. **Real antisymmetric, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta A_{yz})e_y=\cos\theta\,e_y-\sin\theta\,e_z$, fixing $e_t$ and $e_x$; at $\theta=0.4$ the image of $e_y$ is $(0,\,0,\,0.9211,\,-0.3894)$.

**The boson.** $g_{6}$, a gluon of the green–blue plane, massless. **The bracket is $[A_{yz},iS_{yz}]=2i(E_{yy}-E_{zz})=2d_{3}$**, the third of the three, and the three together are the whole diagonal content of the octet.

**The star.** $\star A_{yz}=+A_{tx}$, the inverse of the assignment on the red–green plane.

### $g_{7}$, a gluon of the green–blue plane: $iS_{yz}$, the complex rotation

$$
iS_{yz}=i\bigl(E_{yz}+E_{zy}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i \\ 0 & 0 & i & 0\end{pmatrix}
$$

**The entries.** Both cells $+i$. **Anti-Hermitian, trace zero, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta\, iS_{yz})e_y=\cos\theta\,e_y+i\sin\theta\,e_z$, complex and not orthogonal.

**The boson.** $g_{7}$, the second gluon of the green–blue plane, massless. **The six off-diagonal arrays $g_{1},g_{2},g_{4},g_{5},g_{6},g_{7}$ plus the two diagonals are the octet**: the grid's $3\times3$ block has nine cells, the trace is removed, and eight traceless directions remain.

### $T^{c}_{3}$, the gluon of the red–green phase: $d_{2}$, a colour phase and not a rotation

$$
d_{2}=\tfrac i2\bigl(W_{yy}-W_{xx}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & -i & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

**The entries.** Two diagonal cells, $+i$ at $(x,x)$ and $-i$ at $(y,y)$, and nothing on the lepton line or the blue line. **Imaginary diagonal, norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** Two opposite phases and two fixed lines,
$$
\exp(\theta d_{2})=\operatorname{diag}\bigl(1,\,e^{i\theta},\,e^{-i\theta},\,1\bigr),
$$
giving $0.9211+0.3894i$ on red and $0.9211-0.3894i$ on green at $\theta=0.4$. **It preserves the real quartet**, because a phase pair $\pm\theta$ is a rotation when read on the two real lines together, but it is not a rotation of one plane: it fixes the lepton and blue lines and multiplies the other two.

**The boson.** $T^{c}_{3}$ is one of the two Cartan directions of the octet. **It is massless by the same accident**, $D$ being a multiple of the identity on the colour triple, and it is unbroken at every scale. **Its entries are the ones paired with the corner's trace**: the three colour phases together with $iD$ exhaust the diagonal sector, which is why four diagonal cells give three diagonal directions plus the trace.

### $T^{c}_{8}$, the gluon of the green–blue phase: $d_{3}$, the second colour phase

$$
d_{3}=\tfrac i2\bigl(W_{zz}-W_{yy}\bigr)=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & -i\end{pmatrix}
$$

**The entries.** Two diagonal cells, $+i$ at $(y,y)$ and $-i$ at $(z,z)$. **Norm $2$, spectrum $0,0,\pm i$.**

**The exponential.** $\exp(\theta d_{3})=\operatorname{diag}\bigl(1,\,1,\,e^{i\theta},\,e^{-i\theta}\bigr)$.

**The boson.** $T^{c}_{8}$ is the eighth colour diagonal, massless and unbroken. **One property is unique to this pair and it is the only exception among the fifteen**: $\operatorname{tr}(d_{2}d_{3})=+1$, so the two diagonals are not orthogonal in the trace form. **That is the array form of the statement that a colour basis is a choice and the algebra is not**: any two independent combinations of the two phases would serve, the octet's Cartan is fixed only up to a rotation among them, and the Gram entry is the price of writing them as $d_{2}$ and $d_{3}$.

## The Checks

Twenty-three recomputations, at $\operatorname{tr}$ in the fundamental, the quartet ordered $(t,x,y,z)$, $i$ the imaginary unit and $\star$ the Euclidean star.

| check | computation | result |
| --- | --- | --- |
| the twenty-one are anti-Hermitian and traceless | $X^{\dagger}=-X$, $\operatorname{tr}X=0$ | $21/21$ |
| the norms | $\operatorname{tr}(X^{\dagger}X)$ | $2$ fourteen times, $1$ six times, $12$ once |
| the cells | nonzero entries | $2$ fourteen times, $4$ seven times |
| the spectra | eigenvalues | $0,0,\pm i$ fourteen times; $\pm\tfrac i2$ twice six times; $-3i,i,i,i$ once |
| the lepton rotation | $\exp(0.4A_{tx})e_t$ | $(0.9211,-0.3894,0,0)$ |
| the complex lepton rotation | $\exp(0.4\,iS_{tx})e_t$ | $(0.9211,\,0.3894i,\,0,\,0)$, unitary, not orthogonal |
| the half-angle | $\exp(0.4T^{L}_{x})e_t$ | $(0.9801,0.1987,0,0)$ |
| the neutral of the left triple | $\exp(0.4T^{L}_{z})e_t$ | $(0.9801,0,0,0.1987)$ |
| the reversed colour plane | $\exp(0.4T^{R}_{x})e_y$ | $(0,0,0.9801,-0.1987)$ |
| the corner's phases | $\exp(0.4\,iD)$ | $0.3624-0.9320i$ once and $0.9211+0.3894i$ three times |
| the colour phases | $\exp(0.4d_{2})$ | $1$, $e^{0.4i}$, $e^{-0.4i}$, $1$ |
| the second colour phase | $\exp(0.4d_{3})$ | $1$, $1$, $e^{0.4i}$, $e^{-0.4i}$ |
| the colour rotation | $\exp(0.4A_{xy})e_x$ | $(0,0.9211,-0.3894,0)$ |
| the self-dual triple | $\star\omega(T^{L}_{a})$ against $\omega(T^{L}_{a})$ | $+1$ three times |
| the anti-self-dual triple | $\star\omega(T^{R}_{a})$ against $\omega(T^{R}_{a})$ | $-1$ three times |
| the star on the real planes | $\star A_{tx}$, $\star A_{ty}$, $\star A_{tz}$ | $+A_{yz}$, $-A_{xz}$, $+A_{xy}$ |
| the plane bracket | $[A_{jk},iS_{jk}]$ against $2i(E_{jj}-E_{kk})$ | $15/15$ exact |
| the left triple | $[T^{L}_{a},T^{L}_{b}]$ against $\epsilon_{abc}T^{L}_{c}$ | $3/3$ exact |
| the right triple | $[T^{R}_{a},T^{R}_{b}]$ against $-\epsilon_{abc}T^{R}_{c}$ | $3/3$ exact |
| the two triples commute | $[T^{L}_{a},T^{R}_{b}]$ | $0$, nine of nine |
| the recombination | $T^{L}_{x}+\tfrac12(A_{tx}+A_{yz})$, $T^{R}_{x}+\tfrac12(A_{tx}-A_{yz})$ | $0$ and $0$ |
| the masses | $\operatorname{tr}([X,\Phi_0]^{\dagger}[X,\Phi_0])$ | $32v^{2}$ six times, $0$ nine times, $8v^{2}$ on the six weak |
| the Gram of the fifteen | $105$ pairs | one nonzero, $\operatorname{tr}(d_{2}d_{3})=+1$ |

## Summary

**Twenty-one arrays, one per boson, and the index at the top is the whole table of contents.** Three of $\mathfrak{su}(2)_L$, three of $\mathfrak{su}(2)_R$, and the fifteen of $\mathfrak{su}(4)$: one corner, six leptoquarks, six off-diagonal gluons and two colour diagonals.

**Two behaviours and not twenty-one.** A real plane array has a real orthogonal exponential and turns its plane; an imaginary one has a unitary exponential and phases its lines. **Only the six weak arrays and the six real planes rotate the quartet**, and the three parts of the article follow that split.

**Three spectra.** $0,0,\pm i$ on the fourteen plane and diagonal arrays, $\pm\tfrac i2$ twice on the six weak arrays, $-3i,i,i,i$ on the corner. **Nothing else appears**, and that is why every exponential in the article has a closed form.

**Two masses and one artefact.** $32v^{2}$ on the six leptoquark arrays, zero on the nine colour and corner arrays, $8v^{2}$ on the six weak arrays where the number is not a mass. **The $32$ is twice the square of the vacuum's lepton-minus-colour difference**, and the zeros are the two facts that $D$ is a multiple of the identity on colour and that it commutes with itself.

**Every array closes with its partner.** $[A_{jk},iS_{jk}]=2i(E_{jj}-E_{kk})$ holds on all fifteen planes and gives $2d_{2}$, $2(d_{2}+d_{3})$ and $2d_{3}$ in the colour block, one diagonal combination per leptoquark plane, and nothing new at the corner.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $E_{jk}$ | the matrix unit in the order $(t,x,y,z)$ |
| $A_{jk}$ | $E_{jk}-E_{kj}$, the real array of the plane $\{j,k\}$ |
| $iS_{jk}$ | $i(E_{jk}+E_{kj})$, the imaginary array of the same plane |
| $iD$ | $i(W_{xx}+W_{yy}+W_{zz})=i\operatorname{diag}(-3,1,1,1)$, the corner |
| $d_{2}$, $d_{3}$ | the two colour diagonals, $\tfrac i2(W_{yy}-W_{xx})$ and $\tfrac i2(W_{zz}-W_{yy})$ |
| $T^{L}_{a}$, $T^{R}_{a}$ | $\tfrac12L_{\mathrm{axf}}(\vec e_a)$ and $\tfrac12R_{\mathrm{axf}}(\vec e_a)$ |
| $\star$ | the Hodge star of $\mathbb{R}^4$ with the Euclidean metric, $\star^2=+1$ |
| $m^{2}(X)$ | $\operatorname{tr}([X,\Phi_0]^{\dagger}[X,\Phi_0])$, the diagonal entry of the mass matrix |
| $X^{a}$, $\bar X^{a}$ | the two leptoquark amplitudes of colour $a$ |
| $g_{1}\dots g_{7}$ | the six off-diagonal gluons, named by the cell they occupy |
| $T^{c}_{3}$, $T^{c}_{8}$ | the two colour diagonals, read as $d_{2}$ and $d_{3}$ |
| $v$ | the breaking value: the $\mathrm{SU}(4)$ one in $m^{2}(X)$, the bidoublet's $\sqrt{\kappa^{2}+\kappa'^{2}}$ in the charged block |
| $\kappa$, $\kappa'$, $\beta$ | the bidoublet's two vacuum values and $\tan\beta=\kappa'/\kappa$ |

## Further Reading

- [Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html), which builds every array printed here in three steps.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html), for the frame and the reading by columns.
- [The Rotors of the Twenty-One Generators](the-rotors-of-the-twenty-one-generators-in-the-four-colours-left-right-model-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html), for each exponential and the proof that none of them is a boost.
- [The Commutation Table of the Twenty-One Generators](the-commutation-table-of-the-twenty-one-generators-441-entries-164-nonzero-and-six-rules.html). Every bracket of every array with every other, which is where each fate in the last column of the family table comes from.
- [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html), which computes the $225$ entries the last column of the index comes from.
- [The Adjoint Mass Matrix as the Square of the Roots](the-adjoint-mass-matrix-as-the-square-of-the-roots-two-v-squared-double-commutator-six-planes-and-nine-zeros.html), for the operator behind the $32v^{2}$ and the $9$ zeros.
- [The Mass Matrix of the Twenty-One Gauge Bosons](the-mass-matrix-of-the-twenty-one-gauge-bosons-four-blocks-one-mixing-and-the-nine-zeros.html), for the charged block and the mixing the two weak triples undergo.
- [The Unbroken Subgroup](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html), for the nine and the twelve.
- [Classification of the Bosons](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html), for the grid that names the cells and the ledger.
- [Where the Twenty-One Generators Go](where-the-twenty-one-generators-go-one-ledger-three-readings-and-the-one-abelian-factor.html), which joins this article's twenty-one subsections to the classification's cells in one ledger, names every array printed here, and reads the ledger three ways.
- [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html), which reads the corner entry of $iD$ as the quark–lepton relation: $-3+1+1+1=0$.
- [The Leptoquarks of the Four Colours Left–Right Model](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html) and [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$](quantum-chromodynamics-as-the-residual-of-su4.html), for the two sectors the third part supplies.
