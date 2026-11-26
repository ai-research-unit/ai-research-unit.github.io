# __Construction of the AXF Matrices of the Rotors of the Fifteen Generators: One Closed Form per Array, and Where the Half Angle Comes From__

## Introduction

**This article exponentiates the fifteen arrays that [the construction article](construction-of-the-axf-matrices-of-the-fifteen-generators.html) builds, and prints the fifteen answers.** The construction article supplies the directions; this article supplies the motion along them, one closed form per array, in the same axis-free frame and with the same names. **The order is not the construction article's**, and it is explained in the next paragraph.

**Three articles, three questions, and the division is deliberate.** [The construction article](construction-of-the-axf-matrices-of-the-fifteen-generators.html) answers *what is the array*. [The rotors article](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) answers *which space does it turn, and why is none of them a boost*. **This article answers only *what is the turned thing, written out*** — and it does so for all fifteen rather than for the few the theorem needs.

**One structural fact makes all of this elementary, and it is worth stating before anything is computed: every one of the fifteen arrays squares to a diagonal matrix.** Fourteen of them square to a scalar multiple of a rank-two projector, and the corner squares to a diagonal with two distinct values. **Because the square is diagonal, the exponential is a two-term formula, and no eigen-decomposition is ever needed.**

**What this article establishes that the two companions do not state.** The fifteen rotors are fifteen one-parameter circles, and **the six arrays $T^{L}_{a}$, $T^{R}_{a}$ are not a sixteenth family**: each of them is a half-sum of two of these circles, and its rotor is a product of two of the rotors printed here, exactly and not approximately. **So the half angle is not a feature of this model's bosons.** It is what a rotation looks like when it is read in a basis half way between two rotors, and §*Where the Half Angle Comes From* shows the composition in both directions.

## Conventions

**The names and the basis are the construction article's, and nothing is renamed here.** The order is not the construction article's. **The twelve real arrays come first and the nine complex ones second, because that split is the eigenspace decomposition of one involution of $\mathfrak{su}(4)$ and not a choice of presentation**: complex conjugation on $\mathfrak{su}(4)$ is minus transpose, its fixed set is $\mathfrak{so}(4)$, the six-dimensional algebra of the real quartet, and its other eigenspace is nine-dimensional. [The Relation between $\mathfrak{su}(4)$ and $\mathfrak{so}(4)$](../articles_internal/structures/structure-SU4-SO4-relations.html) proves the decomposition, counts it, and answers the objection that the construction article's pairing $\{A_{jk},iS_{jk}\}$ is more economical. **That pairing is more economical by one sentence and weaker by one argument**, since it puts one leg in each eigenspace.

$$
\bigl(A_{tx},A_{ty},A_{tz},A_{xy},A_{xz},A_{yz},\ iS_{tx},iS_{ty},iS_{tz},iS_{xy},iS_{xz},iS_{yz},\ iD,d_{2},d_{3},\ T^{L}_{x},T^{L}_{y},T^{L}_{z},T^{R}_{x},T^{R}_{y},T^{R}_{z}\bigr),
$$

**in the basis $(e_{t},e_{x},e_{y},e_{z})$**, with $A_{jk}=E_{jk}-E_{kj}$ the real plane, $iS_{jk}=i(E_{jk}+E_{kj})$ the imaginary plane, $D=\operatorname{diag}(-3,1,1,1)$, $d_{2}=i\operatorname{diag}(0,1,-1,0)$, $d_{3}=i\operatorname{diag}(0,0,1,-1)$, and

$$
T^{L}_{a}=\tfrac12 L_{\vec e_{a}},\qquad T^{R}_{a}=\tfrac12 R_{\vec e_{a}} ,
$$

**with $L$ and $R$ the left and right multiplication by the unit $\vec e_{a}$.** The matrices are printed in [the detail article](the-15-axf-matrices-of-the-bosons-in-detail.html) and are not reprinted except where a rotor needs one.

**One rotor per array, one parameter per rotor.**

$$
R_{a}(\theta)=\exp\bigl(\theta\,G_{a}\bigr),
\qquad
G_{a}\ \text{anti-hermitian},
$$

