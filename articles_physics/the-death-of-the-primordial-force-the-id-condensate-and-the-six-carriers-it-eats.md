# __The Death of the Primordial Force: The $\langle iD\rangle$ Condensate and the Six Carriers It Eats__

## Introduction

**The layer.** The transition is a statement about a formal copy of the carrier, and its Layer-A content is one diagonal element and its adjoint action. Nothing here needs a potential, a temperature, or a cosmological history: **the death of the primordial force is the adjoint action of one direction on fifteen arrays, and everything else is arithmetic on its spectrum.**

**The question.** What exactly does the condensation do to $\mathrm{SU}(4)$, which generators does it remove from the spectrum, and what do those generators weigh once they are gone?

**The answer.**

$$
\boxed{\;
iD=\operatorname{diag}(-3,1,1,1),\qquad
\operatorname{ad}(iD):\quad 0^{9}\oplus(-4i)^{3}\oplus(+4i)^{3},\qquad
15=9+3+3 ;
\;}
$$

$$
\boxed{\;
\ker\operatorname{ad}(iD)=\mathfrak{u}(3)=\mathfrak{su}(3)_c\oplus\mathfrak{u}(1)_{B-L},\qquad
\text{the sextet is exactly the }\pm4i\text{ eigenspace} ;
\;}
$$

$$
\boxed{\;
M^{2}=2v^{2}\bigl[D,[D,\cdot\,]\bigr]=\operatorname{diag}\bigl(\underbrace{32v^{2},\dots,32v^{2}}_{6},\underbrace{0,\dots,0}_{9}\bigr).
\;}
$$

**So the death is one line of spectral theory.** A single diagonal direction, with eigenvalue pattern $(-3,1,1,1)$, commutes with nine arrays and moves six; the six it moves are the six that acquire mass, and the nine it fixes are the nine that stay massless.

**What this article establishes.** That the stabiliser of the lepton line is exactly the nine-dimensional $\mathfrak{u}(3)$; that the six generators it breaks are exactly the leptoquark sextet, with $Q=\pm\tfrac23$ and $B-L=\pm\tfrac43$; that their mass is one number per plane, $32v^{2}$; and that the rank does not move, $3\to2+1$, so **the death is a death of dimension and not of rank.**

**Not established.** Nothing here says *why* the condensate forms. The scalar potential is not derived anywhere in the corpus, and this article does not pretend to derive it. **What is established is what follows once the condensate exists** — and that is a great deal, because the entire mass spectrum of the first breaking follows from one direction.

**What "death" means here, stated before it is used.** Two things happen to the six generators at once, and they are the same event seen twice: **they are eaten** (each becomes the longitudinal mode of a now-massive vector) and **they become heavy** ($32v^{2}$ each). Neither is a destruction. **The six are absent from the spectrum below the transition and present in it above; that is what a condensate does to a gauge direction.**

**Where the rest is.** The mass matrix is derived in §*The Mass the Six Acquire*, together with the basis question. The six states are [The Sextet Put Aside](the-sextet-put-aside-six-leptoquarks-above-m-c-and-why-they-are-not-seen.html), which owns their mass relation and their experimental bound. The scalar that condenses is the line in the centre, fixed in §*The Condensate*. **What the six cannot do — become the weak bosons — is [What the Sextet Cannot Do](what-the-sextet-cannot-do-the-charge-theorem-that-rules-out-the-recomposition.html)**, and it is the reason the next article is about an index rather than about debris.

## The Condensate: One Direction, Chosen From the Carrier

**What condenses.** A scalar field acquires a value. In this frame a scalar is not an element of the algebra and not an element of the state module: it is a line in the centre, which is why it can multiply the carrier from either side without a choice. **The value it acquires is a vector, and the direction of that vector is the whole content of the breaking.**

**The direction is the lepton line, and it is not a free choice.** The model's one load-bearing declaration is the canonical split

