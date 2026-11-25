# __The Charge Theorem: The Sextet Cannot Be Recomposed Into the Weak Pair__

## Introduction

**The layer.** The sextet is the complement of a stabiliser in $\mathfrak{su}(4)$, and this article proves two negative results about it. **Both are theorems of the model and neither can be repaired by a better calculation**, which is why they are collected here rather than scattered as remarks.

**The question.** The sextet is six generators and the weak pair is six generators. Why is the obvious identification wrong, and what exactly does the arithmetic say?

**The answer.**

$$
\boxed{\;
Q=\pm\tfrac23\ \text{on every member}\quad\Longrightarrow\quad
\text{colour singlets have }Q\in2\mathbb Z\quad\Longrightarrow\quad Q=\pm1\text{ is unreachable} ;
\;}
$$

$$
\boxed{\;
m_{\text{composite}}\ \gtrsim\ \Lambda_{\text{confine}}=M_C\gtrsim250\ \mathrm{TeV}
\quad\Longrightarrow\quad \text{no }80\ \mathrm{GeV}\text{ composite} ;
\;}
$$

**So the sextet fails twice, on quantum numbers and on size.** The first failure needs no dynamics at all: it is a count on charges that stays true at every coupling. The second needs one line of dimensional analysis: a bound state cannot be lighter than the scale that binds it.

**What this article establishes.** That the charge sum of any colour-singlet state built from sextets is an even integer, hence never $\pm1$; that the specific channel $\mathbf3\otimes\bar{\mathbf3}$ gives $\mathbf1_0\oplus\mathbf8_0$ with the singlet neutral identically, hence six neutral vectors and no charged one; what the six exact additive identities do and do not show, with the mass table that separates an identity from a particle; the $45^\circ$ that a naive reading of the identities would impose, against the measured $28.7^\circ$; and the confinement-scale bound that closes the composite route a second time.

**Not established.** Nothing positive. **This article is the negative half of the migration and it contains no construction**; the construction is [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html), and its whole point is that it does not need the sextet.

**Where the rest is.** The sextet's identity and mass are [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html). The rank argument that runs alongside these two closures is [The Centraliser, the Complement, and the Index](the-centraliser-the-complement-and-the-index-dimension-and-rank.html). The positive construction is the article named above.

## The Charge Theorem

**The data.** Every generator of the sextet carries one lepton index and one colour index, so

$$
B-L=\pm\tfrac43,\qquad Q=\tfrac12(B-L)=\pm\tfrac23 .
$$

**The theorem.** Let $\lvert\psi\rangle$ be any state with zero triality built from sextet states — in particular any colour singlet. Then

$$
Q(\psi)\in2\mathbb Z .
$$

**Proof.** Suppose $\psi$ contains $n$ sextet constituents of charge $+\tfrac23$ and $m$ of charge $-\tfrac23$. Its charge is

$$
Q(\psi)=\tfrac23\,(n-m) .
$$

**Colour neutrality requires zero triality**, and each sextet member carries triality $+1$ or $-1$, so

$$
n-m\equiv0\pmod 3,\qquad\text{say } n-m=3k .
$$

**Substituting,**

$$
Q(\psi)=\tfrac23\cdot3k=2k\in2\mathbb Z . \qquad\square
$$

**Read the theorem.** The smallest non-zero charges available to a colour singlet built from sextets are $\pm2$, $\pm4$, and so on. **The charge $\pm1$ is not merely difficult to reach; it is not in the arithmetic.**

**The same result by parity, which is shorter.** A sum of $N$ terms each $\pm\tfrac23$ equals $\tfrac23(2j-N)$ for integer $j$, so it equals $\pm1$ only if $2(2j-N)=\pm3$, an odd number equal to an even one. **No such $j$ exists.** The triality argument shows why the two routes agree: **colour neutrality forces the count difference to be a multiple of three, and three is what turns the thirds into wholes.**

**Why this is a theorem of the model and not of the notation.** The charges are fixed by the index structure — one lepton index at $B-L=-1$, one colour index at $+\tfrac13$ — and the triality condition is colour neutrality, which any state that could be mistaken for a weak boson must satisfy. **Nothing here depends on a coupling, a scale, a basis, or a vacuum.**

## The Best Channel, Computed

**The most favourable configuration.** A sextet member and an anti-member, since that pair can be a colour singlet:

$$
\mathbf3_{+4/3}\otimes\bar{\mathbf3}_{-4/3}=\mathbf1_{0}\oplus\mathbf8_{0}.
$$

**The singlet is neutral identically.** Its $B-L$ is $+\tfrac43-\tfrac43=0$, hence $Q=\tfrac12\cdot0=0$ — not by cancellation among constituents but because the two contributions are exactly opposite.