**and the hermitian reading is the same rotor with the sign of the parameter flipped.** With the hermitian generator $iG_{a}$ — the printed array times $i$, unnormalised — $\exp(i\theta\,iG_{a})=\exp(-\theta G_{a})=R_{a}(-\theta)$, **so nothing is lost and nothing is gained by the change of convention.** The article uses the anti-hermitian $G$ because that is what the construction article prints; the action of [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) uses $t_{a}=iG_{a}/\sqrt{2\operatorname{tr}(G_{a}^{\dagger}G_{a})}$, and the rescaling only changes what the parameter $\theta$ is called.

**Every rotor has determinant one, and the reason is one line.** Since $\operatorname{tr}G_{a}=0$ for all fifteen — the planes are off-diagonal and the diagonals are traceless — we have $\det R_{a}(\theta)=\exp(\theta\operatorname{tr}G_{a})=1$. **So all fifteen rotors sit in $\mathrm{SU}(4)$, and the six whose arrays are real sit in $\mathrm{SO}(4)$.**

## The One Formula, and the Fourteen Arrays It Covers

**Fourteen of the fifteen arrays obey $G^{2}=-\omega^{2}P$ with $P$ a projector, and then the exponential is three terms.**

$$
G^{2}=-\omega^{2}P,\quad P^{2}=P
\qquad\Longrightarrow\qquad
\exp(\theta G)=\mathbb{1}+\frac{\sin\omega\theta}{\omega}\,G+\frac{1-\cos\omega\theta}{\omega^{2}}\,G^{2}.
$$

**The proof is that $G^{3}=-\omega^{2}PG=-\omega^{2}G$, so the series closes after two powers** and the two coefficients are the sine and the versine. **Nothing about the dimension or the carrier is used beyond that identity.**

| family | count | $G^{2}$ | $\omega$ | $\operatorname{tr}G^{2}$ |
| --- | --- | --- | --- | --- |
| real planes $A_{jk}$ | $6$ | $-\bigl(E_{jj}+E_{kk}\bigr)$ | $1$ | $-2$ |
| imaginary planes $iS_{jk}$ | $6$ | $-\bigl(E_{jj}+E_{kk}\bigr)$ | $1$ | $-2$ |
| colour diagonals $d_{2},d_{3}$ | $2$ | $-\bigl(E_{jj}+E_{kk}\bigr)$ | $1$ | $-2$ |
| corner $iD$ | $1$ | $-\operatorname{diag}(9,1,1,1)$ | $3$ on $e_{t}$, $1$ on the triple | $-12$ |
| the halves $T^{L}_{a},T^{R}_{a}$ | $6$ | $-\tfrac14\mathbb{1}$ | $\tfrac12$ | $-1$ |

**The corner is the one array whose square is not a scalar multiple of a projector, and it is handled as two blocks of the same formula**: $\omega=3$ on the lepton line and $\omega=1$ on the colour triple. **That is the whole of its exceptional treatment**, and the two-block reading is what produces the four phases rather than two.

**The half in $T^{L}_{a}=\tfrac12L_{\vec e_{a}}$ is exactly the half angle in its rotor.** It is the only place where the parameter and the turned angle differ, **and it belongs to a composite and not to a generator**: the model's fifteen have no half angle, because none of them is half of another. **A reader who expects $\theta$ and finds $\theta/2$ has found the $\tfrac12$ of a basis that is not this model's.**

**The formula was checked against a Taylor series at $\theta=0.37$ for all fifteen arrays, maximum deviation $9.3\times10^{-16}$.** The check is one line of arithmetic per family and it is in the table at the end.

## The Six Real Planes: Rotors of the Quartet

**A real plane gives a real orthogonal rotor, so these six turn the quartet itself.**

$$
\exp\bigl(\theta A_{tx}\bigr)=
\begin{pmatrix}
\cos\theta&\sin\theta&0&0\\
-\sin\theta&\cos\theta&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\qquad
\exp\bigl(\theta A_{xy}\bigr)=
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&\sin\theta&0\\
0&-\sin\theta&\cos\theta&0\\
0&0&0&1
\end{pmatrix}.
$$