$$
\mathbf 4=\mathbf 1\oplus\mathbf 3=\mathbb C e_t\oplus\operatorname{span}\{e_x,e_y,e_z\},
$$

**with $e_t$ the lepton and the other three the colours.** The scalar carries one $\mathrm{SU}(4)$ index, so its value is a vector in the carrier, and the declaration says which of the four directions is available: **the one that is not a colour.**

**In components.** Write the vacuum as $D=\operatorname{diag}(\ell,q,q,q)$ in the basis $(e_t,e_x,e_y,e_z)$. The algebra is $\mathfrak{su}(4)$, so the trace vanishes:

$$
\ell+3q=0.
$$

**One equation, four unknowns, and the solution is a line.** Set $q=1$; then $\ell=-3$, and

$$
D=\operatorname{diag}(-3,1,1,1),\qquad iD=\operatorname{diag}(-3i,i,i,i).
$$

**The scale is free and the direction is not.** Any multiple of $D$ gives the same breaking. **So the condensate contributes one dimensionful number — its magnitude $v$ — and one discrete choice, the sign, which changes nothing because every mass is quadratic in $D$.** That is the entire freedom of the first step.

**Why the number $4$ will appear later.** The trace condition is not decoration: it is what turns "the scalar takes a value" into "the scalar takes the only value available". With $q$ fixed the corner is forced. **The $4$ in $32=2\cdot4^{2}$ is exactly $q-\ell=1-(-3)$, the one departure from a multiple of the identity that a trace-free diagonal direction can have.** Change the split of the quartet and the pattern of six and nine changes with it; keep the split and there is nothing left to choose.

**The stabiliser.** The set of arrays that annihilate the vacuum is

$$
\mathfrak{u}(3)=\{X\in\mathfrak{su}(4)\ :\ [iD,X]=0\},
$$

**the block-diagonal matrices acting on the three colour directions, traceless.** Its dimension is $1+9-1=9$: one corner entry, a $3\times3$ block, and the trace condition removing one. **That nine is the whole of the surviving gauge sector, and it is computed, not assumed.**

## The Adjoint Action, Which Is the Whole Theorem

**The object.** For an array $X$ in the fifteen,

$$
\operatorname{ad}(iD)(X)=[iD,X].
$$

**The spectrum.** On the plane arrays it is immediate, and the derivation takes three steps.

**The colour planes commute.** If $j,k\in\{x,y,z\}$ then $[iD,A_{jk}]=0$ and $[iD,iS_{jk}]=0$, because $D$ is a multiple of the identity on that block. **That is six directions with eigenvalue zero, before any work.**

**The corner directions do not commute.** For $a\in\{x,y,z\}$,

$$
[iD,A_{ta}]=(-3i-i)A_{ta}=-4i\,A_{ta},
\qquad
[iD,iS_{ta}]=-4i\,iS_{ta},
$$

**and with the indices in the other order the sign flips,**

$$
[iD,A_{at}]=+4i\,A_{at},\qquad [iD,iS_{at}]=+4i\,iS_{at}.
$$

**The three diagonal directions are in the kernel.** They are linear combinations of $iD$ itself and of the two trace-free colour diagonals, and $[iD,iD]=0$.

**Adding it up.**

| block | directions | eigenvalue of $\operatorname{ad}(iD)$ |
| --- | --- | --- |
| colour planes $A_{jk},iS_{jk}$, $j,k\in\{x,y,z\}$ | $6$ | $0$ |
| the two trace-free colour diagonals | $2$ | $0$ |
| $iD$ itself | $1$ | $0$ |
| $A_{ta},iS_{ta}$ | $6$ | $-4i$ on three, $+4i$ on three |
| **total** | $15$ | $0^{9}\oplus(-4i)^{3}\oplus(+4i)^{3}$ |