**Spin it.** A $\mathbf1$ of colour with a vector bound state has $J=1$ and therefore three spin states:

$$
J=1:\quad m_J=+1,0,-1,\qquad Q=0\ \text{for all three}.
$$

**Three neutral states from one channel.** The weak pair needs four charged and two neutral; **the channel supplies zero charged and three neutral.**

**Do it twice, once per chirality.** Two chiralities give six neutral vectors and no charged one. **Six for six, and the six are all neutral.** That is the exact opposite of the required content, and it is the sharpest single line in the article: **the count matches, the charge is inverted.**

**Why no other channel helps.** A colour singlet needs equal numbers of $\mathbf3$ and $\bar{\mathbf3}$ in triality, hence $n-m\in3\mathbb Z$, hence charge $2k$ by the theorem. **Every channel is closed by the same argument, at once.** There is no cleverer combination to find.

## What the Six Identities Do Show

**The identities, and they are exact.**

$$
T^{L}_{x}=-\tfrac12\bigl(A_{tx}+A_{yz}\bigr),\qquad
T^{R}_{x}=-\tfrac12\bigl(A_{tx}-A_{yz}\bigr),
$$
$$
T^{L}_{y}=-\tfrac12\bigl(A_{ty}-A_{xz}\bigr),\qquad
T^{R}_{y}=-\tfrac12\bigl(A_{ty}+A_{xz}\bigr),
$$
$$
T^{L}_{z}=-\tfrac12\bigl(A_{tz}+A_{xy}\bigr),\qquad
T^{R}_{z}=-\tfrac12\bigl(A_{tz}-A_{xy}\bigr).
$$

**Three things follow, and all three are worth having.**

**First, the six halves are in $\mathfrak{su}(4)$.** Each is a sum of two plane generators of the fifteen, so $\mathfrak{so}(4)$, spanned by the six arrays, is a real subalgebra of $\mathfrak{su}(4)$. **This is true and it is not the obstruction** — a reader who thinks the six identities prove the weak pair is a fragment of the primordial force has confused *the arrays are in the algebra* with *the pairs are the sextet*.

**Second, every identity is one leptoquark plane and one colour plane, in equal halves.** That is the striking content: **in this basis each half is half primordial and half strong.** A vector built on it would be a coherence between a leptoquark direction and a colour direction.

**Third, the identities are the pair resolution.** They are a canonical rotation inside each $2\times2$ block, they hold in every basis with no reference to any dynamics, and **that is exactly why they cannot encode the mixing.** A statement that is true whatever happens cannot say what happens.

## The Mass Table, Which Is the Point

**The table that separates an identity from a particle.**

| array | the two halves | $m^{2}$ of each half | mass eigenstate? |
| --- | --- | --- | --- |
| $T^{L}_{x}$ | $A_{tx}$ and $A_{yz}$ | $32v^{2}$ and $0$ | **no** |
| $T^{R}_{x}$ | $A_{tx}$ and $A_{yz}$ | $32v^{2}$ and $0$ | **no** |
| $T^{L}_{y},T^{R}_{y}$ | $A_{ty}$ and $A_{xz}$ | $32v^{2}$ and $0$ | **no** |
| $T^{L}_{z},T^{R}_{z}$ | $A_{tz}$ and $A_{xy}$ | $32v^{2}$ and $0$ | **no** |

**Every half is a sum of a state at $32v^{2}$ and a state at $0$.** A sum of a heavy and a massless state is a coherence; it has no mass of its own, and it is not a particle.

**In the pair basis, the mass matrix is visible.** Since $A_{tx}=-(T^{L}_{x}+T^{R}_{x})$ and $A_{yz}=-(T^{L}_{x}-T^{R}_{x})$, the block reads

$$
M^{2}=32v^{2}\begin{pmatrix}1&1\\[2pt]1&1\end{pmatrix},
\qquad\text{eigenvalues }64v^{2},0,
$$

**with the heavy eigenvector $T^{L}_{x}+T^{R}_{x}$ — which is $-A_{tx}$, a leptoquark plane — and the massless one $T^{L}_{x}-T^{R}_{x}$, which is $-A_{yz}$, a colour plane.** **The physical states are the leptoquark and the colour direction; the halves are the $45^\circ$ rotated basis.**

**What a mixing angle needs, and what is missing.** Mass mixing requires degeneracy: $W^{3}$ and $B$ mix into $Z$ and $\gamma$ because both are massless before the breaking. **Here the two halves are split $32v^{2}$ against $0$ — maximally non-degenerate — so there is nothing for them to mix with.** The condensate destroys degeneracy by design, and that is what makes the identities bookkeeping rather than dynamics. **This is the honest sense in which the transition is a breaking: it removes the degeneracy that a mixing would need.**