**The action on a basis vector is read off one column**, $e_{t}\mapsto\cos\theta\,e_{t}-\sin\theta\,e_{x}$ and $e_{x}\mapsto\cos\theta\,e_{x}-\sin\theta\,e_{y}$, which are the two images the rotors article quotes. **The plane is turned by $\theta$ and the two complementary lines are fixed**, so the rotor is a rotation in a two-plane and the identity elsewhere.

**The period is $2\pi$ and the half period is worth naming once.**

$$
R_{A}(\pi)=\text{the sign flip on the turned plane},\qquad R_{A}(2\pi)=\mathbb{1} .
$$

**Concretely $\exp(\pi A_{xy})=\operatorname{diag}(1,-1,-1,1)$**: at half a turn the rotor is not a rotation by $\pi$ in the plane alone but the diagonal sign flip that also fixes the two untouched lines, and **that element is the one a reader will meet again as a $\mathbb{Z}_{2}$ of the group.** At a full turn the rotor returns to the identity, which is what separates this family from the weak one below.

**The six split three and three by what they carry.** The three $A_{bc}$ turn the colour triple and fix the lepton line; the three $A_{ta}$ carry the lepton line into colour and back. **That is the geometric content of the statement that colour is a stabiliser and the leptoquarks are not**, and it is read from the rotor in one line: $R_{A_{bc}}(\theta)e_{t}=e_{t}$ for every $\theta$, while $R_{A_{ta}}(\theta)e_{t}\ne e_{t}$ as soon as $\theta\ne0$.

## The Six Imaginary Planes: Rotors of the Complexified Carrier

**The imaginary plane has the same square as the real one and a different exponential, and the difference is one factor of $i$ on the off-diagonal term.**

$$
\exp\bigl(\theta iS_{tx}\bigr)=
\begin{pmatrix}
\cos\theta&i\sin\theta&0&0\\
i\sin\theta&\cos\theta&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
$$

**The matrix is symmetric where the real plane's is antisymmetric, and it is not real.** So $R_{iS}(\theta)$ does not preserve the real quartet for general $\theta$; **it preserves the complexified carrier, and on that carrier it is a rotation in the same plane.** The clean way to say it is with the circular combinations,

$$
\bigl(e_{t}\pm i e_{x}\bigr)\ \longmapsto\ e^{\mp i\theta}\bigl(e_{t}\pm i e_{x}\bigr),
$$

**two eigenvectors with opposite phases and unit modulus.** That is why the corpus calls these arrays "the two phases" and not "the two rotations": on the real lines the rotor mixes with a weight $i\sin\theta$, and on the circular lines it is purely a phase.

**The rotor is real at exactly the half-turns, and there it coincides with the real plane's rotor.**

$$
R_{iS}(\pi)=\operatorname{diag}(1,-1,-1,1)=R_{A}(\pi),
$$

**so the two families meet at $\theta=\pi$ and nowhere else in $(0,2\pi)$.** The statement is exact and it is the sharpest way to see that the imaginary planes are not a second kind of rotation but the same rotation read on a complex basis: **at the half-turn the imaginary weight $\sin\theta$ vanishes and only the real part survives.**

**What the imaginary planes are for, on the rotor side, is the phases of the massless sector.** The corner and the two colour diagonals below are diagonal and give phases outright; the six imaginary planes give the mixing that a phase alone cannot, and **the pair $\{iS_{jk},A_{jk}\}$ together is what makes $\mathfrak{u}(2)$ on the plane** rather than $\mathfrak{so}(2)$ alone.

## The Corner and the Two Colour Diagonals: Three Commuting Rotors and the Torus

**The corner is diagonal, so its rotor is four phases and needs no formula beyond the entrywise exponential.**

$$
\exp\bigl(\theta iD\bigr)=\operatorname{diag}\bigl(e^{-3i\theta},\,e^{i\theta},\,e^{i\theta},\,e^{i\theta}\bigr).
$$

**The lepton line turns three times as fast as each colour line, and the relative phase is four times the parameter.**

$$
\exp\bigl(\theta iD\bigr)=e^{i\theta}\operatorname{diag}\bigl(e^{-4i\theta},1,1,1\bigr),
$$

**which is the display [the charge-quantisation article](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html) prints, character for character.** That is not a coincidence of notation: the article's $N\theta$ relative phase and this article's factor $3$ against $1$ are the same statement, and the two were computed from different starting points.