**Two readings of one table, and both are used.** The real reading says: **nine directions are fixed and six are moved, and the six are moved by an operator with eigenvalues $\pm4$**, so they pair into three rotation planes. The complex reading says: **the six form two complex three-dimensional eigenspaces, conjugate to each other**, so the sextet is a $\mathbf3$ and a $\bar{\mathbf3}$. **The real pairing and the complex splitting are the same statement, which is why the leptoquarks come in three charge-conjugate pairs.**

**The multiplicities, checked.** $9+3+3=15$; $\operatorname{tr}\operatorname{ad}(iD)=0$ because the spectrum is symmetric; the kernel is nine-dimensional and the image six-dimensional. **No number in the table is a choice.**

## The Six That Are Eaten, Named

**Which six.** The $(-4i)$ and $(+4i)$ eigenspaces are spanned by the planes that touch the lepton line and one colour:

$$
\mathfrak m=\operatorname{span}_{\mathbb C}\{A_{ta},iS_{ta}\ :\ a=x,y,z\},\qquad \dim_{\mathbb C}\mathfrak m=6 .
$$

**Under the unbroken $\mathrm{SU}(3)_c$ they split as a triplet and an antitriplet**, because they carry one colour index:

$$
\mathfrak m=\mathbf 3_{+4/3}\oplus\bar{\mathbf 3}_{-4/3},
\qquad
B-L=\pm\tfrac43,\qquad Q=\tfrac12(B-L)=\pm\tfrac23 .
$$

**The names.** A triplet member with $Q=+\tfrac23$ or $-\tfrac23$ is a leptoquark, written $X$; its conjugate is written $\bar X$. **Six states, three of charge $+\tfrac23$ and three of charge $-\tfrac23$**, each carrying a colour index.

**Why they are eaten, counted in real components.** Breaking fifteen generators to nine removes six, and the Goldstone theorem gives one real scalar degree of freedom per broken generator:

$$
15-9=6\ \text{broken}\quad\Longrightarrow\quad 6\ \text{real components eaten}.
$$

**The scalar supplies them and has two to spare.** A scalar with one $\mathrm{SU}(4)$ index is a complex four, hence eight real components; six are eaten and two survive. **Those two are not a loose end: in the fuller organisation they are exactly the two that the second breaking eats when the copy index is gauged**, which is why the corpus's count for this multiplet is eight eaten of sixteen real components, $6+2$, drawn from a doubled index. **The count of six for the $\mathrm{SU}(4)$ step does not depend on whether the copy index is gauged.**

**The eaten six are not destroyed, and the distinction matters for everything that follows.** A Goldstone mode is a rotation of the condensate, and the condensate can be rotated back. **What is absent below the transition is the six as *asymptotic* states; what is present is the six as longitudinal modes of the six massive vectors.** An article that says "the leptoquarks are destroyed" has thrown away the only ingredient the later articles need.

## The Mass the Six Acquire

**The mass matrix.** From the gauge kinetic term evaluated on the vacuum,

$$
\bigl(M^{2}\bigr)_{XY}=2v^{2}\operatorname{tr}\bigl([iD,X]^{\dagger}[iD,Y]\bigr)\Big/\operatorname{tr}(X^{\dagger}Y),
$$

**which is diagonal in the plane basis because $\operatorname{ad}(iD)$ is.** Inserting the spectrum:

$$
M^{2}=\operatorname{diag}\bigl(\underbrace{32v^{2},\dots,32v^{2}}_{6},\underbrace{0,\dots,0}_{9}\bigr).
$$

**Why $32$, in one line.** $32=2\times4^{2}$, and $4=1-(-3)$ is the difference between a colour eigenvalue and the lepton eigenvalue. **A plane's mass is twice the square of the eigenvalue difference across it: a plane touching the lepton line sees the difference, a plane inside the colour triple does not, and a direction along a line cannot see one at all.**

**The table, one row per kind of plane.**