## The $45^\circ$, and the Factor $2.16$

**If the identities were the mixing, the angle would be fixed, and it is wrong by a factor of two.**

**The coefficients are $\pm\tfrac12$ with equal magnitudes**, so the rotation between the plane basis and the pair basis is exactly $45^\circ$:

$$
\cos\theta=\sin\theta=\tfrac1{\sqrt2},
\qquad
\sin^{2}\theta=0.5 .
$$

**The measured value is**

$$
\sin^{2}\theta_W=0.23122 ,
\qquad
\frac{0.5}{0.23122}=2.16 .
$$

**A factor of $2.16$, and it cannot be adjusted.** The $45^\circ$ comes from the $\tfrac12$ in the identities, which comes from the normalisation of the six halves, which comes from the algebra. **There is no free parameter**: any change that moves the angle also breaks the algebra.

**What this falsifies and what it does not.** It falsifies the reading *the six identities are the electroweak mixing*. It does not falsify the identities, which remain exact; and it does not falsify the construction of the companion article, which never uses the identities as a mixing. **The correct mixing is the corpus's: three neutral fields, two vacua, rank two, one null direction — computed where the $Z$ and the photon actually are.**

## The Second Closure: Confinement Scale

**A bound state weighs at least the scale that binds it.**

$$
m_{\text{composite}}\ \gtrsim\ \Lambda_{\text{confine}} .
$$

**This is not a dynamical preference; it is what a bound state is.** In QCD the lightest vector is $776\ \mathrm{MeV}$ against constituents of about $330\ \mathrm{MeV}$ each, a ratio of $1.18$: **the confinement scale is what the mass is made of.**

**In this model the confinement scale is fixed by experiment.** The sextet's own bound is

$$
M_X=M_C\ \gtrsim4.0\times10^{-5}\ \mathrm{J}=2.5\times10^{5}\ \mathrm{GeV}=250\ \mathrm{TeV},
$$

**from $K_L\to\mu e$ and not from proton decay**, because $B$ moves in thirds and the leading operator is dimension nine.

**So any $\mathrm{SU}(4)$-bound object weighs hundreds of teraelectronvolts.** An $80.4\ \mathrm{GeV}$ composite would need a confinement scale of order $80\ \mathrm{GeV}$; **this model's confinement scale is above that by at least three and a half decades, and it is not a parameter that can be dialled** — lowering it would put the sextet inside the reach of a kaon decay that has not been seen.

**Two numbers, because the scale has a floor and a preference.**

| where $M_C$ sits | $M_C/M_W$ | decades |
| --- | --- | --- |
| the flavour floor, $2.5\times10^{5}$ GeV | $3.1\times10^{3}$ | $3.49$ |
| the unification preference, $\sim10^{13}$ GeV | $1.2\times10^{11}$ | $11.1$ |

**Both close the route, and the floor is the number quoted above**, because the floor holds whatever one believes about unification. **Twenty-two was an earlier draft's error**: it came from a $10^{15}$ GeV proton-decay bound that this sector does not carry.

## What the Identities Establish

**Two things, and both belong in the corpus.**

**A bookkeeping identity.** They give the six halves in the basis the mass matrix is diagonal in, which is exactly what a reader needs in order to compute what each half weighs in that basis. **The answer is the mass table**, and the mass table is what shows that the halves are not mass eigenstates.

**A structural identity.** They show that $\mathfrak{so}(4)$ sits inside $\mathfrak{su}(4)$ as a real subalgebra, and they show *how*: by pairing each leptoquark plane with a colour plane. **That pairing is the reason the two readings of the fifteen are so close** — the span of the two maximal-rank subgroups is twelve of fifteen, the intersection is four, and the missing three are exactly the directions that the identities cannot reach. **The identities are the visible tip of that closeness, and the closeness is what makes the wrong story attractive.**