**The rotor is central exactly four times a turn, and the four values are the fourth roots of unity.**

$$
\exp\Bigl(k\tfrac{\pi}{2}\,iD\Bigr)=i^{k}\,\mathbb{1},
\qquad k=0,1,2,3,
$$

**so $iD$ generates a circle whose image contains the centre four times, and it is the only array of the fifteen that reaches the centre inside a single turn.** The six planes and the two colour diagonals are central only at $\theta\in2\pi\mathbb{Z}$, with value $+1$; **the six composites at $\theta\in2k\pi$, with value $(-1)^{k}$, and that factor is the half angle again.** **Only the corner reaches $i\mathbb{1}$ and $-i\mathbb{1}$, and only it reaches the centre four times in one period.** This is the rotor-side reading of the corpus's "central four times a turn".

**The two colour diagonals give two opposite phases each, and no mixing.**

$$
\exp\bigl(\theta d_{2}\bigr)=\operatorname{diag}\bigl(1,\,e^{i\theta},\,e^{-i\theta},\,1\bigr),
\qquad
\exp\bigl(\theta d_{3}\bigr)=\operatorname{diag}\bigl(1,\,1,\,e^{i\theta},\,e^{-i\theta}\bigr).
$$

**The pair is the diagonal of an $\mathrm{SU}(2)$ acting on two of the three colour lines, with the third line playing the role of the trace**, exactly as the construction article's $d_{2},d_{3}$ are the diagonal of the colour triple with the missing combination the trace.

**These three commute, so their exponentials compose into a three-angle torus and the composition is exact.**

$$
\exp\bigl(\alpha iD+\beta d_{2}+\gamma d_{3}\bigr)
=\operatorname{diag}\Bigl(e^{-3i\alpha},\,e^{i(\alpha+\beta)},\,e^{i(\alpha-\beta+\gamma)},\,e^{i(\alpha-\gamma)}\Bigr),
$$

**four phases with one relation among them, which is rank three.** No Baker–Campbell–Hausdorff correction appears because no bracket is nonzero — **this is the one place among the arrays where a multi-parameter rotor is written in closed form**, and it is closed for the reason the Cartan is abelian.

## Where the Half Angle Comes From

**The composite $T^{L}_{x}$ squares to $-\tfrac14\mathbb{1}$, so its rotor is a half-angle rotation of two planes at once. It is printed here to show that nothing in it is new.**

$$
\exp\bigl(\theta T^{L}_{x}\bigr)=\mathbb{1}\cos\frac{\theta}{2}+2\,T^{L}_{x}\sin\frac{\theta}{2}
=
\begin{pmatrix}
\cos\frac{\theta}{2}&-\sin\frac{\theta}{2}&0&0\\
\sin\frac{\theta}{2}&\cos\frac{\theta}{2}&0&0\\
0&0&\cos\frac{\theta}{2}&-\sin\frac{\theta}{2}\\
0&0&\sin\frac{\theta}{2}&\cos\frac{\theta}{2}
\end{pmatrix}.
$$

**and the two $2\times2$ blocks are identical**, which is the matrix form of "one generator, two planes, the same angle". The $tx$ plane and the $yz$ plane are turned together. **The right-handed partner turns the same $tx$ plane and the opposite $yz$ plane**,

$$
\exp\bigl(\theta T^{R}_{x}\bigr)=
\begin{pmatrix}
\cos\frac{\theta}{2}&-\sin\frac{\theta}{2}&0&0\\
\sin\frac{\theta}{2}&\cos\frac{\theta}{2}&0&0\\
0&0&\cos\frac{\theta}{2}&\sin\frac{\theta}{2}\\
0&0&-\sin\frac{\theta}{2}&\cos\frac{\theta}{2}
\end{pmatrix},
$$

**and the sign difference sits entirely in the second block**, which is the construction article's "the two arrays of one label differ in sign on the plane $\{b,c\}$ and not on $\{t,a\}$", read after exponentiation.

**The period is $4\pi$ in the parameter and $\pi$ in each plane, and the half-turn of the parameter is minus the identity.**

$$
\exp\bigl(2\pi T^{L}_{a}\bigr)=-\mathbb{1},
\qquad
\exp\bigl(4\pi T^{L}_{a}\bigr)=+\mathbb{1}.
$$