| plane | indices | $m^{2}$ |
| --- | --- | --- |
| $A_{ta},iS_{ta}$ | lepton and colour | $32v^{2}$ |
| $A_{jk},iS_{jk}$ | colour and colour | $0$ |
| the three trace directions | diagonal | $0$ |

**Six planes heavy, nine directions massless, and no cross terms.** The matrix is already diagonal in the basis the algebra hands over, which is why no diagonalisation step appears — **and why the number $32$ can be read off a spectrum rather than solved for.**

**The physical normalisation, so that the number can be compared with an experiment.** With $g_4$ the primordial-force coupling,

$$
M_X^{2}=\tfrac12\,g_4^{2}\,v_R^{2},
$$

**one half, one coupling squared, one vacuum squared, and no free number.** The $32v^{2}$ above differs from this by factors common to every entry — the coupling, the half, the field normalisation — **which cancel in every ratio, so the two statements are one statement in two normalisations.**

**What is *not* claimed.** $32v^{2}$ is not a mass in kilograms. **All couplings here are symbolic**, and the conversion of $v_R$ into a number is an experimental question, treated in the article on the sextet and in the coupling article.

## The General Vacuum, and Why the Kernel Is an Algebra

**One number per plane, at any vacuum.** The corner is one point; the identity behind it is not.

**The general diagonal vacuum.** Let $\Phi_0=\operatorname{diag}(d_1,d_2,d_3,d_4)$ with $\sum_j d_j=0$. The same computation gives

$$
M^{2}=2\,(d_j-d_k)^{2}\,v^{2}\ \text{on the plane }\{j,k\},\qquad
0\ \text{on the three Cartan directions},
$$

so a squared mass is twice the square of a root of the vacuum and a massless generator is one the vacuum does not see.

**The operator form, and why there are two commutators.** With $\mathcal E(X)=[D,[D,X]]$,

$$
M^{2}_{XY}=v^{2}\operatorname{tr}\bigl(X^{\dagger}\,\mathcal E(Y)\bigr),
$$

and in the basis with $\operatorname{tr}(X_a^{\dagger}X_b)=2\delta_{ab}$ the matrix is $2v^{2}$ times the matrix of $\mathcal E$. **One commutator does not preserve the fifteen**: $[A_{jk},D]=(\lambda_k-\lambda_j)S_{jk}$ is real symmetric, outside $\mathfrak{su}(4)$, and the second commutator returns $(\lambda_j-\lambda_k)^{2}A_{jk}$. The mass operator is defined on the fifteen; its square root is not.

**The corner is the degenerate case.** At $D=\operatorname{diag}(-3,1,1,1)$ the three colour entries are equal, so the six roots inside the colour triple vanish. The twelve differences become $\pm4$ three times each and $0$ six times; the square sends the two signs to the single number $32v^{2}$. **The nine-and-six display is a statement about how degenerate the vacuum is**, which is the same statement as "colour is unbroken".

**A regular vacuum, as the check.** At $d=(3,1,-1,-3)v$ the pairwise differences are $2,4,6$, so

$$
M^{2}=2v^{2}\cdot\{\underbrace{4,\dots,4}_{6},\underbrace{16,\dots,16}_{4},\underbrace{36,36}_{2}\},\qquad 0,0,0,
$$

that is $8v^{2}$ six times, $32v^{2}$ four times, $72v^{2}$ twice and three zeros. $6+6+3=15$: twelve roots and three Cartan directions.

**The kernel is a centraliser, hence an algebra.** $\ker M^{2}=\{X:[D,X]=0\}$, and if $[D,X]=[D,Y]=0$ then $[D,[X,Y]]=0$ by the Jacobi identity. **The nine massless generators are therefore closed under the bracket by construction, not by a check of every bracket among them.** A mass matrix whose kernel is a subalgebra is the matrix statement that the breaking leaves a group standing.

## The Nine That Survive, and Why They Are Exactly Nine

**The list.**