**And one thing they are not good for.** They are not a mechanism. **Every statement above is true before and after the transition, at every scale, and in the presence or absence of any dynamics.** A formula with that property is a statement about a basis, and the corpus's own article on the mass matrix says so when it warns that the half in $T^{L}_{x}$ appears twice and is not a mass.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the sextet's charges | $B-L=\pm\frac43$ | $Q=\pm\frac23$ |
| colour-singlet charge | $n-m\in3\mathbb Z$, $Q=\frac23(n-m)$ | $Q\in2\mathbb Z$ |
| the parity route | $\frac23(2j-N)=\pm1$ | $2(2j-N)=\pm3$, impossible |
| the pair channel | $\mathbf3\otimes\bar{\mathbf3}$ | $\mathbf1_0\oplus\mathbf8_0$ |
| the singlet's charge | $\frac43-\frac43$ | $0$ |
| the singlet's spin content | $J=1$ | three states, all $Q=0$ |
| two chiralities | $2\times3$ | six neutral, zero charged |
| each half's two terms | one $A_{ta}$, one $A_{jk}$ | $32v^{2}$ and $0$ |
| the block in the pair basis | $32v^{2}[[1,1],[1,1]]$ | eigenvalues $64v^{2},0$ |
| the identity's angle | equal coefficients | $45^\circ$, $\sin^{2}=0.5$ |
| the measured angle | $\sin^{2}\theta_W$ | $0.23122$ |
| the discrepancy | $0.5/0.23122$ | $2.16$ |
| the confinement bound | $M_C/M_W$ | $3.49$ at the floor, $11.1$ at $10^{13}$ GeV |
| the pair's closure | $[\mathfrak m,\mathfrak m]$ | $\mathfrak u(3)$, dimension $9$ |

## Distinctions That Are Easy to Lose

An array in the algebra is not a state in the spectrum. $T^{L}_{x}$ is an element of $\mathfrak{su}(4)$ and is not a particle, because it is a sum of a heavy and a massless state (*What the Six Identities Do Show*).

An identity is not a mixing. The identities hold in every basis and at every scale; a mixing angle depends on the dynamics of a mass matrix (*The $45^\circ$*).

Colour neutrality is not automatic. It is the condition that turns thirds into wholes, and it is what makes the charge theorem sharp rather than suggestive (*The Charge Theorem*).

Three and a half decades is a floor and not a ceiling. At the flavour bound the composite route is out by $3.5$ decades; at the unification-preferred scale by $11$. **The smaller number is the honest one and it is still fatal**; an earlier version's twenty-two came from a bound this sector does not carry (*Confinement Scale*).

Six for six is a coincidence of dimension. It says nothing about charge, spin, colour or mass, and the charge is inverted (*The Channel That Looks Best*).

## Summary

**The charge theorem.** Every sextet member has $Q=\pm\tfrac23$; colour neutrality forces $n-m\in3\mathbb Z$; therefore every colour-singlet state built from sextets has $Q\in2\mathbb Z$, and $Q=\pm1$ is unavailable. **A count, true at every coupling.**

**The channel.** $\mathbf3_{+4/3}\otimes\bar{\mathbf3}_{-4/3}=\mathbf1_0\oplus\mathbf8_0$; the singlet is neutral identically; $J=1$ gives three neutral states per chirality, six in all, and no charged state. **The count matches and the charge is inverted.**

**The identities.** Exact, and they show that the six halves are half leptoquark and half colour. **The mass table shows why they are not particles**: $32v^{2}$ against $0$, a coherence and not an eigenstate.

**The angle.** Read as a mixing the identities impose $45^\circ$, against the measured $28.7^\circ$; **a factor $2.16$ that no adjustment can remove.**

**The size.** A bound state weighs at least its confinement scale, and that scale is $250$ TeV. **An $80$ GeV composite is at least three and a half decades out of reach.**

**The verdict.** The sextet is the parent of the strong force and the object the flavour bound measures. **It is not the parent of the weak force, and the reason is arithmetic.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathfrak m$ | the sextet, $\mathbf3_{+4/3}\oplus\bar{\mathbf3}_{-4/3}$ |
| $A_{ta},iS_{ta}$ | leptoquark planes, mass $32v^{2}$ |
| $A_{jk},iS_{jk}$ | colour planes, mass $0$ |
| $T^{L}_{a},T^{R}_{a}$ | the six halves, half leptoquark and half colour |
| $n,m$ | numbers of sextet and anti-sextet constituents |
| $k$ | half the triality count, $n-m=3k$ |
| $M_C$ | the transition scale, $\gtrsim250$ TeV |
| $\sin^{2}\theta_W$ | the measured electroweak mixing, $0.23122$ |

## Further Reading

- [Six Leptoquarks Above $M_C$: Quantum Numbers, the Mass Ratio, and the Bound From $K_L\to\mu e$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html). The sextet's identity, mass and bound.
- [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). The construction that does not need the sextet.
- [The Centraliser, the Complement, and the Index: Dimension Falls at a Breaking, Rank Rises at an Arrival](the-centraliser-the-complement-and-the-index-dimension-and-rank.html). The closure argument that runs beside the charge argument.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). Where $32v^{2}$ and $0$ come from, and the warning about the half in $T^{L}_{x}$.
- [The Weak Sector Below $M_C$](the-weak-sector-below-m-c-three-neutrals-a-diagonal-charged-pair-and-the-bidoublet.html). Where the electroweak mixing is actually computed.