**This is the one structural difference between the two kinds of rotor in the model.** A real plane returns to the identity after one turn of its parameter; a half takes two. **The reason is the factor $\tfrac12$ in $T^{L}_{a}=\tfrac12L_{\vec e_{a}}$, and the consequence is that the half's image circle is traversed twice by its parameter** — a statement about the map and not about the subgroup, which is a circle either way.

**Two combinations of the triples are worth naming, because they are the real planes in disguise.**

$$
T^{L}_{x}+T^{R}_{x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}=-A_{tx},
\qquad
T^{L}_{x}-T^{R}_{x}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}=-A_{yz}.
$$

**The sum turns the leptoquark plane and the difference turns the colour plane**, and that is the whole content of the vector-and-axial split in this basis. **One bracket then turns these two displays into a statement about rotors, which is the next section.**

## The Real Plane Rotor, and the Two Half-Angle Rotors Behind It

**A real plane is a sum of two composites, and the two commutation classes of $\mathfrak{so}(4)$ commute.** The identity below is what makes the half angle disappear when it is added to itself.

$$
A_{ta}=-\bigl(T^{L}_{a}+T^{R}_{a}\bigr),
\qquad
A_{bc}=-\bigl(T^{L}_{a}-T^{R}_{a}\bigr)\ \ \text{with }(a,b,c)\ \text{cyclic},
\qquad
\bigl[T^{L}_{a},\,T^{R}_{b}\bigr]=0 .
$$

**Because the two factors commute, the exponential of the sum is the product of the exponentials with no correction term.**

$$
\exp\bigl(\theta A_{ta}\bigr)=\exp\bigl(-\theta T^{L}_{a}\bigr)\exp\bigl(-\theta T^{R}_{a}\bigr),
\qquad
\exp\bigl(\theta A_{bc}\bigr)=\exp\bigl(-\theta T^{L}_{a}\bigr)\exp\bigl(+\theta T^{R}_{a}\bigr)
$$

**and the arithmetic that makes this a real rotation is the arithmetic of half angles.** Each factor turns its plane by $\theta/2$; the two factors turn the same plane when they are summed and opposite planes when they are subtracted; **so the sum turns one plane by $\theta/2+\theta/2=\theta$ and leaves the other alone, and the difference does the reverse.** That is why a half has period $4\pi$ and a real plane has period $2\pi$: the real plane is two half-turns added.

**The six identities, with the coefficients, checked by direct multiplication.** The sign pattern reverses for $A_{xz}$ because the cyclic order $(a,b,c)$ runs $(x,y,z)$ and $A_{xz}$ is the reversed orientation of $A_{zx}$; **that one reversal is the only place in the six where a plus sign appears outside the bracket.**

| real plane | as a pair | coefficient of $T^{L}$ | coefficient of $T^{R}$ |
| --- | --- | --- | --- |
| $A_{tx}$ | $-(T^{L}_{x}+T^{R}_{x})$ | $-1$ | $-1$ |
| $A_{ty}$ | $-(T^{L}_{y}+T^{R}_{y})$ | $-1$ | $-1$ |
| $A_{tz}$ | $-(T^{L}_{z}+T^{R}_{z})$ | $-1$ | $-1$ |
| $A_{yz}$ | $-(T^{L}_{x}-T^{R}_{x})$ | $-1$ | $+1$ |
| $A_{xz}$ | $+\,(T^{L}_{y}-T^{R}_{y})$ | $+1$ | $-1$ |
| $A_{xy}$ | $-(T^{L}_{z}-T^{R}_{z})$ | $-1$ | $+1$ |

**Both the algebra and the rotor identity were verified for all six at two parameter values**, $\theta=0.37$ and $\theta=1.1$, to $10^{-9}$.

**The consequence is a count, and it is the article's main claim.**

$$
15\ \text{independent directions, and}\ 6\ \text{halves that are sums of them},
$$

**because the fifteen arrays span fifteen dimensions as $4\times4$ matrices.** The rank was computed from the fifteen flattened arrays and is $15$; the six real planes are linear combinations of the six composites, and no relation exists among the fifteen. **So the fifteen rotors are fifteen independent circles, and the six composites are exactly what a redundant basis adds** — the shape the counts article describes when it separates names from directions.