| surviving direction | count | name |
| --- | --- | --- |
| $A_{jk},iS_{jk}$ for $j,k\in\{x,y,z\}$ | $8$ | gluons |
| $iD$ | $1$ | $B'$ |
| the two trace-free colour diagonals | counted in the eight | $\lambda_3,\lambda_8$ |

**Eight gluons and one abelian vector.** $\mathfrak{u}(3)=\mathfrak{su}(3)\oplus\mathfrak{u}(1)$ is $8+1=9$, and the corpus's $B'$ is the abelian one — **the fourth-colour direction that survives because colour is a stabiliser and is therefore not broken.**

**The rank does not move, and this is the structural fact to carry forward.**

$$
\operatorname{rank}\mathfrak{su}(4)=3\ \longrightarrow\ \operatorname{rank}\bigl(\mathfrak{su}(3)\oplus\mathfrak{u}(1)\bigr)=2+1=3 .
$$

**The breaking costs dimension and not rank.** A condensate chooses a direction inside the maximal torus, so the torus survives; **that is why colour plus one abelian factor is available as an endpoint and colour plus two weak factors is not.** The second is a rank-five statement, and rank five is not reachable from rank three by any breaking at all — **which is the content of the next two articles, and the reason the weak force cannot be a fragment of what dies here.**

## What Dies and What Does Not

**Four rows, because four different things are true at once.**

| object | before | after | in what sense |
| --- | --- | --- | --- |
| the group | $\mathrm{SU}(4)$, dimension $15$ | $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}$, dimension $9$ | it dies |
| the six leptoquarks | massless gauge directions | massive vectors, $M_X^{2}=\tfrac12g_4^{2}v_R^{2}$ | heavy, not absent from the theory |
| the rank | $3$ | $3$ | it does not move |
| the colour | inside the fifteen | a stabiliser factor | it survives, and survives exactly |

**The sentence to keep.** **The primordial force dies into colour and one abelian factor, and the price of the death is six vectors at $32v^{2}$ and six real scalars absorbed.** Everything else — the rank, the colour, the abelian direction, the vacuum — is unchanged.

**And the sentence that must not be written.** *The leptoquarks are destroyed and their debris becomes the weak force.* The charge theorem of [the companion article](what-the-sextet-cannot-do-the-charge-theorem-that-rules-out-the-recomposition.html) closes that reading: every member of the sextet has $Q=\pm\tfrac23$, so no combination of them reaches $Q=\pm1$. **The death produces colour, one abelian factor, and six heavy vectors. It does not produce a weak doublet.**

## The Checks

| claim | check | result |
| --- | --- | --- |
| the vacuum | trace-free diagonal, $q=1$ | $\ell=-3$, $D=\operatorname{diag}(-3,1,1,1)$ |
| the kernel | $[iD,X]=0$ on the colour block | $6+2+1=9$ |
| the spectrum | $[iD,A_{ta}]=-4iA_{ta}$ | $0^{9}\oplus(\pm4i)^{3}$ |
| the multiplicities | $9+3+3$ | $15$ |
| the trace | the spectrum is symmetric under $X\mapsto-X$ | $\operatorname{tr}\operatorname{ad}(iD)=0$ |
| the sextet's charges | $B-L=\pm\frac43$, $Q=\frac12(B-L)$ | $\pm\frac23$ |
| the sextet's shape | one colour index, one lepton index | $\mathbf3\oplus\bar{\mathbf3}$, $\dim 6$ |
| the eaten count | $15-9$ | $6$ real components |
| the mass | $2(1-(-3))^{2}$ | $32v^{2}$ |
| the massless count | $8$ gluons $+$ $1$ abelian | $9=\dim\mathfrak{u}(3)$ |
| the rank | $2+1$ | $3$, unchanged |
| the physical mass | $\tfrac12g_4^{2}v_R^{2}$ | the same number in another normalisation |

## Distinctions That Are Easy to Lose