**One qualification, and it is now the whole point.** The identity above is a statement about the quartet. **On the model's sixteen fermions only the fifteen act**, each as $t_{a}\otimes\mathbb{1}_{2}$ on the copy index, and the six composites are not operators of that representation at all. **The rotor identity is a quartet-basis statement, and the quartet basis is the one place where a composite has an exponential.** It is not carried to the fermion module, where it has no meaning.

## What the Fifteen Rotors Are Not

**They are not the group.** Fifteen rotors are fifteen one-parameter curves, and the group is fifteen-dimensional. **A general element is $\exp\bigl(\sum_{a}\theta_{a}G_{a}\bigr)$, which for non-commuting generators is not the product $\prod_{a}\exp(\theta_{a}G_{a})$ and is not in general any one of the fifteen.** The three diagonal generators are the exception and the previous section used it: for the Cartan the product and the exponential of the sum coincide.

**They are not rotations of space.** The quartet's three spatial indices $x,y,z$ are the carrier's, and [the rotors article](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) states the caveat in full: the group of the carrier is not the Lorentz group, and the identification of the carrier's triple with laboratory space is an extra input and not a result. **$R_{A_{xy}}(\theta)$ rotates the carrier's triple; whether the apparatus turns with it is a question this article does not touch.**

**None of them is a boost.** $G_{a}$ is anti-hermitian for all fifteen, so $R_{a}(\theta)$ is unitary with unit-modulus eigenvalues and $\operatorname{tr}G_{a}^{2}$ is negative: **it takes the value $-2$ on the twelve planes and two colour diagonals, $-12$ on the corner, and never a positive number.** A boost in the $tx$ plane has $K^{2}=E_{tt}+E_{xx}$, so $\operatorname{tr}K^{2}=+2$; **the sign alone separates the fifteen from every boost, and the smallest gap is the corner's $-12$ against the boost's $+2$.** The rotors article proves this three ways and this article does not re-prove it; the closed forms above are the strongest single illustration, since every one of them is a rotation or a phase and **no hyperbolic function appears in any of the fifteen.**

**Nine of them are not rotors of a real plane.** The six imaginary planes and the three diagonals are complex arrays, so their rotors leave the real quartet at every $\theta$ except the half-turns. **Six rotors of $\mathbb{R}^{4}$ and nine of $\mathbb{C}^{4}$ is the honest split**, and the title's fifteen counts the curves and not fifteen real rotations.

## The Checks

| check | computation | result |
| --- | --- | --- |
| every array squares to a diagonal | $G^{2}$ for all $15$ | no off-diagonal entry |
| the closed form | Taylor against the two-term formula at $\theta=0.37$ | $9.3\times10^{-16}$ |
| the determinant | $\exp(\operatorname{tr}G)$, all fifteen traceless | $1$ |
| the real-array count | arrays with real entries | $6$ real, $9$ complex |
| $R_{A}$ at the half-turn | $\exp(\pi A_{xy})$ | $\operatorname{diag}(1,-1,-1,1)$ |
| $R_{iS}$ at the half-turn | $\exp(\pi iS_{xy})$ against $\exp(\pi A_{xy})$ | equal |
| the corner's phases | $\exp(\theta iD)$ | $e^{-3i\theta}$, $e^{i\theta}$ thrice |
| the corner against the charge article | $e^{i\theta}\operatorname{diag}(e^{-4i\theta},1,1,1)$ | identical |
| the corner's central points | $\exp(k\tfrac{\pi}{2}iD)$ | $i^{k}\mathbb{1}$ |
| the centrality ladder | the parameter at which each family is central | $2\pi$ for the fourteen, $k\tfrac{\pi}{2}$ for the corner, $2k\pi$ for the six |
| the colour diagonals | $\exp(\theta d_{2})$, $\exp(\theta d_{3})$ | $(1,e^{i\theta},e^{-i\theta},1)$, $(1,1,e^{i\theta},e^{-i\theta})$ |
| the torus | $\exp(\alpha iD+\beta d_{2}+\gamma d_{3})$ | four phases, one relation |
| the halves' square | $G^{2}$ for $T^{L}_{a},T^{R}_{a}$ | $-\tfrac14\mathbb{1}$ |
| the halves' period | $\exp(2\pi T)$, $\exp(4\pi T)$ | $-\mathbb{1}$, $+\mathbb{1}$ |
| the halves' bracket | $[T^{L}_{x},T^{R}_{x}]$ | $0$ |
| the sum and the difference | $T^{L}_{x}\pm T^{R}_{x}$ | $-A_{tx}$, $-A_{yz}$ |
| the rotor identity | $\exp(\theta A_{ta})$ against the product | exact at $\theta=0.37$ and $1.1$ |
| the rank | the fifteen as $4\times4$ arrays | $15$ |