A condensate is not a choice of basis. The direction is chosen by the scalar's value; the basis is chosen by the writer, and the spectrum does not care (*The Condensate*).

Eaten is not destroyed. The six leave the asymptotic spectrum and enter it as longitudinal modes; calling them destroyed removes the only object the later articles use (*The Six That Are Eaten*).

$32v^{2}$ is not a mass. It is the coefficient of $v^{2}$; the conversion is a coupling statement and lives elsewhere (*The Mass the Six Acquire*).

The nine are not "the rest". They are exactly the centraliser of the vacuum, and there is a theorem behind the word exactly (*The Nine That Survive*).

The rank is not reduced. Six dimensions leave and the torus stays; that is why the endpoint is $\mathrm{SU}(3)\times\mathrm{U}(1)$ and not something with fewer abelian directions (*What Dies and What Does Not*).

**The six weak generators are not among the fifteen.** The corpus states it in the mass-matrix article and it is worth repeating: on the carrier they are sums of colour and leptoquark planes, and **their masses come from a later breaking through a different vacuum**. **That sentence is the seed of the whole migration**: what dies here is the parent of colour, and the parent of the weak force is a different object.

## Summary

**The transition is one direction.** $iD=\operatorname{diag}(-3,1,1,1)$, forced by the lepton-line declaration and by the trace condition up to scale.

**Its adjoint action is the whole theorem.** $\operatorname{ad}(iD)$ has spectrum $0^{9}\oplus(\pm4i)^{3}$; the kernel is $\mathfrak{u}(3)=\mathfrak{su}(3)_c\oplus\mathfrak{u}(1)_{B-L}$, dimension nine; the $\pm4i$ eigenspace is the leptoquark sextet, $\mathbf3_{+4/3}\oplus\bar{\mathbf3}_{-4/3}$, $Q=\pm\tfrac23$.

**The six are eaten and heavy at once.** Six real scalar components become longitudinal modes, and the six vectors acquire $M^{2}=32v^{2}=2(1-(-3))^{2}v^{2}$ each, equivalently $M_X^{2}=\tfrac12g_4^{2}v_R^{2}$.

**The nine survive exactly.** Eight gluons and $B'$, the centraliser of the vacuum, massless and untouched.

**The rank does not move.** $3\to2+1=3$: the breaking costs dimension and not rank. **That single line is why the weak force cannot come from here**, and it is where the next article begins.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $iD$ | the condensate $\operatorname{diag}(-3i,i,i,i)$, the vacuum direction |
| $\operatorname{ad}(iD)$ | the map $X\mapsto[iD,X]$, whose spectrum squares into the mass matrix |
| $\mathfrak m$ | the sextet, $\mathbf3_{+4/3}\oplus\bar{\mathbf3}_{-4/3}$, the $\pm4i$ eigenspace |
| $X,\bar X$ | a leptoquark and its conjugate, $Q=\pm\tfrac23$, colour $\mathbf3$ or $\bar{\mathbf3}$ |
| $v$ | the magnitude of the condensate, the unit of the adjoint mass matrix |
| $v_R$ | the same magnitude in the normalisation where $M_X^{2}=\tfrac12g_4^{2}v_R^{2}$ |
| $\mathfrak{u}(3)$ | $\mathfrak{su}(3)_c\oplus\mathfrak{u}(1)_{B-L}$, the kernel, dimension $9$ |
| $B'$ | the surviving abelian vector, the $iD$ direction |

## Further Reading

- [The Sextet Put Aside](the-sextet-put-aside-six-leptoquarks-above-m-c-and-why-they-are-not-seen.html). The mass relation, the $K_L\to\mu e$ bound, and the diquark fork.
- [What the Sextet Cannot Do: The Charge Theorem That Rules Out the Recomposition](what-the-sextet-cannot-do-the-charge-theorem-that-rules-out-the-recomposition.html). Why the six cannot become the weak pair.