## Summary

**The fifteen rotors are the exponentials of the fifteen arrays, and all of them are elementary because all fifteen arrays square to diagonal matrices.** Fourteen obey one two-term formula with a single frequency, and the corner obeys the same formula twice with two frequencies, $3$ on the lepton line and $1$ on the colour triple.

**The rotors fall into a $6+9$ split that the arrays' entries decide.** Six have real entries and give rotations of the quartet with period $2\pi$; nine have complex entries and give unitary rotors of the complexified carrier, real only at the half-turns, where the imaginary planes coincide with the real ones.

**The corner is the only rotor that is ever central, and it is central four times a turn with values $i^{k}$.** That is the rotor-side reading of the corpus's "$B-L$'s eigenvalue is fixed at every scale" — the array is untouched, while the charge it names is broken at the transition — and the display reproduces the charge-quantisation article's relative phase $N\theta$ without being copied from it.

**The article's one new result is the direction of the half angle.** $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$ and $A_{bc}=-(T^{L}_{a}-T^{R}_{a})$, the two triples commute, so the exponentials factorise exactly and the half angles of two composites add to the full angle of a real plane. **Fifteen circles, and six composites that are not circles of the model** — which is why a composite takes two turns of its parameter to return while a real plane takes one, and why the model's bosons have no half angle at all.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $R_{a}(\theta)$ | $\exp(\theta G_{a})$, the rotor of the array $G_{a}$ |
| $G_{a}$ | One of the fifteen arrays, anti-hermitian |
| $\omega$ | The frequency in $G^{2}=-\omega^{2}P$; $1$ or $\tfrac12$ or, for the corner, $3$ and $1$ |
| $P$ | The projector in $G^{2}=-\omega^{2}P$ |
| $T^{L}_{a},T^{R}_{a}$ | $\tfrac12L_{\vec e_{a}}$ and $\tfrac12R_{\vec e_{a}}$ |
| $A_{ta},A_{bc}$ | The real planes, which are minus the sum and minus the difference of the two halves |
| $iS_{jk}$ | The imaginary plane |
| $iD$, $d_{2}$, $d_{3}$ | The corner and the two colour diagonals |
| $12$, $9$ | Rotors of $\mathbb{R}^{4}$ and of $\mathbb{C}^{4}$ |
| $15$ | The rank of the fifteen as $4\times4$ arrays |

## Further Reading

- [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html). The arrays this article exponentiates, in the same order and the same basis.
- [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html). Which space each rotor turns, and the three proofs that none of them is a boost.
- [The Relation between $\mathfrak{su}(4)$ and $\mathfrak{so}(4)$: the Twelve Real Arrays and the Nine Complex Ones](../articles_internal/structures/structure-SU4-SO4-relations.html). Why the order of this article is the split it is, and why the pairing $\{A_{jk},iS_{jk}\}$ is not a substitute.
- [The Fifteen AXF Matrices of the Boson Rotors in Detail](the-15-axf-matrices-of-the-boson-rotors-in-detail-every-matrix-every-boson-its-entries-its-role.html). The same closed forms read one boson at a time: the entries, the fixed lines, and the role of each matrix.
- [The Fifteen AXF Matrices of the Bosons in Detail](the-15-axf-matrices-of-the-bosons-in-detail.html). One subsection per array, with the printed matrix and the spectrum.
- [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). The corner's exponential and the relative phase $N\theta$ that this article's display reproduces.
- [The Counts of the Fifteen](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html). Names against directions, which is the count this article's rank computation confirms.
